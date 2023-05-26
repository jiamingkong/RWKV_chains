from langchain.prompts import PromptTemplate
from .llm_math import LLM_MATH_PROMPT
from .summarize import load_rwkv_summarize_chain
from .llm_bash import LLMBashChain
# from .qa_generation import QAGenerationChain
from .question_answering import load_rwkv_qa_chain

TEMPLATE = """Below is an instruction that describes a task. Write a response that appropriately completes the request.
# Instruction:
{instruction}

# Response:
"""

rwkv_prompt = PromptTemplate(
    input_variables=["instruction"],
    template=TEMPLATE,
)