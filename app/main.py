from fastapi import Depends, FastAPI
from routers import users_route
from settings import supabase

app = FastAPI()

connection = supabase.create_supabase_client()

app.include_router(users_route.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

@app.get("/testdb")
async def buscarUsuarios():
    usu = connection.table('usuario').select('*').execute()
    return usu