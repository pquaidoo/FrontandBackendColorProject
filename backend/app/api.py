
from fastapi import FastAPI
#Base rout
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

colorList = [
    "Blue",
    "Red",
    "Yellow",
    "White",
    "Black",
    "Purple",
    "Orange",
    "Green",
    "Pink"
]
colorHistory = []

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/color/{color}")
async def get_color(color:str):
    for i in colorList:
        if i == color:
            colordata = " ",len(colorHistory)+1,":",{color}
            colorHistory.append(colordata)
            return {"message": f"You Chose {color}"}
    return {"message": "Not Valid Color"}

@app.get("/colorHistory")
async def get_colorHistory():
    return(colorHistory)

@app.delete("/colorHistory")
async def clear_color_history():
    colorHistory.clear()
    return {"message": "Color history has been cleared."}
