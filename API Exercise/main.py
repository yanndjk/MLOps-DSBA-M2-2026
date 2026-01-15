from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/{surface}")
def read_item(surface: int):
    return {"surface": surface}

#test by pasting http://127.0.0.1:8000/50   in the browser after running the app with: uvicorn main:app --reload
#you should see {"surface": 50}