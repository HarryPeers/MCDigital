from fastapi import APIRouter, Request

router = APIRouter()

# View all users

@router.get("/api/admin/users/all")
async def all_users(request:Request):
    pass

# View details of a single user
# Path param: id:int

@router.get("/api/admin/users/{id}/view")
async def view_user(request:Request, id:int):
    pass

# Delete a user
# Path param: id:int

@router.delete("/api/admin/users/{id}/delete")
async def delete_user(request:Request, id:int):
    pass

# Change admin status
# Path param: id:int
# Query param: admin:bool

@router.delete("/api/admin/blogs/{id}/admin")
async def status_user(request:Request, id:int, admin:bool):
    pass
