# Importing necessary modules and classes
from typing import TypedDict, Annotated  # For defining structured types and annotations
from langchain_core.messages import HumanMessage  # Represents a message from a human user
from langgraph.graph import add_messages, StateGraph, END  # Utilities for managing state graphs
from langchain_groq import ChatGroq  # LLM interface (currently unresolved import issue)

# Define the structure of the state used in the state machine
class State(TypedDict): 
    messages: Annotated[list, add_messages]  # A list of messages annotated with the add_messages utility

# Initialize the language model (LLM) with a specific model configuration
llm = ChatGroq(model="llama-3.1-8b-instant")

# Define constants representing different states in the state machine
GENERATE_POST = "generate_post"
GET_REVIEW_DECISION = "get_review_decision"
POST = "post"
COLLECT_FEEDBACK = "collect_feedback"

# Function to generate a LinkedIn post using the LLM
def generate_post(state: State): 
    return {
        "messages": [llm.invoke(state["messages"])]  # Invoke the LLM with the current state messages
    }

# Function to get a review decision from the user
def get_review_decision(state: State):  
    post_content = state["messages"][-1].content  # Extract the content of the last message
    
    print("\n📢 Current LinkedIn Post:\n")
    print(post_content)  # Display the post content to the user
    print("\n")

    decision = input("Post to LinkedIn? (yes/no): ")  # Prompt the user for a decision

    if decision.lower() == "yes":
        return POST  # Transition to the POST state
    else:
        return COLLECT_FEEDBACK  # Transition to the COLLECT_FEEDBACK state

# Function to finalize and post the content
def post(state: State):  
    final_post = state["messages"][-1].content  # Extract the final post content
    print("\n📢 Final LinkedIn Post:\n")
    print(final_post)  # Display the final post content
    print("\n✅ Post has been approved and is now live on LinkedIn!")

# Function to collect feedback from the user
def collect_feedback(state: State):  
    feedback = input("How can I improve this post?")  # Prompt the user for feedback
    return {
        "messages": [HumanMessage(content=feedback)]  # Add the feedback as a new human message
    }

# Create a state graph to manage the workflow
graph = StateGraph(State)

# Add nodes to the state graph, each representing a state and its associated function
graph.add_node(GENERATE_POST, generate_post)
graph.add_node(GET_REVIEW_DECISION, get_review_decision)
graph.add_node(COLLECT_FEEDBACK, collect_feedback)
graph.add_node(POST, post)

# Set the entry point of the state graph
graph.set_entry_point(GENERATE_POST)

# Define transitions between states
graph.add_conditional_edges(GENERATE_POST, get_review_decision)  # Transition from GENERATE_POST to GET_REVIEW_DECISION
graph.add_edge(POST, END)  # Transition from POST to END
graph.add_edge(COLLECT_FEEDBACK, GENERATE_POST)  # Transition from COLLECT_FEEDBACK to GENERATE_POST

# Compile the state graph into an executable application
app = graph.compile()

# Invoke the application with an initial state
response = app.invoke({
    "messages": [HumanMessage(content="Write me a LinkedIn post on AI Agents taking over content creation")]
})

# Print the final response
print(response)











