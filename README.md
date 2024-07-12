;# telegramBot-CommandHandler

This Python project creates a simple Telegram bot using the python-telegram-bot library. The bot is capable of responding to two commands: /hello and /ping. The /hello command greets the user by name, while the /ping command performs a ping to Google's public DNS (8.8.8.8) and returns the output to the user.

## Features
Greet Users: Responds to /hello with a personalized greeting.
Ping Google DNS: Executes a ping to 8.8.8.8 and returns the result when /ping is called.

## Requirements
Python 3.x
python-telegram-bot library

## Setup and Installation
1. Install Dependencies: Ensure Python 3.x is installed on your system. Then, install the required Python package:
```sh
pip install -r requirements.txt
```
2. Telegram Bot Token: You must have a Telegram bot token. If you don't have one, you can create a bot and obtain a token by chatting with the BotFather on Telegram.

3. Configure the Token: Replace the placeholder token in the script with your actual Telegram bot token:
```sh
app = ApplicationBuilder().token("YOUR_TELEGRAM_BOT_TOKEN").build()
```
## Running the Bot
Execute the script to start the bot:
```sh
python main.py
```

## Telegram Settings
1. Search for "BotFather"
   
![image](https://github.com/user-attachments/assets/f3f35b70-30b8-4eea-815b-c2cdcc83a166)

3. Check all the commands by typing "/help"

![image](https://github.com/user-attachments/assets/087f8bb3-43d8-49b9-9db5-33711247a1c0)

4. Execute "/newbot" command on telegram console and follow up the menu

![image](https://github.com/user-attachments/assets/95667bae-23a8-484b-b423-6d2a508900df)

This bot already removed. So the token you see above do not work.

5. You can see the token value now

Once the bot is running, you can interact with it by sending /hello or /ping commands in the chat.

## Security Note
Ensure you keep your Telegram bot token secure and never expose it in public repositories or forums.

## License
This project is open-sourced under the MIT License.

