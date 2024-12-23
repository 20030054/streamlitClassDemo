import streamlit as st

def main():
    st.title("Simple Calculator App")

    # Input fields for numbers
    st.header("Enter Your Numbers")
    num1 = st.number_input("Enter the first number", value=0.0, step=1.0)
    num2 = st.number_input("Enter the second number", value=0.0, step=1.0)

    # Dropdown for selecting operation
    operation = st.selectbox("Choose an operation", ("Add", "Subtract", "Multiply", "Divide"))

    # Perform calculation based on the selected operation
    result = None
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"

    # Display result
    if st.button("Calculate"):
        st.subheader("Result")
        st.write(result)

if __name__ == "__main__":
    main()
