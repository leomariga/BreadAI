from typing import Optional
#from generateRecipe import Recipe
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Input_net(BaseModel):
    nwords: int
    baseword: str

@app.get("/")
def read_root():
    return {"João": "O padeiro triste"}

@app.get("/generate/")
def generateget():
    #rcp = Recipe()
    return {'recipe':'Lorem ipsum dolor sit amet,\n consectetur adipiscing elit, sed \ndo eiusmod tempor incididunt ut labore et dolore \nmagna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat \nnon proident, sunt in culpa qui officia deseru\nnt mollit ani\n\nm id est laborum.'}#{'recipe':rcp.generate_text(item.baseword,item.nwords)}

    #return {'recipe':rcp.generate_text(firword,nwords)}


#@app.post("/generate/")
#async def generate(item: Input_net):
#    #rcp = Recipe()
#    return {'recipe':'Lorem ipsum dolor sit amet,\n consectetur adipiscing elit, sed \ndo eiusmod tempor incididunt ut labore et dolore \nmagna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat \nnon proident, sunt in culpa qui officia deseru\nnt mollit ani\n\nm id est laborum.'}#{'recipe':rcp.generate_text(item.baseword,item.nwords)}
