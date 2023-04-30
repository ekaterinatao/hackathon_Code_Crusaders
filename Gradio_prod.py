import gradio as gr
import numpy as np
import pandas as pd
import sqlite3


def query_database(query):
    connection = sqlite3.connect('/root/StartUps_DB.db')
    results = pd.read_sql_query(query, connection)
    df = pd.DataFrame(results)
    connection.close()
    return df

demo = gr.Interface(
    fn=query_database,
    inputs=[
        gr.Textbox(label="SQL query", value="SELECT * FROM StartUps_DB LIMIT 10"),
    ],
    outputs=gr.Dataframe(),
    title="StartUp Database Interactive Query Tool",
    description="Enter SQL query to retrieve data from our SQLite database with StartUps.",
)

if __name__ == "__main__":
    demo.launch(inbrowser=True, share=True, server_name ='0.0.0.0', server_port=8000)