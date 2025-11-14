import streamlit as st
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
st.title("Mini Research Report Generator")
st.write("Generate detailed research reports based on online information.")
query = st.text_input("Enter research topic:")
if st.button("Generate Report",type="primary"):
    from agent import build_graph
    graph = build_graph()
    executable_graph = graph.compile()
    result = executable_graph.invoke({"query": query})
    if hasattr(result, '__dict__'):
        result = vars(result)
    st.subheader("Summaries:")
    summaries = result.get("summaries", [])
    for item in summaries:
        summary_text = item.content if hasattr(item, "content") else str(item)
        st.write(summary_text)
    st.subheader("Final Report:")
    final_report = result.get("write", "")
    st.write(final_report)

    with open("history.txt", "a", encoding="utf-8") as f:
        f.write(f"Query: {query}\n")
        f.write("Summaries:\n")
        for item in final_report:
            summary_text = item.content if hasattr(item, "content") else str(item)
            f.write(f"- {summary_text}\n")
        f.write("\n")
    st.download_button(
        label="Download Report",
        data=final_report,
        file_name="research_report.txt",)
    st.download_button(
        label="Download Summaries",
        data=''.join(str(summaries)),
        file_name="summaries.txt",)