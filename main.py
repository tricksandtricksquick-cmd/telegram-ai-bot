import telebot
from groq import Groq

# Apni keys yahan paste karein
BOT_TOKEN = "8802524461:AAHG7MTCSIDUSu0M_qX20bO7izuMYGmVRLs"
GROQ_API_KEY = "APKI_GROQ_API_KEY"

bot = telebot.TeleBot(BOT_TOKEN)
client = Groq(api_key=GROQ_API_KEY)

@bot.message_handler(func=lambda message: True)
def chat_ai(message):
    # Groq ka Llama 3 model use kar rahe hain
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": message.text}],
        model="llama3-8b-8192", 
    )
    bot.reply_to(message, response.choices[0].message.content)

bot.infinity_polling()
