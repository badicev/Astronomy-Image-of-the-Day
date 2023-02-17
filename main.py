import requests
from key import api_key
import streamlit as st

url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

request = requests.get(url)
data = request.json()


title = data["title"]
image_url = data["url"]
desc = data["explanation"]

#download the image
image_filepath =  "img.png"
response_img = requests.get(image_url)
with open(image_filepath, 'wb') as file:
    file.write(response_img.content)

st.title(title)
st.image(image_filepath)
st.write(desc)