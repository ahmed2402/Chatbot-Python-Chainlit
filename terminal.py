import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

while True:
    user_input = input("Enter your message (type 'q' to quit): ")
    if user_input.lower() == 'q':
        print("Exiting the chatbot. Goodbye!")
        break
    response = model.generate_content(user_input)
    print(response.text)
    