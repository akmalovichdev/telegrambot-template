import logging
from aiogram import types
from aiogram.dispatcher import FSMContext
from bot import dp

logger = logging.getLogger(__name__)

# Команда /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message, state: FSMContext, is_new_user: bool = False):
    """Обработчик команды /start"""
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    # Приветственное сообщение
    if is_new_user:
            text = f"""

"""

    await message.reply(text, parse_mode='HTML')
    await state.finish()
