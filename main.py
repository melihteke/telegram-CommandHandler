from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import subprocess

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("hello telegram")
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def ping_google(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("pinging google dns")
    command = ['ping', '-c', '4', "8.8.8.8"]
    output = subprocess.check_output(command, universal_newlines=True)
    print(output)
    await update.message.reply_text(f'Hello {update.effective_user.first_name} - \n Ping output: {output}')



app = ApplicationBuilder().token("6935929131:AAETTYK3-wnt6OxOHvMLkiJQRRY2lweiXfc").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("ping", ping_google))

app.run_polling()
