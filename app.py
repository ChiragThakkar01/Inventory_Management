import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Page configuration
st.set_page_config(
    page_title="All in One Retail Management",
    page_icon="📦",
    layout="wide"
)

# Load Lottie animations
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

retail_lottie = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_9cyyl8i4.json")

# --- Custom CSS ---
st.markdown("""
    <style>
        /* Hide default Streamlit sidebar */
        [data-testid="stSidebar"] {
            display: none;
        }
        .stApp {
            background: linear-gradient(to right, #141e30, #243b55);
            color: white;
        }
        h1, h2, h3, .stMarkdown p {
            color: #f0f0f0;
        }
        .top-nav {
            display: flex;
            justify-content: center;
            background-color: #1f2937;
            padding: 12px;
            border-radius: 10px;
            margin-bottom: 30px;
        }
        .nav-link {
            margin: 0 20px;
            padding: 10px 20px;
            color: white;
            text-decoration: none;
            background-color: #374151;
            border-radius: 8px;
        }
        .nav-link:hover {
            background-color: #3b82f6;
        }
        img {
            border-radius: 12px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Top Navigation Icons ---
st.markdown("""
    <div class="top-nav">
        <a class="nav-link" href="#" onclick="window.location.href='/app'">🏠 Home</a>
        <a class="nav-link" href="#" onclick="window.location.href='/upload_data'">📤 Upload</a>
        <a class="nav-link" href="#" onclick="window.location.href='/inventory'">📦 Inventory</a>
        <a class="nav-link" href="#" onclick="window.location.href='/purchases'">🛒 Purchases</a>
        <a class="nav-link" href="#" onclick="window.location.href='/sales'">📈 Sales</a>
    </div>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("<h1 style='text-align:center;'>📦 All in One Retail Management</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:18px;'>Empowering retailers with real-time insights.</p>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# --- Layout ---
left_col, right_col = st.columns([1.2, 1])
with left_col:
    st.subheader("🔧 Features:")
    st.markdown("""
    - 📋 **Inventory**: Track stock levels, product variations, and categories.
    - 📈 **Sales**: View product performance, trends, and orders.
    - 📥 **Purchases**: Manage vendor performance and payment schedules.
    """)
    
    st.subheader("🚀 Get Started:")
    st.markdown("""
    1. Go to the **Upload or Add Data** page.
    2. Use the **top navigation bar** to switch between views.
    3. Monitor trends, alerts, and inventory health — all in one place!
    """)
    
    st.subheader("⚙️ Built With:")
    st.markdown("-  Python + Streamlit\n- 🛢️ MySQL\n- 📊 Realtime Dashboards")

with right_col:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Inventory_management_dashboard.jpg/800px-Inventory_management_dashboard.jpg",
        caption="Retail Inventory Dashboard",
        use_container_width=True
    )
    st_lottie(retail_lottie, height=250, key="retail_anim")

# --- Footer ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align:center;'>
    🔒 Secure | ⚡ Fast | 🎯 Accurate<br>
    <span style='font-size:12px;'>Built by Sakshi Saraiya & Chirag Thakkar</span>
</div>
""", unsafe_allow_html=True)
