# Import necessary libraries for creating a human-in-the-loop system
from typing import TypedDict, Annotated
from langchain_core.messages import HumanMessage
from langgraph.graph import add_messages, StateGraph, END
from langchain_groq import ChatGroq

# Define the State TypedDict to structure the state of the system
class State(TypedDict): 
    messages: Annotated[list, add_messages]

# Initialize the language model
llm = ChatGroq(model="llama-3.1-8b-instant")

# Define the nodes in the state machine
GENERATE_POST = "generate_post"
GET_REVIEW_DECISION = "get_review_decision"
POST = "post"
COLLECT_FEEDBACK = "collect_feedback"

# Define the generate_post function to generate a LinkedIn post
def generate_post(state: State): 
    return {
        "messages": [llm.invoke(state["messages"])]
    }

# Define the get_review_decision function to get human feedback on the generated post
def get_review_decision(state: State):  
    post_content = state["messages"][-1].content 
    
    print("\n📢 Current LinkedIn Post:\n")
    print(post_content)
    print("\n")

    decision = input("Post to LinkedIn? (yes/no): ")

    if decision.lower() == "yes":
        return POST
    else:
        return COLLECT_FEEDBACK


# Define the post function to simulate posting on LinkedIn
def post(state: State):  
    final_post = state["messages"][-1].content  
    print("\n📢 Final LinkedIn Post:\n")
    print(final_post)
    print("\n✅ Post has been approved and is now live on LinkedIn!")

# Define the collect_feedback function to collect feedback from the human user
def collect_feedback(state: State):  
    feedback = input("How can I improve this post?")
    return {
        "messages": [HumanMessage(content=feedback)]
    }

# Create the state machine graph
graph = StateGraph(State)

# Add nodes to the graph
graph.add_node(GENERATE_POST, generate_post)
graph.add_node(GET_REVIEW_DECISION, get_review_decision)
graph.add_node(COLLECT_FEEDBACK, collect_feedback)
graph.add_node(POST, post)

# Set the entry point for the state machine
graph.set_entry_point(GENERATE_POST)

# Add conditional edges based on the review decision
graph.add_conditional_edges(GENERATE_POST, get_review_decision)
graph.add_edge(POST, END)
graph.add_edge(COLLECT_FEEDBACK, GENERATE_POST)

# Compile the graph into an app
app = graph.compile()

# Invoke the app with an initial human message to generate a LinkedIn post on AI Agents
response = app.invoke({
    "messages": [HumanMessage(content="Write me a LinkedIn post on AI Agents taking over content creation")]
})

# Print the response from the app
print(response)











