# Import necessary libraries for defining data models
from pydantic import BaseModel, Field
from typing import List

# Define the Reflection model
# This model captures critiques of an answer, including missing and superfluous information
class Reflection(BaseModel):
    missing: str = Field(description="Critique of what is missing.")  # Field for missing information
    superfluous: str = Field(description="Critique of what is superfluous")  # Field for superfluous information

# Define the AnswerQuestion model
# This model represents a detailed answer to a question, along with search queries and reflection
class AnswerQuestion(BaseModel):
    """Answer the question."""

    answer: str = Field(
        description="~250 word detailed answer to the question."  # Field for the detailed answer
    )
    search_queries: List[str] = Field(
        description="1-3 search queries for researching improvements to address the critique of your current answer."
    )  # Field for search queries
    reflection: Reflection = Field(
        description="Your reflection on the initial answer."  # Field for the reflection
    )

# Define the ReviseAnswer model
# This model extends AnswerQuestion by adding a references field for citations
class ReviseAnswer(AnswerQuestion):
    """Revise your original answer to your question."""

    references: List[str] = Field(
        description="Citations motivating your updated answer."  # Field for references
    )