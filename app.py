import streamlit as st
from streamlit_lottie import st_lottie
import requests
import os

# Set page configuration
st.set_page_config(
    page_title="All-in-One Retail Management",
    page_icon="🛒",
    layout="wide"
)

# --- Load Lottie Animations ---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load animations
inventory_lottie = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_jcikwtux.json")
retail_lottie = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_9cyyl8i4.json")

# --- Title ---
st.markdown("<h1 style='text-align:center;'>🛒 Retail Inventory Management System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:18px;'>Empowering retailers with real-time control over stock, sales, and purchases.</p>", unsafe_allow_html=True)
st.markdown("---")

# --- Layout: Left & Right Content Sections ---
left_col, right_col = st.columns([1.3, 1])

with left_col:
    st.subheader("🔧 Key Features:")
    st.markdown("""
    - 📦 **Inventory Management**: Stay updated with stock levels, product types, and categories.
    - 📈 **Sales Insights**: Monitor performance, revenue trends, and popular products.
    - 📥 **Purchase Tracking**: Keep tabs on vendor orders and payment statuses.
    """)

    st.subheader("🚀 How to Get Started:")
    st.markdown("""
    1. Navigate to the **Upload or Add Data** page.
    2. Use the **Sidebar** to switch between views.
    3. Visualize sales, purchases, and stock data — all in one dashboard.
    """)

    st.subheader("⚙️ Built Using:")
    st.markdown("""
    - 🐍 Python with Streamlit  
    - 🗄️ MySQL Database  
    - 📊 Real-time Interactive Dashboards  
    """)

    st.subheader("🧭 Quick Navigation:")
    nav1, nav2 = st.columns(2)
    with nav1:
        if st.button("📤 Upload Data"):
            st.switch_page("pages/0_upload_data.py")
    with nav2:
        if st.button("📦 View Inventory"):
            st.switch_page("pages/1_Home.py")

with right_col:
    st_lottie(retail_lottie, height=250, key="retail_anim")
    st_lottie(inventory_lottie, height=250, key="inventory_anim")

# --- Visuals Section ---
st.markdown("---")
st.subheader("📸 Retail Management Visuals")

img_col1, img_col2 = st.columns(2)

with img_col1:
    st.image(
        "mnt/data/aa119cfb-a14a-4a1e-9d22-9cae5a089bc3.png",
        caption="Inventory Management – Real-time Stock Overview",
        use_container_width=True
    )

with img_col2:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Sales_analytics_dashboard.png/800px-Sales_analytics_dashboard.png",
        caption="Sales & Profit Dashboard – Business Insights",
        use_container_width=True
    )

# --- Footer ---
st.markdown("---")
st.markdown("<div style='text-align:center;'>🔐 Secure | ⚡ Fast | 📊 Smart Dashboards</div>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center; font-size:12px;'>© 2025 Built by Sakshi Saraiya & Chirag Thakkar</div>", unsafe_allow_html=True)
