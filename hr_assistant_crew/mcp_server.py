from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("HR_System")

# الرابط اللي أعطاك إياه ngrok
COLAB_URL = "https://exclusionary-axile-glayds.ngrok-free.dev"

@mcp.tool()
def search_hr_rag(question: str) -> str:
    """البحث في سياسات الموارد البشرية الحقيقية عبر الـ RAG في Colab"""
    try:
        response = requests.post(COLAB_URL, json={"query": question}, timeout=30)
        return response.json().get("answer", "No answer found")
    except Exception as e:
        return f"Error connecting to Colab: {str(e)}"

if __name__ == "__main__":
    mcp.run()
