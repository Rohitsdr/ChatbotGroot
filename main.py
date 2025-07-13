import streamlit as st
import requests
import json
import time
from typing import Optional

# Page configuration
st.set_page_config(
    page_title="Groot Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Simple CSS for clean design
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Creepster&display=swap');
    
    .stApp {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #000000 0%, #1a0000 25%, #330000 50%, #1a0000 75%, #000000 100%);
        background-size: 400% 400%;
        animation: fogShift 8s ease-in-out infinite;
    }
    
    @keyframes fogShift {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    .chat-header {
        background: linear-gradient(135deg, #8b0000 0%, #ff0000 25%, #8b0000 50%, #ff0000 75%, #8b0000 100%);
        background-size: 200% 200%;
        animation: bloodPulse 4s ease-in-out infinite;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
        color: white;
        box-shadow: 0 10px 30px rgba(139, 0, 0, 0.5), inset 0 0 50px rgba(255, 0, 0, 0.3);
        border: 2px solid #ff0000;
        position: relative;
        overflow: hidden;
    }
    
    .chat-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at 30% 30%, rgba(255,255,255,0.1) 0%, transparent 50%),
                    radial-gradient(circle at 70% 70%, rgba(255,0,0,0.2) 0%, transparent 50%);
        animation: fogFloat 6s ease-in-out infinite;
        pointer-events: none;
    }
    
    @keyframes bloodPulse {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    @keyframes fogFloat {
        0%, 100% { opacity: 0.3; transform: translateY(0px); }
        50% { opacity: 0.7; transform: translateY(-10px); }
    }
    
    .chat-title {
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 0 0 20px #ff0000, 0 0 40px #ff0000, 0 0 60px #ff0000;
        font-family: 'Creepster', cursive;
        animation: titleGlow 3s ease-in-out infinite alternate;
        position: relative;
        z-index: 1;
    }
    
    @keyframes titleGlow {
        0% { text-shadow: 0 0 20px #ff0000, 0 0 40px #ff0000, 0 0 60px #ff0000; }
        100% { text-shadow: 0 0 30px #ff0000, 0 0 60px #ff0000, 0 0 90px #ff0000; }
    }
    
    .chat-subtitle {
        font-size: 1.1rem;
        margin-top: 0.5rem;
        opacity: 0.9;
        text-shadow: 0 0 10px #ff6666;
        position: relative;
        z-index: 1;
    }
    
    .chat-container {
        background: rgba(0, 0, 0, 0.8);
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        border: 1px solid #ff0000;
        box-shadow: 0 10px 30px rgba(139, 0, 0, 0.3), inset 0 0 50px rgba(255, 0, 0, 0.1);
        backdrop-filter: blur(10px);
        position: relative;
        overflow: hidden;
    }
    
    .chat-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: 
            radial-gradient(circle at 20% 20%, rgba(255,0,0,0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 80%, rgba(139,0,0,0.1) 0%, transparent 50%),
            radial-gradient(circle at 40% 60%, rgba(255,69,0,0.05) 0%, transparent 50%);
        animation: containerFog 8s ease-in-out infinite;
        pointer-events: none;
    }
    
    @keyframes containerFog {
        0%, 100% { opacity: 0.3; }
        50% { opacity: 0.6; }
    }
    
    .user-message {
        background: linear-gradient(135deg, #8b0000 0%, #ff0000 100%);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 20px 20px 5px 20px;
        margin: 1rem 0;
        margin-left: 20%;
        box-shadow: 0 5px 15px rgba(139, 0, 0, 0.5), inset 0 0 20px rgba(255, 0, 0, 0.3);
        border: 1px solid #ff6666;
        position: relative;
        z-index: 1;
        animation: messageSlide 0.5s ease;
    }
    
    @keyframes messageSlide {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    .bot-message {
        background: linear-gradient(135deg, #330000 0%, #660000 100%);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 20px 20px 20px 5px;
        margin: 1rem 0;
        margin-right: 20%;
        box-shadow: 0 5px 15px rgba(51, 0, 0, 0.5), inset 0 0 20px rgba(255, 0, 0, 0.2);
        border: 1px solid #cc0000;
        position: relative;
        z-index: 1;
        animation: messageSlideLeft 0.5s ease;
    }
    
    @keyframes messageSlideLeft {
        from { transform: translateX(-100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    .loading-message {
        background: linear-gradient(135deg, #4a0000 0%, #800000 100%);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 20px 20px 20px 5px;
        margin: 1rem 0;
        margin-right: 20%;
        text-align: center;
        font-style: italic;
        box-shadow: 0 5px 15px rgba(74, 0, 0, 0.5);
        border: 1px solid #cc0000;
        position: relative;
        z-index: 1;
        animation: loadingPulse 2s ease-in-out infinite;
    }
    
    @keyframes loadingPulse {
        0%, 100% { opacity: 0.7; }
        50% { opacity: 1; }
    }
    
    .quick-action-btn {
        background: linear-gradient(135deg, #8b0000 0%, #ff0000 100%);
        color: white;
        border: 1px solid #ff6666;
        border-radius: 10px;
        padding: 0.75rem 1.5rem;
        font-weight: 500;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(139, 0, 0, 0.4);
        position: relative;
        overflow: hidden;
    }
    
    .quick-action-btn::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        transition: left 0.5s;
    }
    
    .quick-action-btn:hover::before {
        left: 100%;
    }
    
    .quick-action-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(139, 0, 0, 0.6);
        background: linear-gradient(135deg, #ff0000 0%, #cc0000 100%);
    }
    
    .footer {
        text-align: center;
        padding: 1rem;
        background: rgba(0, 0, 0, 0.8);
        border-radius: 10px;
        margin-top: 2rem;
        border: 1px solid #ff0000;
        color: #ff6666;
        box-shadow: 0 5px 15px rgba(139, 0, 0, 0.3);
        backdrop-filter: blur(5px);
    }
    
    /* Input styling */
    .stTextInput > div > div > input {
        background: rgba(0, 0, 0, 0.8);
        border: 2px solid #ff0000;
        border-radius: 25px;
        padding: 1rem 1.5rem;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        color: white;
        box-shadow: 0 5px 15px rgba(139, 0, 0, 0.3);
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #ff6666;
        box-shadow: 0 0 20px rgba(255, 0, 0, 0.5);
        background: rgba(0, 0, 0, 0.9);
    }
    
    .stTextInput > div > div > input::placeholder {
        color: #ff6666;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #8b0000 0%, #ff0000 100%);
        color: white;
        border: 1px solid #ff6666;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(139, 0, 0, 0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(139, 0, 0, 0.6);
        background: linear-gradient(135deg, #ff0000 0%, #cc0000 100%);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #000000 0%, #1a0000 100%);
        border-right: 1px solid #ff0000;
    }
    
    .css-1d391kg .css-1v0mbdj {
        color: #ff6666;
    }
    
    /* Slider styling */
    .stSlider > div > div > div {
        background: rgba(139, 0, 0, 0.3);
    }
    
    .stSlider > div > div > div > div {
        background: #ff0000;
    }
    
    /* Selectbox styling */
    .stSelectbox > div > div {
        background: rgba(0, 0, 0, 0.8);
        border: 1px solid #ff0000;
        color: white;
    }
    
    /* Text styling for sidebar */
    .css-1d391kg h3, .css-1d391kg h4, .css-1d391kg p, .css-1d391kg label {
        color: #ff6666 !important;
    }
    
    /* Fog particles effect */
    .fog-particle {
        position: fixed;
        width: 2px;
        height: 2px;
        background: rgba(255, 0, 0, 0.3);
        border-radius: 50%;
        animation: fogFloat 10s linear infinite;
        pointer-events: none;
        z-index: -1;
    }
    
    .fog-particle:nth-child(1) { top: 10%; left: 10%; animation-delay: 0s; }
    .fog-particle:nth-child(2) { top: 20%; left: 80%; animation-delay: 2s; }
    .fog-particle:nth-child(3) { top: 60%; left: 20%; animation-delay: 4s; }
    .fog-particle:nth-child(4) { top: 80%; left: 70%; animation-delay: 6s; }
    .fog-particle:nth-child(5) { top: 40%; left: 50%; animation-delay: 8s; }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# API Configuration
def get_api_response(prompt: str, api_endpoint: Optional[str] = None, api_key: Optional[str] = None, temperature: float = 0.7, max_tokens: int = 1000) -> dict:
    """
    Make API call to get response for the given prompt
    """
    try:
        # Default to OpenAI-like API format
        if not api_endpoint:
            api_endpoint = "https://api.openai.com/v1/chat/completions"
        
        headers = {
            "Content-Type": "application/json",
        }
        
        if api_key:
            headers["Authorization"] = f"Bearer {api_key}"
        
        # System message for professional tone
        system_message = """You are Groot Chatbot, a helpful and professional AI assistant. You respond in a friendly, informative, and professional manner. You're knowledgeable, clear, and always helpful. Use appropriate emojis sparingly to make responses engaging but not overwhelming."""
        
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": max_tokens,
            "temperature": temperature
        }
        
        # For demo purposes, return a mock response if no API key
        if not api_key:
            time.sleep(1)  # Simulate API delay
            return {
                "success": True,
                "response": f"Hello! I'm Groot Chatbot 🤖\n\nI received your message: '{prompt}'\n\nThis is a demo response. To get real responses, please configure your API settings in the sidebar.\n\nI'm here to help you with any questions or tasks you might have!"
            }
        
        response = requests.post(api_endpoint, headers=headers, json=payload, timeout=30)
        
        if response.status_code == 200:
            data = response.json()
            return {
                "success": True,
                "response": data.get("choices", [{}])[0].get("message", {}).get("content", "No response received")
            }
        else:
            return {
                "success": False,
                "error": f"API Error: {response.status_code} - {response.text}"
            }
    
    except Exception as e:
        return {
            "success": False,
            "error": f"Connection Error: {str(e)}"
        }

# Main application
def main():
    load_css()
    
    # Add fog particles for atmospheric effect
    st.markdown("""
    <div class="fog-particle"></div>
    <div class="fog-particle"></div>
    <div class="fog-particle"></div>
    <div class="fog-particle"></div>
    <div class="fog-particle"></div>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown("""
    <div class="chat-header">
        <h1 class="chat-title">🔥 Groot Chatbot 🔥</h1>
        <p class="chat-subtitle">Your dark AI assistant</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize session state
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'loading' not in st.session_state:
        st.session_state.loading = False
    
    # Sidebar configuration
    with st.sidebar:
        st.markdown("### ⚙️ Configuration")
        
        # API Settings
        st.markdown("#### API Settings")
        api_key = st.text_input("🔑 API Key", 
                               value="sx----------------------------------------------------------------------------------------------------",
                               type="password", 
                               help="Enter your OpenAI API key")
        api_endpoint = st.text_input("🌐 API Endpoint", 
                                   value="https://api.openai.com/v1/chat/completions",
                                   help="API endpoint URL")
        
        # Chat Settings
        st.markdown("#### Chat Settings")
        temperature = st.slider("🌡️ Temperature", 0.0, 2.0, 0.7, 0.1, help="Controls randomness")
        max_tokens = st.slider("📏 Max Tokens", 100, 2000, 1000, 100, help="Maximum response length")
        
        # Clear chat button
        if st.button("🗑️ Clear Chat"):
            st.session_state.messages = []
            st.rerun()
    
    # Main chat interface
    col1, col2, col3 = st.columns([1, 6, 1])
    
    with col2:
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
        
        # Chat history
        for message in st.session_state.messages:
            if message["role"] == "user":
                st.markdown(f'<div class="user-message">👤 You: {message["content"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="bot-message">🤖 Groot: {message["content"]}</div>', unsafe_allow_html=True)
        
        # Loading indicator
        if st.session_state.loading:
            st.markdown('<div class="loading-message">🤖 Groot is thinking...</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Input area
    st.markdown("### 💬 Send a Message")
    
    # Create input form
    with st.form("chat_form", clear_on_submit=True):
        col1, col2 = st.columns([4, 1])
        
        with col1:
            user_input = st.text_input("", 
                                     placeholder="Type your message here...",
                                     label_visibility="collapsed")
        
        with col2:
            submitted = st.form_submit_button("Send 🚀")
    
    # Handle form submission
    if submitted and user_input:
        # Add user message to chat
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Set loading state
        st.session_state.loading = True
        st.rerun()
    
    # Process API call if loading
    if st.session_state.loading:
        # Get the last user message
        last_message = st.session_state.messages[-1]["content"]
        
        # Make API call
        response = get_api_response(last_message, api_endpoint or "", api_key or "")
        
        # Add bot response
        if response["success"]:
            st.session_state.messages.append({"role": "assistant", "content": response["response"]})
        else:
            error_msg = f"❌ Error: {response['error']}\n\nPlease check your API configuration in the sidebar."
            st.session_state.messages.append({"role": "assistant", "content": error_msg})
        
        # Clear loading state
        st.session_state.loading = False
        st.rerun()
    
    # Quick actions
    st.markdown("### ⚡ Quick Actions")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("📚 Get Help", key="help_btn"):
            st.session_state.messages.append({"role": "user", "content": "Can you help me with something?"})
            st.session_state.loading = True
            st.rerun()
    
    with col2:
        if st.button("💡 Ask Question", key="question_btn"):
            st.session_state.messages.append({"role": "user", "content": "I have a question for you"})
            st.session_state.loading = True
            st.rerun()
    
    with col3:
        if st.button("🤝 Chat", key="chat_btn"):
            st.session_state.messages.append({"role": "user", "content": "Let's have a conversation"})
            st.session_state.loading = True
            st.rerun()
    
    with col4:
        if st.button("✨ General", key="general_btn"):
            st.session_state.messages.append({"role": "user", "content": "Tell me something interesting"})
            st.session_state.loading = True
            st.rerun()
    
    # Footer
    st.markdown("""
    <div class="footer">
        <p>Powered With OpenAI | Built by Rohit</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
