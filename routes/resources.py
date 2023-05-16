from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import FileResponse
from os import path

router = APIRouter()

@router.get("/")
async def index(request:Request): return FileResponse(f"{request.app.cwd}/resources/pages/index.html")

@router.get("/{page}")
async def index(request:Request, page:str):
    if not path.exists(f"{request.app.cwd}/resources/pages/{page}.html"): raise HTTPException(404, "File not found.")
    return FileResponse(f"{request.app.cwd}/resources/pages/{page}.html")

@router.get("/resources/{category}/{file}")
async def get_resource(request:Request, category, file):
    if category not in request.app.permitted_resource_categories: raise HTTPException(404, "Category of resources not found.")
    if not path.exists(f"{request.app.cwd}/resources/{category}/{file}"): raise HTTPException(404, "File not found.")

    return FileResponse(f"{request.app.cwd}/resources/{category}/{file}")
    
