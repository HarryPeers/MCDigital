from fastapi import APIRouter, Request

router = APIRouter()

# View all blogs

@router.get("/api/admin/blogs/all")
async def all_blogs(request:Request):
    pass

# View details of a single blog
# Path param: id:int

@router.get("/api/admin/blogs/{id}/view")
async def view_blog(request:Request, id:int):
    pass

# Delete a blog
# Path param: id:int

@router.delete("/api/admin/blogs/{id}/delete")
async def delete_blog(request:Request, id:int):
    pass

# Approve a blog
# Path param: id:int

@router.delete("/api/admin/blogs/{id}/approve")
async def approve_blog(request:Request, id:int):
    pass

# Deny a blog
# Path param: id:int

@router.delete("/api/admin/blogs/{id}/deny")
async def deny_blog(request:Request, id:int):
    pass