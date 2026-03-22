from aiogram_dialog import DialogManager
from lexicon import guides


async def guide_getter(dialog_manager: DialogManager, **_):
    guides_: dict[str:str] = guides
    guides_items: list = []
    if guides is None:
        return {"guides_items": ""}
    n = 0
    n_header: dict = dict()
    for i in guides_.keys():
        guides_items.append({"id": n, "text": i})
        n_header[n] = i
        n += 1
    dialog_manager.dialog_data["n_header"] = n_header
    return {"guides_items": guides_items}
