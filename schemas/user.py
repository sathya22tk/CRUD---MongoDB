from typing import Optional


def user_entity(item) -> dict:
    return {
        "id": item["id"],
        "name": str(item["name"]),
        "description": str(item["description"]),
        "level": str(item.get("level", "")),
        "requirements": str(item["requirements"]),
        "instructor": str(item["instructor"]),
        "ratings": int(item["ratings"]),
        "price": int(item["price"])
    }


def users_entity(entity) -> list:
    return [user_entity(item) for item in entity]
