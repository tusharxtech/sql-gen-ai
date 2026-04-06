import streamlit as st
from langchain_community.llms import Ollama
import sqlite3
from dotenv import load_dotenv
load_dotenv()

import os
os.environ["LANGCHAIN_API_KEYS"]=os.getenv("LANGCHAIN_API_KEY")
# os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")
# os.environ["LANGCHAIN_TRACKING_V2"]="True"
os.environ["OLLAMA_API_KEY"]=os.getenv("OLLAMA_API_KEY")

llm=Ollama(model="llama3.2:1b")
prompt= """
you are an expert sql query assistant.
input constist query in text 
you convert the text to sql query

important instruction-
Return ONLY valid SQLite SQL query.
Do NOT explain.
Do NOT add text.
do not give header just sql-query
Do NOT add backticks or any type of punctuations.
Only output SQL runnable  query 

table looks like this 


products (product_id, product_name, category, price, stock_quantity)
"""


# def to generate response

def get_user_query_response(query,prompt):
    response=llm.invoke(prompt + "\nUser request: " + query)
    sql = response.replace("```sql", "").replace("```", "").strip()
    print(sql)
    return (sql)

# def to execute query

def query_executer(db,response):
    conn=sqlite3.connect("sqldb.db")
    cur=conn.cursor()
    cur.execute(response)
    rows=cur.fetchall()
    print(rows)
    conn.commit()
    conn.close()
    for row in rows:
        print (row)
    return rows


# Streamlit

query=st.text_input("input",key="input")
submit=st.button("ask th question")

if submit:
    response=get_user_query_response(query,prompt)
    execute=query_executer("sqldb.db",response)
    print(response)
    for row in execute:
        print(row)
        st.header(row)
