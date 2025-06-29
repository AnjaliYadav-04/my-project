# bot/telegram_bot.py
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from telegram.ext import ApplicationBuilder, CommandHandler
from django.contrib.auth import get_user_model
from decouple import config

User = get_user_model()
TOKEN = config('TELEGRAM_BOT_TOKEN')

async def start(update, context):
    username = update.effective_user.username
    user, _ = User.objects.get_or_create(username=username)
    user.telegram_username = username
    user.save()
    await update.message.reply_text(f"Welcome {username}, your Telegram username is saved!")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
