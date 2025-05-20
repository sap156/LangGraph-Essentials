# Import necessary modules and classes
from langgraph.graph import StateGraph, START, END, add_messages  # StateGraph manages the state machine, START and END are predefined states, add_messages is used for message handling
from langgraph.types import Command, interrupt  # Command defines transitions and state updates, interrupt allows human intervention
from typing import TypedDict, Annotated, List  # TypedDict defines structured types, Annotated adds metadata, List is for type hinting
from langgraph.checkpoint.memory import MemorySaver  # MemorySaver is used to save and resume state checkpoints
from langchain_groq import ChatGroq  # ChatGroq is an LLM interface
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage  # Message types for interaction
import uuid  # For generating unique thread IDs

# Initialize the LLM
llm = ChatGroq(model="llama-3.1-8b-instant")

# Define the structure of the state used in the state machine
class State(TypedDict): 
    linkedin_topic: str  # The topic for the LinkedIn post
    generated_post: Annotated[List[str], add_messages]  # A list of generated posts
    human_feedback: Annotated[List[str], add_messages]  # A list of human feedback

# Define the model node in the state machine
def model(state: State): 
    """ Here, we're using the LLM to generate a LinkedIn post with human feedback incorporated """

    print("[model] Generating content")
    linkedin_topic = state["linkedin_topic"]
    feedback = state["human_feedback"] if "human_feedback" in state else ["No Feedback yet"]

    # Define the prompt for the LLM
    prompt = f"""

        LinkedIn Topic: {linkedin_topic}
        Human Feedback: {feedback[-1] if feedback else "No feedback yet"}

        Generate a structured and well-written LinkedIn post based on the given topic.

        Consider previous human feedback to refine the response. 
    """

    response = llm.invoke([
        SystemMessage(content="You are an expert LinkedIn content writer"), 
        HumanMessage(content=prompt)
    ])

    generated_linkedin_post = response.content

    print(f"[model_node] Generated post:\n{generated_linkedin_post}\n")

    return {
       "generated_post": [AIMessage(content=generated_linkedin_post)] , 
       "human_feedback": feedback
    }

# Define the human intervention node in the state machine
def human_node(state: State): 
    """Human Intervention node - loops back to model unless input is done"""

    print("\n [human_node] awaiting human feedback...")

    generated_post = state["generated_post"]

    # Interrupt to get user feedback
    user_feedback = interrupt(
        {
            "generated_post": generated_post, 
            "message": "Provide feedback or type 'done' to finish"
        }
    )

    print(f"[human_node] Received human feedback: {user_feedback}")

    # If user types "done", transition to END node
    if user_feedback.lower() == "done": 
        return Command(update={"human_feedback": state["human_feedback"] + ["Finalised"]}, goto="end_node")

    # Otherwise, update feedback and return to model for re-generation
    return Command(update={"human_feedback": state["human_feedback"] + [user_feedback]}, goto="model")

# Define the final node in the state machine
def end_node(state: State): 
    """ Final node """
    print("\n[end_node] Process finished")
    print("Final Generated Post:", state["generated_post"][-1])
    print("Final Human Feedback", state["human_feedback"])
    return {"generated_post": state["generated_post"], "human_feedback": state["human_feedback"]}

# Build the state graph
graph = StateGraph(State)
graph.add_node("model", model)
graph.add_node("human_node", human_node)
graph.add_node("end_node", end_node)

graph.set_entry_point("model")

# Define the flow
graph.add_edge(START, "model")
graph.add_edge("model", "human_node")

graph.set_finish_point("end_node")

# Enable Interrupt mechanism
checkpointer = MemorySaver()
app = graph.compile(checkpointer=checkpointer)

# Define the thread configuration
thread_config = {"configurable": {
    "thread_id": uuid.uuid4()
}}

# Get the LinkedIn topic from the user
linkedin_topic = input("Enter your LinkedIn topic: ")
initial_state = {
    "linkedin_topic": linkedin_topic, 
    "generated_post": [], 
    "human_feedback": []
}

# Stream the application execution
for chunk in app.stream(initial_state, config=thread_config):
    for node_id, value in chunk.items():
        # If we reach an interrupt, continuously ask for human feedback
        if(node_id == "__interrupt__"):
            while True: 
                user_feedback = input("Provide feedback (or type 'done' when finished): ")

                # Resume the graph execution with the user's feedback
                app.invoke(Command(resume=user_feedback), config=thread_config)

                # Exit loop if user says done
                if user_feedback.lower() == "done":
                    break



