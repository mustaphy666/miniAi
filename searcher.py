import requests
from bs4 import BeautifulSoup
from readability import Document
from langchain_community.tools import DuckDuckGoSearchResults
class SearchAgent:
    def __init__(self):
        self.search = DuckDuckGoSearchResults(max_results=3)
        
    def search_and_extract(self, query: str, num_results: int = 3):
        print(f"🔍 Searching online for: {query}")
        try:
            results = self.search.run(query)
            if not results:
                print("⚠️ No results found.")
                return ["No content found for summarization."]
            print("✅ Search results retrieved successfully.")
            # Wrap results in a list so summarizer gets a non-empty input
            return [results]
        except Exception as e:
            print(f"❌ Search failed: {e}")
            return ["Search failed."]