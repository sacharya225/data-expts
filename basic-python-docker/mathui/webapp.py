import streamlit as st
import requests
import json

st.title("Zeta - Your Math Buddy")
st.write("Square, Cube , Square root and Log Value of the number")
num=st.number_input("Enter a number", placeholder=2.0, label_visibility="visible")

req={
   "number": num
    }
if st.button('Calculate'):
   response=requests.post(url="http://mathapiserver:8000/math", data=json.dumps(req))
   #for local testing -- response=requests.post(url="http://localhost:8000/math", data=json.dumps(req))
#   st.write(response.json())
   for i in response.json():
      st.write( i + " of the number  " + str(response.json()[i]))
      