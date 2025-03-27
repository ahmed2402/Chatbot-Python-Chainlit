import os
import chainlit as cl
import google.generativeai as genai
from dotenv import load_dotenv
from typing import Optional,Dict

load_dotenv()
print(os.getenv("OAUTH_GITHUB_CLIENT_ID"))
gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

@cl.oauth_callback
def oaut_callback(
    provider_id : str ,
    token : str,
    user_data : Dict[str, str],
    default_user : cl.User,
) -> Optional[cl.User]:
    """
    Handle the OAUTH Callback from GITHUB
    RETURN THE USER OBJ IF AUTH IS SUCCESSFUL, none otherwise 
    """
    print(f"Provide : {provider_id}")
    print(f"User Data : {user_data}")

    return default_user

@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history" ,[])
    await cl.Message(content="Hey! How can I help you today?").send()

@cl.on_message
async def handle_message(message: cl.Message):
    prompt = message.content
    response = model.generate_content(prompt)

    response_text = response.text if hasattr(response , "text") else ""
    await cl.Message(content=response_text).send()    