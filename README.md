# ChatCSV — Conversational AI for Your Data Files

> Upload any CSV. Ask questions in plain English. Get instant answers powered by GPT.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python) ![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red?logo=streamlit) ![LangChain](https://img.shields.io/badge/LangChain-0.x-green) ![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5%2F4-412991?logo=openai) ![License](https://img.shields.io/badge/License-GPL--2.0-lightgrey)

---

## What It Does

ChatCSV turns any CSV file into a conversational data source. Drop in a spreadsheet — sales data, survey results, financial records — and ask questions the way you'd ask a human analyst. No SQL, no formulas, no pivot tables.

**Example queries:**
- *"What's the average revenue per region?"*
- *"Which product had the highest return rate in Q3?"*
- *"Show me the top 10 customers by total spend."*

The app uses LangChain's CSV agent under the hood, which translates natural language into pandas operations and returns answers with reasoning.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| LLM | OpenAI GPT-3.5 / GPT-4 |
| Agent Framework | LangChain CSV Agent |
| Data Processing | pandas |

---

## Setup & Installation

### Prerequisites
- Python 3.9+ (Anaconda recommended)
- An OpenAI API key → [platform.openai.com](https://platform.openai.com)

### Steps

```bash
# 1. Clone the repo
git clone https://github.com/abhishekkumarjjha/chatcsv.git
cd chatcsv

# 2. Install dependencies
pip install openai langchain pandas python-dotenv streamlit

# 3. Add your OpenAI API key
# Open agent.py and replace [YOUR_API_KEY] with your actual key

# 4. Launch the app
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`.

---

## Usage

1. Upload your `.csv` file using the file uploader
2. Type your question in the chat input
3. The agent analyzes the data and returns an answer with reasoning

---

## Project Structure

```
chatcsv/
├── app.py          # Streamlit UI and main app logic
├── agent.py        # LangChain CSV agent configuration
├── README.md
└── LICENSE
```

---

## Demo

[▶ Watch demo video] : https://github.com/abhishekkumarjjha/chatcsv/assets/127896599/2a4a356f-76eb-4c87-a795-7bc0014d75ae


---

## Author

**Abhishek Kumar Jha**
AI Safety Researcher · Former xAI (Grok) Red Teamer · MS Business Analytics, UT Arlington

[LinkedIn](https://linkedin.com/in/abhishekkumarjjha) · [GitHub](https://github.com/abhishekkumarjjha)

> Built as part of an ongoing portfolio in applied AI and LLM-powered tooling.

---

## License

[GPL-2.0](LICENSE)# chatcsv



