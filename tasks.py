from crewai import Agent, Task, Process, Crew
from agents import Agents
from tools import *


class Tasks:
    def __init__(self, event):
        self.information_note = event

    def information_task(self):
        search_task = Task(

            description = """
                Search information based on this query = {} using [search_tool] information related to https://www.biotrop.org/ site if information gathered is not relevant  enaough search from other site
                The Information Retrieval Specialist at SEAMEO BIOTROP is responsible for gathering, organizing, and curating relevant information related to tropical biology, environmental conservation, and sustainable development. This includes sourcing scientific data, research findings, and policy reports to support SEAMEO BIOTROP's mission of addressing key challenges in tropical ecosystems. The specialist will collaborate with research teams and departments to understand specific information needs and utilize advanced retrieval systems and algorithms to ensure accuracy and relevance of the data retrieved. Key responsibilities include:
                - Conducting efficient keyword-based and semantic searches across multiple platforms, focusing on tropical biology, biodiversity, and sustainable management practices.
                - Analyzing and summarizing scientific research and environmental policy reports in a structured format.
                - Validating the credibility of data sources, ensuring that the information aligns with SEAMEO BIOTROP's mission and is reliable for academic and policy use.""".format(self.information_note),
            expected_output = """A comprehensive report that includes:
                            - Data Summaries.
                            - Source Citations.
                            - Recommendations.""", 
            agent=Agents().information_agent(), 
            tools=[search_tool]
        )
        return search_task
