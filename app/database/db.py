import json


async def write_to_db(info: dict):
    info["id"] = await _get_new_id()
    info["current_date"] = ""
    await _add_to_db(info)


async def _get_new_id() -> int:
    data = await read_db()
    max_id = -1
    for i in data:
        if i["id"] > max_id:
            max_id = i["id"]
    return max_id + 1


async def read_db() -> list:
    file = open("database/accounts.json", mode="r", encoding="UTF-8")
    try:
        data = json.loads(file.read())
    except Exception:
        data = []
    file.close()
    return data


async def _add_to_db(info: dict):
    data = await read_db()
    data.append(info)
    file = open("accounts.json", mode="w", encoding="UTF-8")
    file.write(json.dumps(data))
    file.close()


async def in_db(id_v: str) -> bool:
    try:
        file = await read_db()
        for i in file:
            if i["id"] == int(id_v):
                return True
    except Exception:
        pass
    return False


async def remove_by_id(id_v: str):
    try:
        file = await read_db()
        new_data = []
        for i in file:
            if i["id"] != int(id_v):
                new_data.append(i)
        file = open("accounts.json", mode="w", encoding="UTF-8")
        file.write(json.dumps(new_data))
        file.close()
    except Exception:
        pass
