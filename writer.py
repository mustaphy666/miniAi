from langchain_google_genai import ChatGoogleGenerativeAI

class WriterAgent:
    def __init__(self, model="gemini-2.5-flash"):
        self.llm = ChatGoogleGenerativeAI(model=model, temperature=0.7,
         google_api_key='your_google_api_key_here')  

    def write(self, summaries):
        print("📝 Writing the final research report...")
        text = "\n".join(summaries)
        prompt = f"""
        You are an academic research writer.
        Using the following summary information, write a detailed, well-structured report (3–5 paragraphs)
        that introduces the topic, discusses key points, and ends with a brief conclusion.
        if you don't have enough information, state that you cannot provide a report.
        if the question is not a research related topic, answer the question by searching the web.
        Summary data:
        {text}
        """
        response = self.llm.invoke(prompt)
        #print(response.content)
        return response.content if hasattr(response, "content") else str(response)