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
        page_title="AI PELATIHAN",
        page_icon="👨🏼‍🏫",
        layout="wide",
        initial_sidebar_state="expanded",
    )
 




    # Judul aplikasi
    st.title('AI Pelatihan')

    # Deskripsi menggunakan HTML dan pemisahan baris
    st.write(
        'Gema Foundation mempersembahkan AI hasil pelatihan canggih yang dirancang untuk menghadirkan solusi inovatif dan efisien.<br>'
        'Dengan fokus pada teknologi dan keberlanjutan, AI ini siap menjadi mitra strategis dalam menghadapi tantangan dan menciptakan masa depan yang lebih baik.',
        unsafe_allow_html=True
    )

    # Input pertanyaan dari pengguna dengan placeholder
    question = st.text_area("Masukkan Pertanyaan Anda:", placeholder="Tulis pertanyaan di sini...")

    # Menampilkan kembali pertanyaan pengguna
    if question:
        st.write(f"**Pertanyaan Anda:** {question}")



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
        st.success("Results saved successfully!")

if __name__ == "__main__":
    main()