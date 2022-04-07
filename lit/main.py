import types

from config import TOKEN, start_message, finding_bag

from aiogram import *
from tele_db import TeleDB
from user_db import UserDB
from parserdb import Database


class tele_bot (object):
    def __init__(self):
        self.bot = Bot(TOKEN)
        self.dp = Dispatcher(self.bot)
        self.general_bd = TeleDB()
        self.users_bd = UserDB()
        self.parser_bd = Database()
        self.coms = ['/start', '/help', '/clear_db', 'find *good_name']

        self.commands()

    def commands(self):
        @self.dp.message_handler(commands=['start'])
        async def process_start_command(message: types.Message):
            await message.reply(start_message)

        @self.dp.message_handler(commands=['help'])
        async def process_help_command(message: types.Message):
            await message.reply("  ".join(self.coms))

        @self.dp.message_handler(commands=['clear_db'])
        async def clear_db(msg: types.Message):
            self.users_bd.delete_from_db(msg.from_user.id, ())
            await self.bot.send_message(msg.from_user.id, "Data base has been cleared")

        @self.dp.message_handler()
        async def echo_message(msg: types.Message):
            if str(msg.text)[:4].lower().strip() == 'find':
                dates = self.parser_bd.find_in_db(str(msg.text)[5:].strip())
                if not dates:
                    await self.bot.send_message(msg.from_user.id, finding_bag)
                for s in dates:
                    await self.bot.send_message(msg.from_user.id, str(s.values())[18:-2])

            if self.general_bd.check_element_in_table(msg.from_user.id) == 0:
                self.general_bd.append_data_base(msg.from_user.id)
                self.users_bd.create_db(msg.from_user.id)
                self.users_bd.append_data_base(msg.from_user.id, msg.text)
            else:
                self.users_bd.append_data_base(msg.from_user.id, msg.text)

        executor.start_polling(self.dp, skip_updates=True)


my_bot = tele_bot()

