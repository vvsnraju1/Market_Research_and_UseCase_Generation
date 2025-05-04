import streamlit as st
import re
from crew.crew_manager import ask

def parse_use_cases(content):
    """Split the AI Use Cases content into individual use cases."""
    use_cases = re.split(r'\n\d+\.\s', content)[1:]  # Skip the intro before '1.'
    return use_cases

def parse_resources(content):
    """Parse the Resource Collection into a dictionary {use case title: list of (name, link, description)}."""
    resources = {}
    matches = re.findall(r'## \d+\. (.*?)\n(.*?)(?=##|\Z)', content, flags=re.S)
    for title, details in matches:
        links = re.findall(r'\[(.*?)\]\((.*?)\)', details)
        description_match = re.search(r'\*\*Description\*\*: (.*?)\n', details)
        description = description_match.group(1) if description_match else ''
        resource_list = []
        for name, link in links:
            resource_list.append({"name": name, "link": link, "description": description})
        resources[title.strip()] = resource_list
    return resources

def main():
    st.title("🤖 AI-Powered Company & Industry Research Assistant")
    st.subheader("Generate insightful research reports and AI use cases.")
    st.markdown(
        "Enter a **company or industry name** to generate a full report with use cases and resources."
    )

    question = st.text_input("Enter the Company/Industry Name:", placeholder="e.g., Tesla, Fintech, Healthcare")

    if 'response' not in st.session_state:
        st.session_state.response = {}

    if st.button("Generate Insights") and question:
        with st.spinner("Thinking hard... 🚀"):
            response = ask(question)
            st.session_state.response = {
                "Industry Research Report": response.tasks_output[0].raw,
                "AI Use Cases": response.tasks_output[1].raw,
                "Resource Collection": response.tasks_output[2].raw
            }

    if st.session_state.response:
        # Display Industry Research
        with st.expander("📊 Industry Research Report", expanded=True):
            st.markdown(st.session_state.response["Industry Research Report"])

        # Parse Use Cases and Resources
        use_cases = parse_use_cases(st.session_state.response["AI Use Cases"])
        resources = parse_resources(st.session_state.response["Resource Collection"])

        st.markdown("## 🤖 AI Use Cases and Related Resources")

        for idx, use_case in enumerate(use_cases, 1):
            with st.expander(f"Use Case {idx}", expanded=False):
                st.markdown(use_case.strip())

                # Try matching resources
                title_search = re.search(r'^(.*?)\n', use_case.strip())
                if title_search:
                    title = title_search.group(1).strip()
                    matched_resources = resources.get(title)
                    if matched_resources:
                        st.markdown("### 📚 Related Resources")
                        for res in matched_resources:
                            res_name = res["name"]
                            res_link = res["link"]
                            res_description = res.get("description", "")
                            st.markdown(f"- [{res_name}]({res_link}) {'- ' + res_description if res_description else ''}")
                    else:
                        st.info("No specific resources linked for this use case.")

if __name__ == "__main__":
    main()
