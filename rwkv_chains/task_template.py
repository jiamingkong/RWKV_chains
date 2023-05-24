def generate_prompt(instruction, input=None, response="\n# Response:\n"):
    if input:
        return f"""Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

# Instruction:
{instruction}

# Input:
{input}
{response}
"""
    else:
        return f"""Below is an instruction that describes a task. Write a response that appropriately completes the request.

# Instruction:
{instruction}
{response}
"""
