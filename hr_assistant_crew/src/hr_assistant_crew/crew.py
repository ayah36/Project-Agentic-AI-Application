import os
from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool  # تم تعديل الاستيراد هنا

load_dotenv()

@CrewBase
class HrAssistantCrew():
    """HrAssistantCrew crew"""

    # تعريف الموديل
    groq_llm = LLM(
        model="groq/llama-3.3-70b-versatile",
        api_key=os.getenv("") # تأكد أن الاسم مطابق لما في ملف .env
    )

    # 1. تعريف الأداة باستخدام decorator @tool
    @tool("Search_Colab_RAG")
    def search_colab_rag(question: str) -> str:
        """Search for actual company policies from the RAG system in Colab. 
        Useful for questions about annual leave, hybrid work, and benefits."""
        import requests
        # رابط ngrok الخاص بك
        url = "https://jenifer-unrelaxing-unbuoyantly.ngrok-free.dev/query"
        try:
            res = requests.post(url, json={"query": question}, timeout=15)
            if res.status_code == 200:
                return res.json().get("answer", "No answer found in RAG.")
            return f"Error: Server returned status {res.status_code}"
        except Exception as e:
            return f"Connection Error: {str(e)}"

    @agent
    def hr_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['hr_researcher'],
            # نمرر اسم الدالة search_colab_rag كأداة
            tools=[self.search_colab_rag], 
            llm=self.groq_llm,
            verbose=True,
            allow_delegation=False
        )

    @agent
    def hr_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['hr_manager'],
            llm=self.groq_llm,
            verbose=True
        )

    @task
    def search_task(self) -> Task:
        return Task(
            config=self.tasks_config['search_task'],
        )

    @task
    def report_task(self) -> Task:
        return Task(
            config=self.tasks_config['report_task'],
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )