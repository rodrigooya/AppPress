from fastapi import FastAPI
from dotenv import dotenv_values
from db.client import db_client
from routers import users_db, products,jwt_auth_users

config = dotenv_values(".env")

app = FastAPI()
#routers

app.include_router(products.router)

app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = db_client
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

@app.get("/")
async def root():
    return "hola Rodrigo"

@app.get("/url")
async def root():
    return {"message": "Hello World"} 