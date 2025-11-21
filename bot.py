import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.environ.get("8531453390:AAFHt_fVTpLC_pK97oOfgPjs9qqp6WQS9Z0")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ආයුබෝවන්! මම ඔබේ Telegram Chat Bot එකයි.\n"
        "ඔබට මේ bot එකෙන් chat කරන්න පුළුවන්."
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"ඔබ කීවා: {update.message.text}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("Bot started...")
    app.run_polling()
