from ..task_template import alpaca_styled_prompt
from langchain.prompts.prompt import PromptTemplate


_PROMPT_TEMPLATE = """Translate a math problem into a expression that can be executed using Python's numexpr library. Use the output of running this code to answer the question.

Question: ${{Question with math problem.}}
```text
${{single line mathematical expression that solves the problem}}
```
...numexpr.evaluate(text)...
```output
${{Output of running the code}}
```
Answer: ${{Answer}}

Begin.

Question: What is 37593 * 67?

```text
37593 * 67
```
...numexpr.evaluate("37593 * 67")...
```output
2518731
```
Answer: 2518731

Question: What is (1+67)*4/9?

```text
(1+67)*4/9
```
...numexpr.evaluate("(1+67)*4/9")...
```output
30.22222222
```
Answer: 30.22222222

Question: {question}

"""


_PROMPT_TEMPLATE_RWKV = alpaca_styled_prompt(instruction=_PROMPT_TEMPLATE, response="")

LLM_MATH_PROMPT = PromptTemplate(
    input_variables=["question"],
    template=_PROMPT_TEMPLATE_RWKV,
)

