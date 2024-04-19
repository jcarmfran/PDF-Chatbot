from langchain.prompts import PromptTemplate

WELCOME_MESSAGE = """\
Welcome to Introduction to LLM App Development Sample PDF QA Application!
To get started:
1. Upload a PDF or text file
2. Ask any question about the file!
"""

template = """
Act as an expert financial analyst when you answer questions and pay attention to the financial statements. Operating margin (AKA op margin) and is calculated by dividing opearing income by revenue. Given the following extracted parts of a long document and a question, create a final answer with references ("SOURCES"). 
If you don't know the answer, just say that you don't know. Don't try to make up an answer.
ALWAYS return a "SOURCES" part in your answer with the format "SOURCES: <source 1>, <source 2>, ..."

QUESTION: {question}
=========
{summaries}
=========
FINAL ANSWER:
"""
PROMPT = PromptTemplate(template=template, input_variables=["summaries", "question"])

EXAMPLE_PROMPT = PromptTemplate(
    template="Content: {page_content}\nSource: {source}",
    input_variables=["page_content", "source"],
)
