import requests
import streamlit as st

# Prepare API key and API url
api_key = "8heyB0Ta0jffXwDQ6SMB2Yt0NaFBxqqjS0HPFSbL"
url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}"

# Get the request data as a dictionary
response1 = requests.get(url)
data = response1.json()

# Extract the image title, url and, explanation
title = data["title"]
date = data["date"]
image_url = data["url"]
explanation = data["explanation"]

# Download the image
image_filepath = "img.png"
response2 = requests.get(image_url)
with open(image_filepath, 'wb') as file:
    file.write(response2.content)

st.title(title)
st.header(date)
st.image(image_filepath)
st.markdown(f"""<p style="text-align: justify;">{explanation}</p>""",
            unsafe_allow_html=True)