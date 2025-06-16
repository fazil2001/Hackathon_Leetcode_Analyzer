# analyzer.py

import pandas as pd
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from .rag import get_topic_benchmark_context
from dotenv import load_dotenv
import os

load_dotenv()

def analyze_submissions(file_path):
    df = pd.read_csv(file_path)

    total = len(df)
    days_active = df['date'].nunique()
    topics_covered = df['topic'].nunique()
    fast_completion = df['date'].value_counts().max() > 10

    feedback = (
        f"📈 You solved **{total} problems** over **{days_active} days**, "
        f"covering **{topics_covered} topics**.\n\n"
    )

    if fast_completion:
        feedback += "⚠️ It looks like you solved too many problems on a few days. Try spreading them out for better retention.\n\n"
    else:
        feedback += "✅ Good pacing! Keep solving consistently over time.\n\n"

    # ✅ Modern LangChain RAG with Google Gemini
    topic_context = get_topic_benchmark_context()

    prompt = PromptTemplate(
        input_variables=["context"],
        template="""
You are a helpful coding interview coach. Based on the following expert prep material, recommend 5 essential LeetCode topics for a student preparing for software interviews.

Expert Material:
{context}

Reply in short bullet points.
"""
    )

    model = ChatGoogleGenerativeAI(
        model="models/gemini-1.5-flash",  # Updated model name
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    # ✅ New chaining style using pipe
    chain = prompt | model
    rag_response = chain.invoke({"context": topic_context})

    return feedback + "🧠 **Recommended Topics to Focus On:**\n\n" + rag_response.content
