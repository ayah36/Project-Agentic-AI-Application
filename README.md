# Project-Agentic-AI-Application
# HR AI Agentic Assistant 🤖

### Overview
This project is an advanced HR system that uses **Multi-Agent Systems (CrewAI)** and **RAG (Retrieval-Augmented Generation)** to analyze HR policies and generate reports.

### Architecture
- **Agents:** Researcher and HR Manager (CrewAI).
- **Tooling:** MCP (Model Context Protocol) connecting the agents to a Flask server.
- **Knowledge Base:** HR Policies hosted on Google Colab (RAG).
- **UI:** Streamlit Dashboard for data visualization.

### How to Run
1. Run the **Colab Notebook** to start the Flask RAG Server and Ngrok tunnel.
2. Update the `MCP_URL` in `mcp_server.py` with the new Ngrok link.
3. Run `crewai run` in the terminal to generate the `report.md`.
