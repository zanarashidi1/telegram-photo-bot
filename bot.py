from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8680792541:AAHJB-htaKwEdEH7XLlzGBzJ1ER_aZ7R7Jc"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ربات فعال است ✅")


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()