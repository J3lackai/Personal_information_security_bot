from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from lexicon import guides


async def on_guide_select(
    callback: CallbackQuery, widget, dialog_manager: DialogManager, item_id: str
):
    n_header = dialog_manager.dialog_data.get("n_header")
    dialog_manager.dialog_data["answer"] = guides[n_header[item_id]]
    await dialog_manager.next()
