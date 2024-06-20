import google.generativeai as Gemini
import telebot

# Replace with your Telegram Bot token
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Replace with your Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize Telegram Bot
bot = telebot.TeleBot(BOT_TOKEN)

# Initialize Gemini Client
client = GFPTClient(api_key=GEMINI_API_KEY)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hi! I'm Royal Katsic, your friendly Telegram AI powered by @Itsroyalkatsic. Ask me anything or give me instructions, and I'll do my best to assist you.")

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    prompt = message.text

    # Send the prompt to the Gemini API
    response = client.text_completion(prompt=prompt)

    # Send the response back to the chat
    bot.reply_to(message, response.text)

# Handle potential errors gracefully
@bot.message_handler(func=lambda message: True)
def handle_errors(message):
    # Log the error for debugging
    print("An error occurred:", message.exception)
    bot.reply_to(message, "Oops, something went wrong. Please try again later.")

# Run the bot
bot.infinity_polling()
