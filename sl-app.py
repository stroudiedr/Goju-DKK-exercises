# Goju streamlit app

import streamlit as st
from PIL import Image
#import time

#st.title("Daigaku Karate Kai")


logo = Image.open("DKKLogo.gif")

st.title("Goju Karate Daily exercises")

st.image(logo,width=350)

link = '[Goju Karate DKK webpage](http://www.goju-karate.co.uk/)'
st.markdown(link, unsafe_allow_html=True)

exercises  = {"A":"12 Push Ups","B":"Gekisai Ichi Kata","C":"12 Sit Ups","D":"120 second plank","E":"Gekisai Ni Kata",
              "F":"Standing sprints (2x60s)","G":"Sepai Kata","H":"12 Squats","I":"12 Push-Ups","J":"Seisan Kata",
              "K":"Saifa Kata","L":"12 Lunge Skips","M":"12 Crocodile Hops","N":"12 Swallow Pushups",
              "O":"12 Burpees","P":"12 Squat Thrusts","Q":"Kururnufa Kata","R":"10 Crunches","S":"Seiunchin Kata",
              "T":"12 Push-Ups","U":"Shisochin Kata","V":"Sanseru Kata","W":"Sanchin Kata","X":"12 Tiger Crawls",
              "Y":"12 Jumping Squats","Z":"10 Burpees","0":"12 Push-Ups","1":"12 Lunge Skips","2":"12 Squats",
              "3":"Feet 4' of (60secs on back)","4":"12 Crunches","5":"12 ankle touches (on back)","6":"12 Reverse Crunches",
              "7":"12 leg raises (on back)","8":"12 crunches","9":"12 burpees"," ":" "
             }

string = st.text_input("Type in your exercise phrase below")

for x in string:
    x = x.upper()
    if x not in exercises.keys():
        st.write(f" {x}: * No exercise * ")
    else:
        st.write(f"{x}: {exercises[x]} ")

