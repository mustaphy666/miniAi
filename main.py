from agent import build_graph

def main():
    
    graph = build_graph()
    query = input("Enter research topic: ")
    executable_graph = graph.compile()
    while True:
        result = executable_graph.invoke({"query": query})
        # If result is a dataclass, convert to dict
        if hasattr(result, '__dict__'):
            result = vars(result)
        print("\n🧾 Summaries:")
        
        summaries = result.get("summaries", [])

        if not isinstance(summaries, list):
            print("Error: 'final_report' is not a list.")
            return
        for item in summaries:
            summary_text = item.content if hasattr(item, "content") else str(item)
            print(summary_text)
        # Print final report
        final_report = result.get("write", [])
        print("\n📝 Final Report:")
        print(final_report)
        # Save query and summaries to history.txt
        with open("history.txt", "a", encoding="utf-8") as f:
            f.write(f"Query: {query}\n")
            f.write("Summaries:\n")
            for item in summaries:
                summary_text = item.content if hasattr(item, "content") else str(item)
                f.write(f"- {summary_text}\n")
            f.write("\n")
        # Remove oldest conversation if more than 5 exist
        with open("history.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
        # Split conversations by blank line
        conversations = []
        conv = []
        for line in lines:
            if line.strip() == "" and conv:
                conversations.append(conv)
                conv = []
            else:
                conv.append(line)
        if conv:
            conversations.append(conv)
        if len(conversations) > 5:
            conversations = conversations[1:]  # Remove first
            with open("history.txt", "w", encoding="utf-8") as f:
                for conv in conversations:
                    f.writelines(conv)
                    f.write("\n")
        query = input("\nEnter research topic (or type 'exit' to quit): ")
        if query.lower() == "exit":
            break

if __name__ == "__main__":
    main()
