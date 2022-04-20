from aiogram import Bot
from aiogram.dispatcher import Dispatcher

import os
import sys

bot_token = os.getenv('TOKEN')

if not bot_token:
    sys.exit("Error: no token provided")

bot = Bot(token = bot_token)
dp = Dispatcher(bot)