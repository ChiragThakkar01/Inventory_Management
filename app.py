import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Page configuration
st.set_page_config(
    page_title="All in One Retail Management",
    page_icon="📦",
    layout="wide"
)

# Load Lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

retail_lottie = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_9cyyl8i4.json")

# --- Custom Styling ---
st.markdown("""
    <style>
        [data-testid="stSidebar"] {display: none;}
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
            gap: 1.5rem;
        }
        .nav-btn {
            font-size: 18px;
            padding: 10px 20px;
            background-color: #374151;
            border: none;
            border-radius: 8px;
            color: white;
        }
        .nav-btn:hover {
            background-color: #3b82f6;
            cursor: pointer;
        }
        img {
            border-radius: 12px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Navigation Buttons (Actual Streamlit Buttons calling switch_page) ---
st.markdown("<div class='top-nav'>", unsafe_allow_html=True)
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("🏠 Home"):
        st.switch_page("app.py")
with col2:
    if st.button("📤 Upload"):
        st.switch_page("pages/0_upload_data.py")
with col3:
    if st.button("📦 Inventory"):
        st.switch_page("pages/2_inventory.py")
with col4:
    if st.button("🛒 Purchases"):
        st.switch_page("pages/3_purchases.py")
with col5:
    if st.button("📈 Sales"):
        st.switch_page("pages/4_sales.py")
st.markdown("</div>", unsafe_allow_html=True)

# --- Title & Description ---
st.markdown("<h1 style='text-align:center;'>📦 All in One Retail Management</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:18px;'>Empowering retailers with real-time insights.</p>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# --- Main Section Layout ---
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
    st.markdown("- Python + Streamlit\n- 🛢️ MySQL\n- 📊 Real-time Dashboards")

with right_col:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Inventory_management_dashboard.jpg/800px-Inventory_management_dashboard.jpg",
        caption="📊 Inventory Management Dashboard",
        use_container_width=True
    )

# --- Retail Animation ---
st_lottie(retail_lottie, height=250, key="retail_anim")

# --- Additional Visuals ---
st.markdown("### 📸 Retail Management in Action")
img_col1, img_col2 = st.columns(2)
with img_col1:
    st.image("https://cdn.pixabay.com/photo/2016/10/27/22/52/barcode-1777816_1280.jpg",
             caption="Barcode Scanning & Stocking", use_container_width=True)
with img_col2:
    st.image("https://cdn.pixabay.com/photo/2016/03/27/07/08/warehouse-1287184_1280.jpg",
             caption="Retail Shelf Management", use_container_width=True)

# --- Footer ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align:center;'>
    🔒 Secure | ⚡ Fast | 🎯 Accurate<br>
    <span style='font-size:12px;'>Built by Sakshi Saraiya & Chirag Thakkar</span>
</div>
""", unsafe_allow_html=True)
