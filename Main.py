import telebot
import google.generativeai as genai
import os
from dotenv import load_dotenv, dotenv_values
genai.title = 'Royal Katsic Ai'

load_dotenv()

# Replace `os.getenv("TELEGRAM_TOKEN")` with your own token
bot = telebot.TeleBot(os.getenv("7252003737:AAHj2qNq5OMu8lEqrOAID_Q9_3VCo32k1R4", parse_mode=None)

# Replace `os.getenv("GENAI_API_KEY")` with your own API key
genai.configure(api_key=os.getenv("AIzaSyCDILzurQ1o7f-98cBZrSenRqtVUbTD9DI"))

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

model = genai.GenerativeModel(model_name="gemini-1.5-pro",
                              generation_config=generation_configaa
convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["Hi"]
  },
  {
    "role": "model",
    "parts": ["Hello This Royal Katsic Ai! How can I assist you today?"]
  },
])

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    convo.send_message(message.text)
    response = convo.last.text
    bot.reply_to(message, response)
	

bot.infinity_polling()
