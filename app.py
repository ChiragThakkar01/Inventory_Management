import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Set page config
st.set_page_config(
    page_title="Retail Inventory Management",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Load Lottie Animations ---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

inventory_lottie = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_jcikwtux.json")
retail_lottie = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_9cyyl8i4.json")
sales_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_p9pzimvd.json")
purchase_lottie = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_tutvdkg0.json")

# --- Top Navigation Bar with Icons ---
st.markdown("""
    <style>
    .nav-container {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin-bottom: 20px;
    }
    .nav-item {
        font-size: 18px;
        padding: 10px 20px;
        background-color: #262730;
        border-radius: 8px;
        color: white;
        text-decoration: none;
    }
    .nav-item:hover {
        background-color: #4F8BF9;
    }
    </style>
    <div class="nav-container">
        <a class="nav-item" href="#">🏠 Home</a>
        <a class="nav-item" href="#">📤 Upload Data</a>
        <a class="nav-item" href="#">📦 Inventory</a>
        <a class="nav-item" href="#">📥 Purchases</a>
        <a class="nav-item" href="#">📈 Sales</a>
    </div>
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
    1. Select a tab from the navigation bar above.
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
    st_lottie(retail_lottie, height=180, key="retail_anim")
    st_lottie(inventory_lottie, height=180, key="inventory_anim")
    st_lottie(sales_lottie, height=180, key="sales_anim")
    st_lottie(purchase_lottie, height=180, key="purchase_anim")

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

img_col3, img_col4 = st.columns(2)

with img_col3:
    st.image(
        "https://www.zoho.com/inventory/images/home/hero-dashboard.png",
        caption="Zoho Inventory Dashboard",
        use_container_width=True
    )

with img_col4:
    st.image(
        "https://d3fy6515xcp0h2.cloudfront.net/article_images/2023/10/inventory-forecasting-header-1000x563.jpg",
        caption="Inventory Forecasting – Retail Intelligence",
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
