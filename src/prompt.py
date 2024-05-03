from langchain.prompts import PromptTemplate

WELCOME_MESSAGE = """\
Hello! I’m your friendly AI assistant. 

I’m here to help you extract and understand information from PDF documents. You can ask me to find specific information, summarize content, or even answer questions based on the content of the PDFs. Just upload your PDF and ask away!

*Please note that while I strive for accuracy, my responses are based on the information available in the document and should be verified for critical applications.*

Let’s get started! 😊

To get started:
1. Upload a PDF or text file
2. Ask any question about the file!
"""

template = """Please act as helpful assistant that answers user queries based on information from the uploaded PDF sources.
Given the following extracted parts of a long document and a question, create a final answer with references ("SOURCES").
If you don't know the answer, just say that you don't know. Don't try to make up an answer.
ALWAYS return a "SOURCES" field in your answer, with the format "SOURCES: <source1>, <source2>, <source3>, ...".

QUESTION: {question}
=========
{summaries}
=========
FINAL ANSWER:"""

PROMPT = PromptTemplate(template=template, input_variables=["summaries", "question"])

EXAMPLE_PROMPT = PromptTemplate(
    template="Content: {page_content}\nSource: {source}",
    input_variables=["page_content", "source"],
)