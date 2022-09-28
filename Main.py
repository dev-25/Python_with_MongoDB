import pymongo
import streamlit as st
from pymongo import MongoClient as mc
from datetime import date,datetime 

cluster = mc('mongodb+srv://dev:dev@project1.hbe9j2y.mongodb.net/?retryWrites=true&w=majority')
db = cluster["DB"]
collection = db["Data"]

st.set_page_config (page_title="TO-DO APP", page_icon="📒",layout="wide")
# st.markdown(""" <style>#Sidebsr {visibility: hidden;}footer {visibility: hidden;}</style> """, unsafe_allow_html=True)

st.write('<style>div.block-container{padding-left:2.3rem;padding-top:0.1rem;}</style>', unsafe_allow_html=True)

st.markdown("<h1 style='color:#66fcf1;text-align: center;'>Python with MongoDB !!</h1>",unsafe_allow_html=True)
for i in range(1,3):
	st.write("")

INSERT,padding,ID1,DATE,NOTES,DELETE = st.columns((3,0.7,0.8,1.6,5,1))

with INSERT:
	st.markdown("<h3 style='color:#66fcf1;text-align: center;'>INSERT a Value ✍</h3>",unsafe_allow_html=True)
	st.write('')			   
	txt = st.text_area("Enter a Note")
	st.write('')
	d = st.date_input("Select a Date")
	dd = str(d)
	st.write('')
	post = {"Date":dd, "Note":txt}
	if st.button('→',key = 754789):
		collection.insert_one(post)
		st.experimental_rerun()

with DATE:
	st.markdown("<h3 style='color:#66fcf1;text-align: center;'>Date</h3>",unsafe_allow_html=True)
	st.write('')
	for record in collection.find({},{ "_id": 0,"Date":1 }):
		for v in record.values():              
			def header(v):                 
				st.markdown(f'<p style="border-style: solid;border-color:#66fcf1;background-color:#1f1833;text-align: center;padding:18.2px; color:white; font-size:16px; border-radius:8px;">{v}</p>', unsafe_allow_html=True)
			header(v)

with NOTES:
	st.markdown("<h3 style='color:#66fcf1;text-align: center;'>DATA INPUTED.. 📝</h3>",unsafe_allow_html=True)
	st.write('')

	for record in collection.find({},{ "_id": 0,"Note":1 }):
		for v in record.values():              
			def header(v):                 
				st.markdown(f'<p style="border-style:solid;border-color:#66fcf1;background-color:#1f1833;text-align:left;padding:18.2px; color:white; font-size:16px; border-radius:8px;">{v}</p>', unsafe_allow_html=True)
			header(v)

with ID1:
	st.markdown("<h3 style='color:#66fcf1;text-align: center;'>No</h3>",unsafe_allow_html=True)
	st.write('')
	ass =  collection.count_documents({})
	ID = ass + 1
	for i in range(1,ID):
		st.markdown(f'<p style="border-style: solid;border-color:#66fcf1;background-color:#1f1833;text-align:center; padding:15px; color:white; font-size:20px; border-radius:8px">{i}</p>', unsafe_allow_html=True)

with DELETE:
	for i in range(1,6):
		st.write('')
	for record in collection.find({},{ "_id": 1}):
		for vv in record.values():
			if st.button("🗑",key=vv):
				delete = {"_id": vv}
				collection.delete_one(delete)
				st.experimental_rerun()			
			st.markdown("""<style>.stButton > button {border-style: solid;border-color:#66fcf1;color: white;margin:-2px;background: #1f1833;width: 40px;height: 50px;}</style>""", unsafe_allow_html=True)