from groq import Groq

API_KEY = input("Enter your Groq API Key: ")

client = Groq(api_key=API_KEY)

documents = {
    "Source 1": """
Artificial Intelligence (AI) is the simulation of human intelligence by machines.
Machine learning is a branch of AI where systems learn from data.
Deep learning is a subset of machine learning based on neural networks.
""",

    "Source 2": """
Generative AI creates text, images, music, code and videos.
Large Language Models include GPT, Llama, Claude and Gemini.
""",

    "Source 3": """
Retrieval-Augmented Generation (RAG) retrieves relevant documents before generating an answer.
It reduces hallucinations and provides answers with citations.
"""
}

system_prompt = """
You are a Research Agent.

Rules:
1. Answer ONLY using the provided sources.
2. If the answer is not available, reply:
'The provided sources do not contain enough information.'
3. Mention the source(s) used at the end.
"""

while True:

    question = input("\nAsk your research question (or type exit): ")

    if question.lower() == "exit":
        break

    context = ""

    for name, text in documents.items():
        context += f"\n{name}\n{text}\n"

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"system",
                "content":system_prompt
            },
            {
                "role":"user",
                "content":f"""
Sources:
{context}

Question:
{question}
"""
            }
        ]
    )

    print("\n-----------------------------")
    print(response.choices[0].message.content)
    print("-----------------------------")
