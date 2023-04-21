import os
os.environ["OPENAI_API_KEY"] = "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"

from langchain.llms import OpenAI
llm = OpenAI(temperature=0.9)
text = "What would be a good company name for a company that makes colorful socks?"
print(llm(text))