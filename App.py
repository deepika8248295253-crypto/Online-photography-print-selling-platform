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
if st.session_state.user is None:
    login_tab, register_tab = st.tabs(
        ["Login", "Register"]
    )
    with login_tab:
    st.header("User Login")
    username = st.text_input("Username")
    password = st.text_input(
        "Password",
        type="password"
    )
    if st.button("Login"):
        user = login(
            username,
            password
        )
        if user:
            st.session_state.user = {
                "username": user[0],
                "role": user[1]
            }
            st.success(
                "Login successful!"
            )
            st.rerun()
        else:
            st.error(
                "Invalid username or password"
            )
    st.info(
        "Admin: admin / admin123"
    )
    with register_tab:

    st.header("Create Account")

    username = st.text_input(
        "New Username"
    )

    password = st.text_input(
        "New Password",
        type="password"
    )
    confirm = st.text_input(
        "Confirm Password",
        type="password"
    )
    if st.button("Register"):
        if password != confirm:
            st.error(
                "Passwords do not match"
            )
        else:
            success, message = register(
                username,
                password
            )
            if success:
                st.success(message)
            else:
                st.error(message)
st.stop()
user = st.session_state.user
st.sidebar.success(
    f"Welcome {user['username']}"
)
st.sidebar.write(
    f"Role: {user['role']}"
)
pages = [
    "Home",
    "Photography Prints",
    "Cart",
    "My Orders"
]
if user["role"] == "admin":
 pages.append("Admin Panel")
page = st.sidebar.radio(
    "Menu",
    pages
)
if st.sidebar.button("Logout"):
    st.session_state.user = None
    st.session_state.cart = []
    st.rerun()
if page == "Home":
    st.header(
        "Welcome to Photography Print Store 📷"
    )
    st.write(
        "Buy beautiful photography prints "
        "for your home, office and gifts."
    )
    products = get_products()
    orders = get_orders(
        user["username"]
    )
    col1, col2, col3 = st.columns(3)
    col1.metric(
        "Products",
        len(products)
    )
    col2.metric(
        "Cart Items",
        len(st.session_state.cart)
    )
    col3.metric(
        "My Orders",
        len(orders)
    )
