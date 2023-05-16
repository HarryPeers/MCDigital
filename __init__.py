# Load all locally installed packages

from sys import path
from os import getenv, getcwd, system, walk, listdir

# Make colorama (ANSI) work in console

system("") 

# Allow imports from .local installed packages

path.append(f"{getcwd()}/.local")

# Load imports

from dotenv import load_dotenv
from fastapi import FastAPI
from uvicorn import run

from modules import modules

# Create the app

app = FastAPI()
app.cwd = getcwd()

# Load enviromental variables

load_dotenv(f"{app.cwd}/variables.env")

# Restrictions

  # Restrict what categories of resources users can get.
app.permitted_resource_categories = [None if "." in x else x for x in listdir(f"{app.cwd}/resources/")]
app.permitted_resource_categories.remove(None)

# Load the routers from the routes folder.

for router in walk(f"{app.cwd}/routes/"):
    base = router[0].split("routes")[-1][1:]
    if len(base) != 0:
        base = "." + base
    for file in router[2]:
        if file.endswith(".py") and not file.startswith("_"):
            exec(f"from routes{base}.{file.split('.')[0]} import router; app.include_router(router)")
            
# Run the app using uvicorn

if __name__ == "__main__": run("__init__:app", host=getenv("HOST"), port=int(getenv("PORT")))