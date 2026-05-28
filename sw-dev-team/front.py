import streamlit as st
import requests
import time

st.set_page_config(
    page_title="AI Software Development Team",
    page_icon="",
    layout="wide"
)


st.title(" AI Software Development Team")
st.caption("Simulating a real AI-powered software company")


with st.sidebar:
    st.header(" Settings")
    st.write("Backend: FastAPI")
    st.write("Agents: CrewAI")

    st.divider()
    st.subheader(" Agents")

    pm_status = st.empty()
    backend_status = st.empty()
    frontend_status = st.empty()


st.subheader("Enter your idea")
prompt = st.text_area("Example: Build a chatbot app")
Api_url= "https://software-developmentteam-simulator.onrender.com"

if st.button(" Build Application"):

    if not prompt.strip():
        st.warning("Please enter a project idea.")
        st.stop()

    
    pm_status.info(" Backend Dev is thinking...")
    backend_status.info(" Backend Dev is working...")
    frontend_status.info(" Frontend Dev is waiting...")

    
    progress = st.progress(0)

    try:
        
        time.sleep(1)
        progress.progress(20)

        
        with st.spinner("Agents are building your project..."):
            res = requests.post(
                Api_url,
                json={"prompt": prompt}
            )

        progress.progress(70)

        data = res.json()

       
        if "error" in data:
            st.error(data["error"])
            st.stop()

        
        time.sleep(1)
        progress.progress(100)

        
        pm_status.success(" Planning completed")
        backend_status.success(" Backend built")
        frontend_status.success(" Frontend built")

        
        st.success(" Project Generated Successfully!")

        st.divider()

        
        tab1, tab2 = st.tabs([" Backend Code", " Frontend Code"])

        with tab1:
            st.subheader("FastAPI Backend")
            st.code(data.get("backend", "No backend output"), language="python")

        with tab2:
            st.subheader("React Frontend")
            st.code(data.get("frontend", "No frontend output"), language="javascript")

       
        st.divider()
        st.subheader("⬇ Download Code")

        col1, col2 = st.columns(2)

        with col1:
            st.download_button(
                label="Download Backend Code",
                data=data.get("backend", ""),
                file_name="backend.py",
                mime="text/plain"
            )

        with col2:
            st.download_button(
                label="Download Frontend Code",
                data=data.get("frontend", ""),
                file_name="frontend.js",
                mime="text/plain"
            )

    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
