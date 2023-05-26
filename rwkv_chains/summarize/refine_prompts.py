# flake8: noqa
from langchain.prompts import PromptTemplate
from ..task_template import alpaca_styled_prompt

REFINE_PROMPT_TMPL = (
    "Your job is to produce a final summary\n"
    "We have provided an existing summary up to a certain point: {existing_answer}\n"
    "We have the opportunity to refine the existing summary"
    "(only if needed) with some more context below.\n"
    "------------\n"
    "{text}\n"
    "------------\n"
    "Given the new context, refine the original summary\n"
    "If the context isn't useful, return the original summary."
)
REFINE_PROMPT = PromptTemplate(
    input_variables=["existing_answer", "text"],
    template=alpaca_styled_prompt(instruction=REFINE_PROMPT_TMPL),
)


prompt_template = """Write a concise summary of the following:


"{text}"
"""
PROMPT = PromptTemplate(template=alpaca_styled_prompt(instruction=prompt_template), input_variables=["text"])
