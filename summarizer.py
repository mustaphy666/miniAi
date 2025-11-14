from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage

class SummarizerAgent:
    def __init__(self, model="gemini-2.5-flash"):
        self.llm = ChatGoogleGenerativeAI(model=model,
            google_api_key='your_google_api_key_here', temperature=0.7)

    def summarize(self, docs):
        if not docs:
            print("⚠️ No documents to summarize.")
            return ["No summaries generated."]
        
        print("🧠 Summarizing the retrieved documents...")
        combined_text = "\n\n".join(docs)
        try:
            summary = self.llm.invoke(f"Summarize the following text:\n\n{combined_text}")
           # print(summary.content)
            return [summary.content if hasattr(summary, "content") else str(summary)]
        except Exception as e:
            print(f"❌ Summarization failed: {e}")
            return ["Summarization failed."]