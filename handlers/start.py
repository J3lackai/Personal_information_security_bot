from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from states import StartSG
from aiogram_dialog import StartMode, DialogManager

router = Router()


@router.message(CommandStart())
async def command_start(message: Message, dialog_manager: DialogManager):
    await message.answer("Здравствуйте!")
    await dialog_manager.start(state=StartSG.main_menu, mode=StartMode.RESET_STACK)
