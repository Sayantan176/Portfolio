import streamlit as st
import os
import base64

name_col, about_col, contact_col = st.columns([3,1,1], vertical_alignment="center")

with st.container():
  with name_col:
    st.header("Sayantan Roy")
    st.write("CS Student | Developer | Agentic AI User")
  with about_col:
    with open("static/my_resume.pdf", "rb") as file:
      pdf_data = file.read()
    st.download_button(
      label="Save Resume",
      data=pdf_data,
      file_name="My_resume.pdf",
      mime="application/pdf",
      type="primary",
      width="stretch"
    )
  with contact_col:
    st.link_button("Email Me", "https://mail.google.com/mail/?view=cm&fs=1&to=sayantanroy634@gmail.com&su=SUBJECT&body=BODY", type="primary", width="stretch")
st.divider()

pfp_col, desc_col = st.columns([2, 3])


with pfp_col:
  with open("static/profile.jpg", "rb") as f:
    image_data = base64.b64encode(f.read()).decode()

  st.markdown(
      f"""
      <img src="data:image/jpeg;base64,{image_data}"
          style="
              width: 150px;
              height: 150px;
              border-radius: 50%;
              object-fit: cover;
          ">
      """,
      unsafe_allow_html=True
  )

with desc_col:
  st.write("I regularly participate in both online and in-person hackathons and try to develop interesting projects (mainly Python + FastAPI for the backend). So far, I have been #2 and #3 in two GDG organized hackathons. I also practice DSA on NeetCode :)")

  git_col, nc_col, push_left = st.columns([1,1,2.3])

  with git_col:
    st.link_button("GitHub🎉", "https://github.com/Sayantan176", type="tertiary")
  with nc_col:
    st.link_button("NeetCode🚀", "https://neetcode.io/user/CelestialShuriken23", type="tertiary")

st.divider()

st.header("Some of My Projects")

p1, p2, p3 = st.columns([1,1,1], vertical_alignment="center")

with p1:
  st.image(os.path.join(os.getcwd(), "static", "p1.jpg"))
  st.subheader("BharatPower")
  st.write("Smart Energy Platform — monitors state-wise energy prices, analyzes appliance consumption, estimates carbon emissions, and delivers comprehensive energy statistics.")
  st.link_button("Visit", "https://bharatpower.netlify.app/")
with p2:
  st.image(os.path.join(os.getcwd(), "static", "p2.jpg"))
  st.subheader("Wizard")
  st.write("The ultimate AI-powered design-to-code companion. Upload a hand-drawn sketch and watch Wizard transform it into a polished, high-fidelity website using Gemini.")
  st.link_button("Visit", "https://wizard-dtmz.onrender.com/")

with p3:
  st.image(os.path.join(os.getcwd(), "static", "p3.jpg"))
  st.subheader("WorldAmaze")
  st.write("WorldAmaze is an editorial-grade global intelligence platform that helps users monitor geopolitical events, track emerging developments, and explore topics through natural language.")
  st.link_button("Visit", "https://worldamaza.onrender.com/")


st.divider()

st.header("Certificates")

projects = {
    "Programming MOOC 2025, Introduction to Programming - University of Helsinki": "https://certificates.mooc.fi/validate/o9fbco8wnmb",
    "Python for Data Science - NPTEL": "https://nptel.ac.in/noc/E_Certificate/NOC26CS80S36010050903208677",
    "Problem Solving (Basic) - HackerRank": "https://www.hackerrank.com/certificates/93c0ae2305f8"
}

for key, value in projects.items():
  st.markdown(f"- [{key}]({value})")

st.divider()

st.header("Academics")

acads = f"""* B.P. Poddar Institute of Management and Technology (2024-2028)
    * B. Tech (CSE)
    * GPA: 9.02 (Upto 2nd Year)
* Methodist School, Dankuni (2022-2024) 
    * 12th Grade: 93.75% (ISC)
* Methodist School, Dankuni (2009-2022)
    * 10th Grade: 89.5% (ICSE)
"""

st.markdown(acads)

