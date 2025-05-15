# 🤖 AI-Powered Company & Industry Research Assistant

Welcome to the **AI-Powered Company & Industry Research Assistant**! This project leverages the latest in Generative AI and LLM technology to generate insightful research reports, innovative AI/ML use cases, and curated resource collections for any company or industry.

---

## 🚀 Features
- **Comprehensive Industry Research**: Get detailed reports on any company or industry, including market trends, competitor strategies, and unique opportunities.
- **AI/ML Use Case Generation**: Discover tailored, actionable AI/ML and GenAI use cases relevant to your chosen domain.
- **Curated Resource Collection**: Instantly access high-quality datasets, models, libraries, and research papers to support each use case.
- **Interactive Streamlit UI**: Simple, beautiful web interface for seamless user experience.

---

## 🏗️ Project Structure
```
├── app.py                  # Streamlit app entry point
├── requirements.txt        # Python dependencies
├── crew/
│   └── crew_manager.py     # Orchestrates agents and tasks
├── agents/
│   ├── research_agent.py   # Industry research agent
│   ├── usecase_agent.py    # AI use case strategist agent
│   └── resource_agent.py   # Resource curator agent
├── tasks/
│   └── tasks.py            # Task definitions for agents
├── utils/
│   ├── llm_client.py       # LLM API client
│   └── file_writer.py      # Utility for file operations
```

---

## ⚡ Quickstart

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd marketresearch
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment variables**
   - Create a `.env` file in the root directory with your [OpenRouter API key](https://openrouter.ai/) and [Serper API key](https://serper.dev/):
     ```env
     OPENROUTER_API_KEY=your_openrouter_api_key_here
     SERPER_API_KEY=your_serper_api_key_here
     ```

5. **Run the app**
   ```bash
   streamlit run app.py
   ```

---

## 🧠 How It Works
- Enter a company or industry name in the app.
- The system orchestrates multiple AI agents:
  - **Industry Research Specialist**: Analyzes the market, trends, and competitors.
  - **AI Use Case Strategist**: Suggests innovative AI/ML use cases.
  - **Resource Curator**: Finds the best datasets, models, and tools for each use case.
- Results are presented in an interactive, expandable format with clickable resources.

---

## 🛠️ Built With
- [Streamlit](https://streamlit.io/)
- [CrewAI](https://github.com/joaomdmoura/crewAI)
- [OpenRouter LLMs](https://openrouter.ai/)
- [SerperDevTool](https://serper.dev/)

---

## 🙏 Credits
- Project inspired by the latest advancements in AI research and agentic workflows.
- Developed by V V S N Raju Namburi.

---

## 📬 Feedback & Contributions
Pull requests, issues, and suggestions are welcome! Let's make AI research accessible and actionable for everyone. 
