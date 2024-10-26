import os
from dotenv import load_dotenv
import streamlit as st
from streamlit.components.v1 import html
from langchain_openai import ChatOpenAI
from crewai import Process, Crew
import base64
from agents import Agents
from tasks import Tasks
from tools import file_writer_tool

load_dotenv()

def main():

    st.set_page_config(
        page_title="BIOTROP AI",
        page_icon="🌾",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    def get_base64_of_bin_file(bin_file):
    
        with open(bin_file, 'rb') as file:
            binary_data = file.read()
            base64_data = base64.b64encode(binary_data).decode('utf-8')
        return base64_data

    image_path = "./Logo/Logo_GEMA.png"
    image_base64 = get_base64_of_bin_file(image_path)

    st.markdown(f"""
        <style>
        .Logo {{
            width: 30vw;
        }}
        </style>
        <img src="data:image/png;base64,{image_base64}" class="Logo">
        """, unsafe_allow_html=True)


    question = st.text_area("Hello Can I help you?:", "Write your question here")
    st.write(f"**Your Question:** {question}")


    openaigpt4 = ChatOpenAI(
        model=os.getenv("OPENAI_MODEL_NAME"),
        temperature=0.2,
        api_key=os.getenv("OPENAI_API_KEY")
    )

    information_crew = Crew(
        agents=[Agents().information_agent()],
        tasks=[Tasks(question).information_task()],
        process=Process.sequential,
        manager_llm=openaigpt4
    )

    start = st.button("Search")
        
    if start:
        results = information_crew.kickoff()
    
        st.markdown("## Results obtained:")
        st.markdown("### Processing...")
        st.write(f"""
            **Answer:**
            {results}
        """)

        results_str = str(results)
        # runner = file_writer_tool._run(filename='example.txt', content=results_str, directory='./note', overwrite=True)
        # print(runner)

        st.success("Results saved successfully!")

if __name__ == "__main__":
    main()