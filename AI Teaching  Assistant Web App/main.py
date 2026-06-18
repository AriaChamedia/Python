import streamlit as st
from hf import generate_response 

st.title("AI Teaching Assistant")
st.write("Welcome, you can ask me anything about various subjects and I'll provide you an answer.")
user_input=st.text_input("Enter your question here: ")

def complete_answer(user_input):
    base_prompt=f"""Answer clearly in numbered points. 
    If you don't know the answer, say I don't know
    Do not cut sentences, finish each point with a complete sentence.
    Question: {user_input}""" 
    
    response=generate_response(base_prompt)
    return response
    
    
    

if user_input:
    st.write("Your question is: ", user_input)
    response=complete_answer(user_input)
    st.write("AI answer is: ")
    st.markdown(response)
    
    


