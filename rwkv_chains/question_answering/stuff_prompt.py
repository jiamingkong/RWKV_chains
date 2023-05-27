# flake8: noqa
from langchain.chains.prompt_selector import ConditionalPromptSelector, is_chat_model
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from ..task_template import alpaca_styled_prompt

prompt_template = """Use the following pieces of context to answer the question at the end. Keep the answer succint and relevant to the context. If you don't know the answer, just say that you don't know, don't try to make up an answer.

{context}


---------------------
According to the context above, answer the question below:
{question}
"""
PROMPT = PromptTemplate(
    template=alpaca_styled_prompt(instruction= prompt_template), input_variables=["context", "question"]
)

system_template = """User: Use the following pieces of context to answer the users question. 
If you don't know the answer, just say that you don't know, don't try to make up an answer.
----------------
{context}"""
messages = [
    SystemMessagePromptTemplate.from_template(system_template),
    HumanMessagePromptTemplate.from_template("{question}"),
]
CHAT_PROMPT = ChatPromptTemplate.from_messages(messages)


PROMPT_SELECTOR = ConditionalPromptSelector(
    default_prompt=PROMPT, conditionals=[(is_chat_model, CHAT_PROMPT)]
)
