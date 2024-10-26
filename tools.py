from langchain.tools import DuckDuckGoSearchRun
from langchain_community.tools import TavilySearchResults
from toolkit.file_writer_tool import FileWriterTool
import os
import dotenv
from dotenv import load_dotenv

load_dotenv()
os.environ["TAVILY_API_KEY"] = os.getenv("tavilyapi_key")


file_writer_tool = FileWriterTool()
search_tool = TavilySearchResults(k=5)