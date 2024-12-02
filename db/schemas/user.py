def user_schema(user) -> dict:
    return{"id": user["id"],
            "username": user["username"],
            "email": user["email"]
            }