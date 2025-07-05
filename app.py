import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Set page config
st.set_page_config(
    page_title="Retail Inventory Management",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="collapsed"  # Collapse sidebar since we're moving navigation to top
)

# --- Load Lottie Animations ---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

inventory_lottie = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_jcikwtux.json")
retail_lottie = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_9cyyl8i4.json")

# --- Top Navigation Bar ---
menu_items = ["🏠 Home", "📤 Upload Data", "📦 Inventory", "📥 Purchases", "📈 Sales"]
selected_tab = st.selectbox("Navigate", menu_items, index=0, key="top_nav")

st.markdown("""
    <style>
    .block-container {
        padding-top: 1rem;
    }
    div[data-baseweb="select"] > div {
        font-size: 18px;
        padding: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title Section ---
st.markdown("""
    <h1 style='text-align: center;'>🛒 Retail Inventory Management System</h1>
    <p style='text-align: center; font-size: 18px;'>Empowering retailers with real-time control over stock, sales, and purchases.</p>
    <hr style='margin-top: 0px;'>
""", unsafe_allow_html=True)

# --- Content Section ---
left, right = st.columns([1.3, 1])

with left:
    st.subheader("🔧 Key Features:")
    st.markdown("""
    - 📦 **Inventory Management**: Track stock levels, product types, and categories.
    - 📈 **Sales Insights**: Monitor performance, revenue trends, and top-selling products.
    - 📥 **Purchase Tracking**: Stay updated on vendor orders and payment statuses.
    """)

    st.subheader("🚀 How to Get Started:")
    st.markdown("""
    1. Select a tab from the navigation dropdown above.
    2. Upload or view data as needed.
    3. Analyze trends, optimize stock, and improve profits!
    """)

    st.subheader("⚙️ Built Using:")
    st.markdown("""
    - 🐍 Python with Streamlit
    - 🗄️ MySQL Database
    - 📊 Realtime Interactive Dashboards
    """)

with right:
    st_lottie(retail_lottie, height=220, key="retail_anim")
    st_lottie(inventory_lottie, height=220, key="inventory_anim")

# --- Retail Visuals ---
st.subheader("📸 Retail Management Visuals")
img_col1, img_col2 = st.columns(2)

with img_col1:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Inventory_management_dashboard.jpg/800px-Inventory_management_dashboard.jpg",
        caption="Inventory Management – Stock Overview",
        use_container_width=True
    )

with img_col2:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Sales_analytics_dashboard.png/800px-Sales_analytics_dashboard.png",
        caption="Sales & Profit Dashboard",
        use_container_width=True
    )

# --- Footer ---
st.markdown("""
---
<div style='text-align:center;'>
    🔐 Secure | ⚡ Fast | 📊 Smart Dashboards<br>
    <small>© 2025 Built by Sakshi Saraiya & Chirag Thakkar</small>
</div>
""", unsafe_allow_html=True)
