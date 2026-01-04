import streamlit as st
from calci import add,subtract,multiply,divide,power
st.title("Simple Calculator App")
st.write("Perform basic arithmetic operations.")

num1 = st.number_input("Enter first number", value=0)
num2 = st.number_input("Enter second number", value=0)
opearation = st.selectbox("Select operation",["Add","Subtract","Multiply","Divide","Power"])

if st.button("Calculate"):
    if opearation == "Add":
        res = add(num1,num2)
        st.success(f"Result: {res}")
    elif opearation == "Subtract":
        res = subtract(num1,num2)
        st.success(f"Result: {res}")
    elif opearation == "Multiply":
        res = multiply(num1,num2)
        st.success(f"Result: {res}")
    elif opearation == "Divide":
        res = divide(num1,num2)
        st.success(f"Result: {res}")
    elif opearation == "Power":
        res = power(num1,num2)
        st.success(f"Result: {res}")
    else:
        st.error("Invalid Operation Selected")