from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import streamlit as st

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

st.markdown("<h1 style='text-align: center; color: lightskyblue;'>Net Capsule</h1>", unsafe_allow_html=True)

# date=""
# url=""

if(st.button('Seal')):
    pass
elif(st.button('Retrieve')):
    URL=st.text_input('URL')
    Date=st.date_input('Date')
    if(st.button('Submit')):
        url2 = f"https://web.archive.org/web/{Date}100101/{URL}" 
        page = requests.get(url2)        # pulls the url as a request.
        soup = BeautifulSoup(page.text, "html.parser")      # uses beautiful soup to parse the "url" for only the html.parser
        htmlfile = open("page.html", "w", encoding="utf-8")     # openning the output file // this is not gonna be the final version. Needs to be changed to output 
        stringed_page = str(soup)       # turns the soup object into a string to use for the writing to a file.
        htmlfile.write(stringed_page)       # writes the string to the file. 
        print("Flag hits")
    