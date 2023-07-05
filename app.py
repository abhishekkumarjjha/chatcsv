import streamlit as st
from agent import query_agent, create_agent


def write_response(response: str):
    """
    Write a response from an agent to a Streamlit app.

    Args:
        response: The response from the agent.

    Returns:
        None.
    """
    st.write(response)


st.title("CSV Summary Generator")

st.write("Please upload your CSV file below.")

data = st.file_uploader("Upload a CSV")

query = st.text_area("Insert your query")

if st.button("Generate Summary", type="primary"):
    # Create an agent from the CSV file.
    agent = create_agent(data)

    # Query the agent.
    response = query_agent(agent=agent, query=query)

    # Write the response to the Streamlit app.
    write_response(response)
