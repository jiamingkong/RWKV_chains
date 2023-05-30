# flake8: noqa
from langchain.prompts import PromptTemplate
from ..task_template import alpaca_styled_prompt
prompt_template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.

{context}
_______________________

According to the context above, answer the question below: {question}
"""
PROMPT = PromptTemplate(
    template=alpaca_styled_prompt(instruction=prompt_template), input_variables=["context", "question"]
)
