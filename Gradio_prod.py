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


wiki_df = pd.read_csv('/root/data/wiki_modified.csv')

with gr.Blocks() as demo:
    gr.Markdown("StartUp Database created within MIPT Hackaton by Code_Crusaders Team.")
    with gr.Tab("Whole Database"):
        with gr.Row():
            query = gr.Textbox(label="Your query", value="SELECT * FROM StartUps_DB LIMIT 10")
        with gr.Row():
            output = gr.Dataframe()
        with gr.Row():
            execution_btn = gr.Button("Execute query")
            execution_btn.click(fn=query_database, inputs=query, outputs=output, api_name="Execute your query                                                                                ")

    with gr.Tab("Wikipedia"):
        with gr.Row():
            df_output = gr.DataFrame(value=wiki_df)

    with gr.Tab('Database content'):
        gr.Image('Dataset_СС.png')

if __name__ == "__main__":
    demo.launch(inbrowser=True, share=True, server_name ='0.0.0.0', server_port=8001)


# def query_database(query):
#     connection = sqlite3.connect('/root/StartUps_DB.db')
#     results = pd.read_sql_query(query, connection)
#     df = pd.DataFrame(results)
#     connection.close()
#     return df

# demo = gr.Interface(
#     fn=query_database,
#     inputs=[
#         gr.Textbox(label="SQL query", value="SELECT * FROM StartUps_DB LIMIT 10"),
#     ],
#     outputs=gr.Dataframe(),
#     title="StartUp Database Interactive Query Tool",
#     description="Enter SQL query to retrieve data from our SQLite database with StartUps.",
# )

# if __name__ == "__main__":
#     demo.launch(inbrowser=True, share=True, server_name ='0.0.0.0', server_port=8000)