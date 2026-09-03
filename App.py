import streamlit as st
from database import init_db
from auth import register, login
from products import get_products, add_product, delete_product
from orders import place_order, get_orders, update_status
st.set_page_config(
    page_title="Photography Print Store",
    page_icon="📷",
    layout="wide"
)
init_db()
if "user" not in st.session_state:
    st.session_state.user = None
if "cart" not in st.session_state:
    st.session_state.cart = []
    st.title(
    "📷 Online Photography Print Selling Platform"
)
st.caption(
    "Python-only Photography Store"
)
