import os
os.environ["OPENAI_API_KEY"] = "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"

from langchain.llms import OpenAI
llm = OpenAI(temperature=0.9)
text = "What would be a good company name for a company that makes colorful socks?"
print(llm(text))