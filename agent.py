import langchain
from langchain.llms import OpenAI
from langchain.agents import create_pandas_dataframe_agent
import pandas as pd

API_KEY = "[YOUR-OPENAI-KEY]"


def create_agent(filename: str):
    llm = OpenAI(openai_api_key=API_KEY)
    df = pd.read_csv(filename)
    return create_pandas_dataframe_agent(llm, df, verbose=False)

def query_agent(agent, query):
    prompt = (
        """
        If it is just asking a question that requires an answer, reply as follows:
        {"answer": "answer"}
        Example:
        {"answer": "The title with the highest rating is 'Gilead'"}

        If you do not know the answer, reply as follows:
        {"answer": "I do not know."}

        Return all output as a string.
        """
        + query
    )

    response = agent.run(prompt)
    return response.__str__()
