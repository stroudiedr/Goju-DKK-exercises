# Goju streamlit app

import streamlit as st
from PIL import Image
#import time

#st.title("Daigaku Karate Kai")


logo = Image.open("DKKLogo.gif")

st.image(logo,width=600)

st.header("Daily exercises")

exercises  = {"A":"10 Push Ups","B":"Gekisai Ichi Kata","C":"10 Sit Ups","D":"120 second plank","E":"Gekisai Ni Kata",
              "F":"Standing sprints (2x60s)","G":"Sepai Kata","H":"10 Squats","I":"10 Push-Ups","J":"Seisan Kata",
              "K":"Saifa Kata","L":"10 Lunge Skips","M":"10 Crocodile Hops","N":"10 Swallow Pushups",
              "O":"10 Burpees","P":"10 Squat Thrusts","Q":"Kururnufa Kata","R":"10 Crunches","S":"Seiunchin Kata",
              "T":"10 Push-Ups","U":"Shisochin Kata","V":"Sanseru Kata","W":"Sanchin Kata","X":"10 Tiger Crawls",
              "Y":"10 Jumping Squats","Z":"10 Burpees","0":"10 Push-Ups","1":"10 Lunge Skips","2":"10 Squats",
              "3":"Feet 4' of (60secs on back)","4":"10 Crunches","5":"10 ankle touches (on back)","6":"10 Reverse Crunches",
              "7":"10 leg raises (on back)","8":"10 crunches","9":"10 burpees"," ":" "
             }

#Grades = ["Please select", "White","Red","Yellow","Orange","Green","Blue","Purple","Brown","Shodan Ho","Shodan","Nidan","Sandan"]

#GradeSelect = st.sidebar.selectbox("Please select your grade",Grades)

## Timer for the exercise

#if st.sidebar.button("Start Timer"):
	#st.sidebar.text("Timer has started")
	#start_time = time.time()

#if st.sidebar.button("Stop Timer"):
	#st.sidebar.text("Time has stopped")
	#stop_time = time.time()

#duration = stop_time - start_time
#st.markdown(start_time)
#st.markdown(stop_time)
#st.write("Your stop time was {stop_time}")

string = st.sidebar.text_input("Type in your exercise phrase below")

for x in string:
    x = x.upper()
    if x not in exercises.keys():
        st.write(f" {x}: * No exercise * ")
    else:
        st.write(f"{x}: {exercises[x]} ")



