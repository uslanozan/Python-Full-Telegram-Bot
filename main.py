from telethon import TelegramClient
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

#! Use your own values from my.telegram.org


configure()
#! Create an .env file and define api_id and api_hash. If these print works successfully it's okay.
#! Add *.session in .gitignore file. Because session logs may includes credentials and must NOT be shared. 
print(os.environ.get('api_id'))
print(os.environ.get('api_hash'))


#?When it first running program. The system asks: 
#?  - BOT Token or Phone Number
#?  - Message Code (In Telegram)
#?  - Password

# The first parameter is the .session file name (absolute paths allowed)
with TelegramClient('anon', os.environ.get('api_id'), os.environ.get('api_hash')) as client:
    client.loop.run_until_complete(client.send_message('me', 'Hello, Cruel World!'))