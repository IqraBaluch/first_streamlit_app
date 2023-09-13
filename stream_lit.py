import streamlit

streamlit.title("Healthy Food")
streamlit.header("Menu For Breackfast")
streamlit.text('1. Orange juice, brown bread and doodh patti')
streamlit.text('2. apple slices, boiled egg and doodh patti')
streamlit.text('3. milk shake, half fried egg and doodh patti')

streamlit.header(" 🥑🍞Some other items")
 
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas

fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.dataframe(fruit_list)

