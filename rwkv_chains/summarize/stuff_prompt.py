# flake8: noqa
from langchain.prompts import PromptTemplate
from ..task_template import alpaca_styled_prompt

prompt_template = """
Document:
{text}

-----------

Write a concise summary of the above document.
"""
PROMPT = PromptTemplate(template=alpaca_styled_prompt(instruction=prompt_template), input_variables=["text"])
