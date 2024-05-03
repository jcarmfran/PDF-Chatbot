# PDF Chatbot Powered by Chainlit
## Summary
This full end-to-end project culminates in a chatbot that can answer questions from PDF source materials. After upload of the PDF, the user can have queries answered based on the contents of the PDF.

This application project was built to with accommodation in mind. The application file (`app.py`) can be modified to use use either Llama3 or OpenAI's API.   
Opening page:
![pre-input](assets/img/pre-input.png)

Answer following PDF read and user prompt: 
![answer](assets/img/answer.png)

## Technology Stack
1. Python
2. Chainlit
3. Groq
4. Langchain

## Running the App
Prerequisites:
 - Obtain OpenAI API key: Follow [Official Documentation](https://platform.openai.com/docs/quickstart) (up to **Step 1**, really)
 - Obtain LangSmith API Key: [Official Documentation](https://docs.smith.langchain.com/)
 - Obtain Groq(Cloud) API key: [Official Documentation](https://wow.groq.com/) 

Navigate to your local target folder and clone this repository

```
clone https://github.com/jcarmfran/PDF-Chatbot.git
```

Download the required libraries.

```
pip install -r requirements.txt
```

Initialize Chainlit

```
chainlit init

```

Run the application

```
chainlit run app.py
```

Upload your PDF and starting querying!

### Environment Variables
Be sure to set necessary API key/tokens as environment variables in your `.env`. An example of what your file should contain:
```python
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_API_KEY="<YOUR-LANGCHAIN-API-KEY>"
LANGCHAIN_PROJECT="<YOUR-LANGCHAIN-PROJECT-NAME>"
OPENAI_API_KEY="<YOUR-OPENAI-API-KEY>"
GROQ_API_KEY="<YOUR-GROQ-API-KEY>"
HUGGINGFACEHUB_API_TOKEN="<YOUR-HUGGINFACE-API-TOKEN>"
```

Some of the above keys are optional depending on whether you would prefer to source your LLM locally (LLAMA 2/3) or via an API (`OPENAI_API_KEY`). 