# RWKV chains

This git intends to provide a set of prompts to let RWKV models work with Langchain. LLMs are generally trained with different datasets and configurations, making them react differently to the same input. In the case of RWKV, because it is not transformer-based, most prompts built inside LangChain are not compatible with it. Therefore we collected and built a set of prompts in `RWKV_chains` to make LangChain work with RWKV.

## How to use

For now, most of the chains are in `rwkv_chains`, you can simply copy and paste this folder to your project and import the chains you want to use. All the chains that I have tested can be found in `main.ipynb`.

## TODO

- [ ] Add more chains
- [ ] Add more tests
- [ ] Cool examples that runs RWKV with LangChain