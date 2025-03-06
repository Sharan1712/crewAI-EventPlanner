import streamlit as st
import os
from crewai import LLM

# Streamlit Page Config
st.set_page_config(
    page_title = "AI Event Planner", 
    page_icon = "📅", 
    layout = "wide",
    initial_sidebar_state = "expanded")

# Logo
st.logo(
    "https://cdn.prod.website-files.com/66cf2bfc3ed15b02da0ca770/66d07240057721394308addd_Logo%20(1).svg",
    link = "https://www.crewai.com/",
    size = "large"
)

col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    # Title and description
    st.title("📅AI Event Planner, powered by :red[CrewAI]")
    st.markdown("Create an entire event plan using AI agents.")
    
# Sidebar
with st.sidebar:
    st.markdown("### ⚙️ Model API Configuration")
    st.write("")
    
    model_options = [
        "gpt-4o-mini",
        "gpt-4o",
        "o1",
        "o1-mini", 
        "o1-preview"
        "o3-mini"
    ]
    
    selected_model = st.selectbox("🤖 Select which LLM to use", model_options, key = "selected_model")
    
    with st.expander("🔑 API Keys", expanded = True):
        
        st.info("API keys are stored temporarily in memory and cleared when you close the browser.")
        
        openai_api_key = st.text_input(
            "OpenAI API Key",
            type = "password",
            placeholder = "Enter your OpenAI API key",
            help = "Enter your OpenAI API key"
        )
        
        if openai_api_key:
            os.environ["OPENAI_API_KEY"] = openai_api_key
            
        serper_api_key = st.text_input(
            "Serper API Key",
            type = "password",
            placeholder = "Enter your Serper API key",
            help = "Enter your Serper API key for web search capabilities"
            )
        if serper_api_key:
            os.environ["SERPER_API_KEY"] = serper_api_key
    
    st.write("")
    
    with st.expander("ℹ️ About", expanded=False):
        st.markdown(
            """This Event Planner assistant uses advanced AI models to help you:
                - Research locations for any type of event (Tech, Party, Company Launch etc)
                - Cordinate all logistics for the event. 
                - Prepare a marketing plan for promoting the event.
                
                Choose your preferred model and enter the required API keys to get started.""")
        
# if not os.environ.get("OPENAI_API_KEY"):
#     st.warning("⚠️ Please enter your OpenAI API key in the sidebar to get started")
#     st.stop()

# if not os.environ.get("SERPER_API_KEY"):
#     st.warning("⚠️ Please enter your Serper API key in the sidebar to get started")
#     st.stop()
    
# Create two columns for the input section
input_col1, input_col2 = st.columns([2, 4])

with input_col1:
    event_topic = st.text_area(
        "Event Topic",
        height = 70,
        placeholder = "Enter the main topic of the event..."                
    )

with input_col2:
    event_desc = st.text_area(
        "Event Description",
        height = 70,
        placeholder = "Enter a brief description of the event..."                
    )
    
# Create columns for the input sections
input_col1, input_col2,input_col3, input_col4 = st.columns([2, 2, 2, 2])

with input_col1:
    location = st.text_area(
        "Location",
        height = 70,
        placeholder = "Enter the location where you want the event to take place..."                
    )
    
with input_col2:
    event_date = st.date_input(
        "Event Date",
        value = "today",
        min_value = "today",
        format = "DD.MM.YYYY"
    )
    
with input_col3:
    exp_participants = st.number_input(
        "Expected Participants",
        min_value = 10
    )
    
with input_col4:
    budget_usd = st.number_input(
        "Approximate Budget in USD",
        min_value = 500
    )