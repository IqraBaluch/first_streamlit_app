import requests
import streamlit
import pandas
import snowflake.connector
from urllib.error import URLError




streamlit.title('Snowflake Application')

streamlit.header('🥣Breakfast Menu🍞')
streamlit.text('🥗Omega 3 & Blueberry Oatmeal')
streamlit.text('  🐔Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑Hard-Boiled Free-Range Egg')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#accesing fruits names from a txt file
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
## add a user interactive widget called a Multi-select that will allow users to pick the fruits they want in their smoothies.
# Let's put a pick list here so they can pick the fruit they want to include 
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from FRUIT_LOAD_LIST")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)





#new section to display
streamlit.header("Fruityvice Fruit Advice!")

try:
    fruit = streamlit.text_input('What fruit you would like to know about')
    if not fruit:
        streamlit.error('Please select the fruit from drop down you would like to know about')
    else:
        responce_back = my_fun(fruit)
        streamlit.dataframe(responce_back)
except URLError as e:
    streamlit.error()
streamlit.stop() #do not run anything past here.












