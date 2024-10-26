import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from crewai import Agent


load_dotenv()

class Agents:
    def __init__(self):
        self.openaigpt4 = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.2,
            api_key=os.getenv("OPENAI_API_KEY")
        )

    def information_agent(self):
        information = Agent(role="Information Retrieval Specialist",
                    goal="""collect and present relevant information quickly and accurately, supporting data-driven decision making.""",
                        backstory="""Addressing the surge of digital data, this agent is designed to navigate and filter information from multiple sources, helping users find quick solutions in scientific, business, and educational fields....""",
                        verbose=True,
                        llm=self.openaigpt4
                    )
        return information
    
    