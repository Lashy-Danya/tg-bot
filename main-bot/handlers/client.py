from aiogram import types, Dispatcher
from create_bot import dp

# @dp.message_handler(commands = ['start', 'help'])
async def command_start(message : types.Message):
    """Отправляет приветственное сообщение и помощь по боту"""
    await message.answer("Ну типо бот")

def handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands = ['start', 'help'])