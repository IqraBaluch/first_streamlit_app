"""
@Author : Saqib Mumtaz
"""
import requests
import streamlit
import pandas as pd
import snowflake.connector
from urllib.error import URLError



streamlit.title('Snowflake Application')


#
# streamlit.header('Breakfast Menu') #
# streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
# streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
# streamlit.text('🐔 🥑🍞 Hard-Boiled Free-Range Egg')
#
df = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
# # Let's put a pick list here so they can pick the fruit they want to include

df = df.set_index('Fruit')
# streamlit.multiselect("Pick some fruits:", list(df.index),['Avocado','Strawberries'])
# streamlit.dataframe(df)

def my_fun(fruit):
    res = requests.get("https://fruityvice.com/api/fruit/"+ fruit)
    fruityvice_normalized = pd.json_normalize(res.json())
    return fruityvice_normalized

selected = streamlit.multiselect("Pick some fruits:", list(df.index),['Avocado','Strawberries'])
show = df.loc[selected]

streamlit.dataframe(show)


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

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The list contain:")
streamlit.dataframe(my_data_rows)
input = streamlit.text_input('What fruit u would like to add in database')
streamlit.write(f'you entered this fruit name : "{input}", Are you sure you want to add this?')
import streamlit as st

def my_fun_no():
    st.write('Your record has not been added')
def my_fun_yes():
    st.write(f'Thanks for Adding: {input}')

# Use a lambda function to pass my_fun as the on_click callback
# No = st.button('No', on_click=lambda: my_fun(), type="secondary")
No = st.button('No', type="secondary")
Yes = st.button('Yes', type="secondary")
if No == True:
    my_fun_no()
elif Yes == True:
    my_fun_yes()
    my_cur.execute(f"INSERT INTO PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST VALUES ('{input}')")
    streamlit.header("The updated list now:")
    my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
    my_data_rows = my_cur.fetchall()
    st.dataframe(my_data_rows)



# my_cur.execute(f'insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values {input}'
# Create a parameterized query with placeholders
# sql = 'INSERT INTO PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST VALUES (?)'

# Execute the query with the input values


# my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
# streamlit.dataframe(my_data_rows)








