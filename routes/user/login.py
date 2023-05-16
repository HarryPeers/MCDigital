from fastapi import APIRouter, Request

router = APIRouter()

# Check wether a credential is valid and authenticated or not.

@router.get("/api/credentials/login")
async def check_credentials(request:Request):
    pass

# Callback from microsoft oauth to add linked user to database.

@router.get("/api/credentials/callback")
async def register_callback(request:Request):
    pass