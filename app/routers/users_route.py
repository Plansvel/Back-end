from fastapi import APIRouter, status, HTTPException
from schemas import user_schema
from services import user_service

router = APIRouter(prefix="/users",
                   tags=["User"],
                   responses={400: {"description": "Not found"}})

@router.post('', status_code=status.HTTP_201_CREATED, response_model=user_schema.User)
async def register_user(user: user_schema.UserCreate):
    try:
        user_created = user_service.create_user(user)
        return user_created
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))