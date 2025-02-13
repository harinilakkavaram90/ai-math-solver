import streamlit as st
from sympy import symbols, Eq, solve, diff, integrate

# Define symbols
x, y = symbols('x y')

# --- Streamlit Page Config ---
st.set_page_config(page_title="AI Math Solver", page_icon="✨", layout="wide")

# --- Custom Baby Pink Styling ---
st.markdown("""
    <style>
        body {
            background-color: #FFD1DC;
        }
        .stApp {
            background-color: #FFD1DC;
        }
        .stTextInput, .stButton, .stSelectbox {
            font-size: 18px !important;
        }
        .stButton button {
            background-color: #FF69B4 !important;
            color: white !important;
            font-weight: bold !important;
            border-radius: 10px !important;
        }
        .stTitle {
            color: #FF1493;
        }
        .stMarkdown {
            color: #D147A3;
            font-size: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/1048/1048952.png", width=100)
st.sidebar.title("💋 AI Math Solver")
option = st.sidebar.radio("Choose an option:", 
    ["📖 Solve an Equation", "✏️ Find a Derivative", "∫ Find an Integral", "🔗 Solve a System"])

st.sidebar.write("---")
st.sidebar.write("💡 **Tip:** Use `*` for multiplication and `**` for powers!")

# --- Solve Equation ---
if option == "📖 Solve an Equation":
    st.subheader("📖 Solve an Algebraic Equation")
    equation = st.text_input("Enter an equation (e.g., 2*x + 3 = 7):")
    if st.button("🧠 Solve"):
        if equation:
            try:
                eq = Eq(eval(equation.split('=')[0]), eval(equation.split('=')[1]))
                solution = solve(eq, x)
                st.success(f"✅ Solution: {solution}")
            except:
                st.error("❌ Invalid equation format!")

# --- Find Derivative ---
elif option == "✏️ Find a Derivative":
    st.subheader("✏️ Find the Derivative of a Function")
    expr = st.text_input("Enter a function (e.g., x**2 + 3*x):")
    if st.button("📉 Calculate Derivative"):
        if expr:
            try:
                derivative = diff(eval(expr), x)
                st.success(f"✅ Derivative: {derivative}")
            except:
                st.error("❌ Invalid function format!")

# --- Find Integral ---
elif option == "∫ Find an Integral":
    st.subheader("∫ Find the Integral of a Function")
    expr = st.text_input("Enter a function (e.g., x**2):")
    if st.button("📈 Calculate Integral"):
        if expr:
            try:
                integral = integrate(eval(expr), x)
                st.success(f"✅ Integral: {integral}")
            except:
                st.error("❌ Invalid function format!")

# --- Solve System of Equations ---
elif option == "🔗 Solve a System":
    st.subheader("🔗 Solve a System of Equations")
    eq1 = st.text_input("Enter first equation (e.g., 2*x + 3*y = 7):")
    eq2 = st.text_input("Enter second equation (e.g., 4*x - y = 5):")
    if st.button("🔍 Solve System"):
        if eq1 and eq2:
            try:
                equation1 = Eq(eval(eq1.split('=')[0]), eval(eq1.split('=')[1]))
                equation2 = Eq(eval(eq2.split('=')[0]), eval(eq2.split('=')[1]))
                solution = solve((equation1, equation2), (x, y))
                st.success(f"✅ Solution: {solution}")
            except:
                st.error("❌ Invalid equation format!")
