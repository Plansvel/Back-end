from fastapi import HTTPException
from schemas import user_schema
from settings import supabase

connection = supabase.create_supabase_client()

def user_exists(key: str = "email", value: str = None):
    user = connection.table("usuario").select("*").eq(key, value).execute()
    return len(user.data) > 0

def create_user(user: user_schema.UserCreate):
    try:
        user_email = user.email.lower()
        
        if user_exists(value=user_email):
            raise HTTPException(status_code=400, detail="Email already registered")
        
        user_created = connection.table("usuario").insert({
            "nome":user.nome,
            "email":user.email,
            "cpf":user.cpf, 
            "telefone": user.telefone,
            "senha":user.senha
            }).execute()
        
        if user_created:
            return user_created
        else:
            raise HTTPException(status_code=412, detail="User creation failed")
    
    except HTTPException as http_exception:
        raise http_exception
    