# flake8: noqa
from langchain.prompts import PromptTemplate
from ..task_template import generate_prompt

prompt_template = """
Document:
{text}
-----------

Write a concise summary of the above document.
"""
PROMPT = PromptTemplate(
    template=generate_prompt(prompt_template),
    input_variables=["text"]
)
