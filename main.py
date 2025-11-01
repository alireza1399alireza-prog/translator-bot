main.py
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from googletrans import Translator

translator = Translator()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 سلام! من ربات مترجم هستم. هر متنی بفرستی، برات ترجمه‌اش می‌کنم.")

async def translate_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    result = translator.translate(text, dest='fa')
    await update.message.reply_text(f"🌐 ترجمه:\n{result.text}")

app = ApplicationBuilder().token("توکن_ربات_خودت").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate_text))

app.run_polling()
