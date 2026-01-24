# TROUBLESHOOTING: 
# If 'streamlit' is not recognized, run using: 
# python -m streamlit run portfolio_app.py

import streamlit as st
from streamlit_option_menu import option_menu
import base64
import os

# Page Configuration
st.set_page_config(page_title="Brian Mabunda | AI Engineer", page_icon="🤖", layout="wide")

# Helper function to allow local images in HTML/CSS
def get_base64_of_bin_file(bin_file):
    if not os.path.exists(bin_file):
        # Fallback to a placeholder if file is missing
        return "https://via.placeholder.com/150"
    with open(bin_file, 'rb') as f:
        data = f.read()
    return f"data:image/png;base64,{base64.b64encode(data).decode()}"

# Pre-load local images (Update these filenames to match your local folder exactly)
profile_pic_base64 = get_base64_of_bin_file("MyproffesionalPhoto.JPG")
fixit_img_base64 = get_base64_of_bin_file("FIxIT.png")
asl_img_base64 = get_base64_of_bin_file("singerSpellerUI.png")

# Futuristic Glassmorphism and Background Animation CSS
st.markdown("""
    <style>
    /* Animated Background */
    @keyframes move {
        100% {
            transform: translate3d(0, 0, 1px) rotate(360deg);
        }
    }

    .background {
        position: fixed;
        width: 100vw;
        height: 100vh;
        top: 0;
        left: 0;
        background: #06080d;
        overflow: hidden;
        z-index: -1;
    }

    .background span {
        width: 20vmin;
        height: 20vmin;
        border-radius: 20vmin;
        backface-visibility: hidden;
        position: absolute;
        animation: move;
        animation-duration: 45s;
        animation-timing-function: linear;
        animation-iteration-count: infinite;
    }

    .background span:nth-child(1) { color: #00d4ff; top: 14%; left: 81%; animation-duration: 15s; background-color: currentColor; opacity: 0.1; }
    .background span:nth-child(2) { color: #583cff; top: 50%; left: 10%; animation-duration: 20s; background-color: currentColor; opacity: 0.1; }
    .background span:nth-child(3) { color: #00d4ff; top: 80%; left: 60%; animation-duration: 25s; background-color: currentColor; opacity: 0.1; }

    /* Glassmorphism Effect */
    .stApp {
        background: transparent;
    }
    
    [data-testid="stHeader"] {
        background: rgba(14, 17, 23, 0.7) !important;
        backdrop-filter: blur(10px);
    }

    .project-card {
        border-radius: 15px;
        padding: 20px;
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(12px);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        margin-bottom: 25px;
        transition: transform 0.3s ease;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
        border: 1px solid rgba(0, 212, 255, 0.5);
    }

    /* Sidebar Fix - Force dark glass */
    [data-testid="stSidebar"] {
        background-color: rgba(10, 12, 18, 0.9) !important;
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(255, 255, 255, 0.05);
        overflow: hidden !important;
    }
    
    [data-testid="stSidebarUserContent"] {
        background-color: transparent !important;
        padding-top: 2rem !important;
        overflow: hidden !important;
    }

    /* Rounded Profile Picture Styling - Updated to fill circle */
    .profile-pic-container {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    /* Targets the iframe component itself */
    iframe[title="streamlit_option_menu.option_menu"] {
        background-color: transparent !important;
        border-radius: 15px;
    }

    /* Targets the Streamlit container around the menu */
    [data-testid="stVerticalBlock"] > div:has(iframe[title="streamlit_option_menu.option_menu"]) {
        background-color: transparent !important;
    }

    /* Ensure the sidebar doesn't add padding that creates light gaps */
    [data-testid="stSidebarUserContent"] {
        padding-top: 1.5rem !important;
    }
    
    .profile-pic {
        width: 150px; 
        height: 150px;
        border-radius: 50%; 
        object-fit: cover; /* Ensures image fills the dimensions without distortion */
        object-position: center; /* Centers the image content */
        border: 3px solid #00d4ff;
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.4);
    }

    h1, h2, h3 {
        color: #00d4ff !important;
        text-shadow: 0px 0px 10px rgba(0, 212, 255, 0.3);
    }

    p, span, label {
        color: #e0e0e0 !important;
    }

    /* Project Image Styling */
    .project-img {
        width: 100%;
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        object-fit: cover;
    }

    /* Targeting both regular buttons and link buttons (Projects) */
    .stButton>button, .stLinkButton>a {
        background-color: transparent !important;
        border: 2px solid #00d4ff !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 0.5rem 1rem !important;
        transition: all 0.3s ease !important;
        text-decoration: none !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        font-weight: 500 !important;
    }

    /* Hover effect to make it glow slightly */
    .stButton>button:hover, .stLinkButton>a:hover {
        background-color: rgba(0, 212, 255, 0.1) !important;
        box-shadow: 0 0 15px rgba(0, 212, 255, 0.4) !important;
        color: #00d4ff !important;
        border: 2px solid #00d4ff !important;
    }
            
    .st.sidebar{
            background-color: rgba(10, 12, 18, 0.9) !important;
            }

    
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    
    <div class="background">
       <span></span>
       <span></span>
       <span></span>
    </div>
    """, unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.markdown(f"""
        <div class="profile-pic-container">
            <img src="{profile_pic_base64}" class="profile-pic">
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align: center; margin-top: -10px;'>Brian Mabunda</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #00d4ff !important; font-weight: bold;'>AI Engineer</p>", unsafe_allow_html=True)
    
    st.write("---")
    
    
    selected = option_menu(
        menu_title=None,
        options=["About Me", "Projects", "Live AI Demos", "Contact"],
        icons=["person", "code-slash", "cpu", "envelope"],
        default_index=0,
        styles={
            "container": {
                # "padding": "15px !important",
                "background-color": "#0a0c12", # Matches your project-card
                "border": "1px solid white", # Subtle glass border
                "backdrop-filter": "blur(12px)", # Frosted effect
                "border-radius": "15px",
                "box-shadow": "1 8px 32px 0 rgba(0, 0, 0, 0.37)",
            },
            "icon": {"color": "#00d4ff", "font-size": "18px"}, 
            "nav-link": {
                "font-size": "15px", 
                "color": "white", 
                "text-align": "left", 
                "margin": "5px", 
                "padding": "10px",
                "transition": "0.3s",
                "--hover-color": "rgba(0, 212, 255, 0.1)" # Prevents default grey hover
            },
            "nav-link-selected": {
                "background-color": "rgba(0, 212, 255, 0.2)", 
                "color": "#00d4ff", 
                "border": "1px solid rgba(0, 212, 255, 0.5)",
                "font-weight": "bold"
            },
        }
    )

# --- ABOUT ME SECTION ---
if selected == "About Me":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("<h1>Hi, I'm Brian Mabunda 👋</h1>", unsafe_allow_html=True)
        st.subheader("AI Engineer | Full-Stack Developer | Computer Systems Engineer")
        st.markdown("""
        <div class="project-card">
        Results-driven AI Engineer with a strong foundation in Computer Systems Engineering. 
        I specialize in bridging the gap between R&D prototypes and scalable, containerized applications.
        Based on my experience, I excel at building production-grade AI solutions, from RAG-based 
        LLM architectures to high-accxuracy object detection systems.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🛠️ Core Expertise")
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("<p style='color:#00d4ff !important;'><b>AI/ML</b></p>", unsafe_allow_html=True)
            st.write("RAG, Agentic Workflows, YOLO v5/v6, MediaPipe, DeepSort, PySpark")
        with col_b:
            st.markdown("<p style='color:#00d4ff !important;'><b>Infrastructure</b></p>", unsafe_allow_html=True)
            st.write("Docker, FastAPI, Vercel, Azure, CI/CD, Apache Airflow")

    with col2:
        # Top Right Tile: Certifications
        st.markdown("""
        <div class="project-card">
        <p style='color:#00d4ff !important'><b>Certifications</b></p>
        <span style='font-size: 0.9rem;'>- IBM Data Scientist Prof.</span><br>
        <span style='font-size: 0.9rem;'>- ND: Computer Systems Eng (TUT)</span><br><br>
        <p style='color:#00d4ff !important'><b>Location</b></p>
        📍 Pretoria, South Africa
        </div>
        """, unsafe_allow_html=True)

        # Bottom Right Tile: Socials
        st.markdown("""
        <div class="project-card">
        <p style='color:#00d4ff !important'><b>Connect With Me</b></p>
        <p style='font-size: 0.9rem; margin-bottom: 8px;'>
            📧 <a href="mailto:brianmabunda00@gmail.com" style="color: #e0e0e0; text-decoration: none;">brianmabunda00@gmail.com</a>
        </p>
        <p style='font-size: 0.9rem; margin-bottom: 8px;'>
            🔗 <a href="https://linkedin.com/in/brianmabunda" style="color: #e0e0e0; text-decoration: none;">linkedin.com/in/brianmabunda</a>
        </p>
        <p style='font-size: 0.9rem;'>
            🐙 <a href="https://github.com/BrianMabunda" style="color: #e0e0e0; text-decoration: none;">github.com/BrianMabunda</a>
        </p>
        </div>
        """, unsafe_allow_html=True)

# --- PROJECTS SECTION ---
elif selected == "Projects":
    st.title("📂 Featured Projects")
    
    projects = [
        {
            "title": "FixIT.core - RAG Diagnostic Tool",
            "desc": "Engineered a custom RAG agent that parses technical manuals to provide context-aware solutions with a state-driven React frontend.",
            "tech": "Agentic UI, RAG Agent, Vector Search, FastAPI, Vercel",
            "link": "https://fix-it-core.vercel.app/",
            "img": fixit_img_base64
        },
        {
            "title": "ASL Speller: Sign Recognition",
            "desc": "Shifted heavy image processing to the client-side using MediaPipe, reducing server latency by 40%.",
            "tech": "MediaPipe, Scikit-learn, Docker, FastAPI, React",
            "link": "https://sign-language-speller-ui.vercel.app/",
            "img": asl_img_base64
        }
    ]
    

    for proj in projects:
        with st.container():
            st.markdown("""
            <style>
                /* Style for ALL link buttons with specific keys */
                iframe[title="streamlit_option_menu.option_menu"] {
                                background-color: transparent !important;
                            }
            </style>
            """, unsafe_allow_html=True)
            st.markdown( f"""
                        <div class="project-card">
                            <div style="display: flex; flex-wrap: wrap; gap: 20px;">
                                <div style="flex: 1; min-width: 300px;">
                                    <img src="{proj['img']}" class="project-img">
                                </div>
                                <div style="flex: 1.5; min-width: 300px;">
                                    <h3>{proj['title']}</h3>
                                    <p>{proj['desc']}</p>
                                    <p><b>Tech:</b> {proj['tech']}</p>git
                                </div>
                            </div>
                        </div>
            """, unsafe_allow_html=True)
            st.link_button(f"Launch {proj['title'].split('-')[0]}", proj['link'])
            st.write("") 

# --- LIVE AI DEMOS SECTION ---
elif selected == "Live AI Demos":
    st.title("🚀 Live Inference Demos")
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    demo_choice = st.selectbox("Choose a Demo", ["Sentiment Analyzer (NLP)", "Object Counter (Mock)"])
    if demo_choice == "Sentiment Analyzer (NLP)":
        user_input = st.text_area("Enter some feedback about a product:")
        if st.button("Analyze"):
            st.success("Analysis Complete: Positive (98%)")
            st.balloons()
    elif demo_choice == "Object Counter (Mock)":
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])
        if uploaded_file:
            st.image(uploaded_file, caption="Uploaded Image")
            with st.spinner("Running YOLOv8 inference..."):
                import time
                time.sleep(1.5)
                st.write("✅ Detected: 3 Persons, 1 Laptop")
    st.markdown('</div>', unsafe_allow_html=True)

# --- CONTACT SECTION ---
elif selected == "Contact":
    st.title("📩 Get In Touch")
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit = st.form_submit_button("Send Message")
        if submit:
            st.success(f"Thanks {name}, I'll get back to you soon!")
    st.markdown('</div>', unsafe_allow_html=True)