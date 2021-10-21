import streamlit as st
import requests
from PIL import Image

image = Image.open("aqara.png")
st.sidebar.title("Aqara Blockchain")
st.sidebar.image(image,width = 200)
submit = st.sidebar.button("Mining and Creating a Blockchain")


if submit:
    mining = requests.get("http://192.168.219.102:5000/mine_block")
    chain = requests.get("http://192.168.219.102:5000/get_chain")
    temp_mining=mining.text
    temp_chain=chain.text
else:
    temp_mining = ""
    temp_chain = ""
st.title("Aqara Blockchain")
st.text_area("New Block",temp_mining,height=150)
st.text_area("Blockchain",temp_chain,height=300)
