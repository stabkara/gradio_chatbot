import gradio as gr
import requests
import json

API_URL = "https://jj78yliqd7.execute-api.eu-central-1.amazonaws.com/dev/chatbot"

def send_prompt_to_api(prompt, message):
    params = {"prompt": prompt}
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        response_body = response.json().get('body')
        answer = response_body.get('answer')
        return answer
    else:
        return "Sorry, something went wrong. Please try again."

gr.ChatInterface(
    send_prompt_to_api,
    chatbot=gr.Chatbot(height=700),
    textbox=gr.Textbox(placeholder="Ask me a question", container=False, scale=7),
    title="Wissensguru - IDTA",
    theme="soft",
    examples=[
    ],
    cache_examples=False,
    retry_btn="Retry",
    undo_btn="Delete Previous",
    clear_btn="Clear",
).launch(server_name="0.0.0.0")
