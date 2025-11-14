from langgraph.graph import StateGraph
from searcher import SearchAgent
from summarizer import SummarizerAgent
from dataclasses import dataclass, field
from writer import WriterAgent
@dataclass  
class StateSchema:
    query: str = ""
    docs: list = field(default_factory=list)
    summaries: list = field(default_factory=list)
    write:list=field(default_factory=list)
    
def build_graph():
    graph = StateGraph(StateSchema)
    search = SearchAgent()
    summarizer = SummarizerAgent()
    writee= WriterAgent()
    def search_node(state):
        results = search.search_and_extract(state.query)
        state.docs = results
        return state

    def summarize_node(state):
        summaries = summarizer.summarize(state.docs)
        state.summaries = summaries
        return state
    def write_node(state):
        write = writee.write(state.summaries)
        state.write = write
       # print(state.write)
        return state

    graph.add_node("search", search_node)
    graph.add_node("summarize", summarize_node)
    graph.add_node("writee", write_node)
    graph.add_edge("search", "summarize")
    graph.add_edge("summarize", "writee")
    graph.set_entry_point("search")

    return graph
