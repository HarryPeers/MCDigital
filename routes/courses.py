from fastapi import APIRouter, Request, HTTPException
from random import randint
from json import dump

router = APIRouter()

@router.post("/api/courses/create")
async def index(request:Request, key:str):

    payload = await request.json()

    if key != request.app.course_key: raise HTTPException(401, "You have not provided a correct key")

    id = randint(111111111,999999999)

    request.app.course_database[id] = payload
    
    with open(request.app.course_database_path, "w") as file: dump(request.app.course_database, file, indent=3)

    return {"id": id}


@router.get("/api/courses/")
async def index(request:Request): return request.app.course_database
