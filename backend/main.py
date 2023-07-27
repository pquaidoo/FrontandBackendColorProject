import uvicorn 

#Entry Point:
if __name__ == "__main__":
    uvicorn.run("app.api:app", host = "0.0.0.0", port = 8000, reload = True)
#terminal commands:
#python -m venv venv
#venv\Scripts\activate
#set PYTHONPATH=%CD%

