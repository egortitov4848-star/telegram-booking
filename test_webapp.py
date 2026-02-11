import os
import json
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Тест",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
                "🚀 ТЕСТ",
                web_app=WebAppInfo(url="https://glampingbober.ru/telegram-booking/test.html")
            )
        ]])
    )

async def webapp_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("\n🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    print("🔥 DATA:", update.message.web_app_data.data)
    print("🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥\n")
    
    if update.message and update.message.web_app_data:
        await update.message.reply_text("✅ ЕСТЬ КОНТАКТ!")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, webapp_data))
    print("✅ ЗАПУЩЕНО")
    app.run_polling()

if __name__ == '__main__':
    main()
