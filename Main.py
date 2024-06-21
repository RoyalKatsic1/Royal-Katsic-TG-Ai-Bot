import google.generativeai as genai
import telebot

genai.title = 'Royal Katsic Ai'

# Your Telegram bot token
TOKEN = '7252003737:AAHj2qNq5OMu8lEqrOAID_Q9_3VCo32k1R4'

# Configure the generative AI API key
gemini.configure(api_key="AIzaSyCDILzurQ1o7f-98cBZrSenRqtVUbTD9DI")

# Create a Telegram bot instance
bot = telebot.TeleBot('7252003737:AAHj2qNq5OMu8lEqrOAID_Q9_3VCo32k1R4')

@bot.message_handler(func=lambda message: True)
def handle_general_message(message):
    """Handles all other messages received by the bot.

    Args:
        message (telegram.Message): The Telegram message object.

    Returns:
        None
    """

    name = message.from_user.first_name
    msg = message.text

    # Check for empty message
    if msg == "":
        return  # Do nothing for empty messages

    # Provide a friendly greeting and acknowledge the user's message
    greeting = f"Hi {name}, thanks for contacting Royal Katsic Ai !"
    response = f"I didn't quite understand '{msg}'\n"

    # Offer assistance based on potential use cases
    response += ("Here are some things I can help you with:\n"
                 "- Search for products: Tell me what you're looking for (e.g., 'find laptops under $500').\n"
                 "- Get help: Ask me a question about using the bot or Telegram in general.\n"
                 "- Just chat: I'm happy to chat about anything you like!")

    bot.send_message(message.chat_id, greeting + "\n" + response)
        
        # Default parameters for the generative AI model
        defaults = {
            'model': 'models/chat-bison-001',
            'temperature': 0.25,
            'candidate_count': 1,
            'top_k': 40,
            'top_p': 0.95,
        }
        
        context = ""
        examples = [
            [
                " ",
            ]
        ]
        
        examples[0].append(str(msg))
        messages = []
        messages.append("NEXT REQUEST")
        
        # Generate response using the generative AI model
        response = generate_response.chat(
            **defaults,
            context=context,
            examples=examples,
            messages=messages
        )
        
        print(response.messages)
        print(response.last)
        bot.reply_to(message, response.last)
    
    except Exception as e:
        bot.reply_to(message, str(e))
        bot.reply_to(message, "Sorry, an error occurred while processing your request.")

# Start the bot's polling loop
if __name__ == "__main__":
    bot.polling()
