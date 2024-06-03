import streamlit as st
import requests

def detect_phishing(url):
    payload = {'url': url}
    response = requests.post('http://127.0.0.1:5000/detect-phishing', json=payload)
    return response.json()

def main():
    st.title("URL Phishing Check")

    url = st.text_input("Enter URL:", "")
    if st.button("Check"):
        if url:
            result = detect_phishing(url)
            
            # st.success(result)
            if result:
                st.error("Unsafe: This URL is identified as a phishing URL.")
            else:
                st.success("Safe: This URL is not identified as a phishing URL.")
        

if __name__ == '__main__':
    main()
