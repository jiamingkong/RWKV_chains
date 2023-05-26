# flake8: noqa
from langchain.prompts import PromptTemplate
from ..task_template import alpaca_styled_prompt

prompt_template = """

{text}
-----------

Write a concise summary of the above article.
"""
PROMPT = PromptTemplate(
    template=alpaca_styled_prompt(prompt_template),
    input_variables=["text"]
)
