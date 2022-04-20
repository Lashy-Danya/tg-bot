from aiogram.utils import executor
from create_bot import dp
from handlers import client

import logging

# logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

async def on_startup(_):
    print("Бот в онлайне")

client.handlers_client(dp)

# @dp.message_handler()
# async def echo(message : types.Message):
#     await message.answer(message.text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True, on_startup = on_startup)