# Đây là file để viết giao diện ứng dụng và xử lý cách tính toán tương tác với người dùng
import streamlit as st
from factorial import fact  # Từ file (cùng cấp) import hàm vào để sử dụng

def main():
    st.title("Factorial Calculator")
    number = st.number_input("Enter a number: ", min_value=0, max_value=900)
    
    if st.button("Calculate"):
        result = fact(number)
        st.write(f"The factorial of {number} is {result}")


if __name__ == "__main__":
    main()