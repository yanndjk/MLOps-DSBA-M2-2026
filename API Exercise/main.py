from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/{surface}")
def read_item(surface: int):
    '''
    Get the surface area.

    Args:
        surface (int): The surface area to be returned.

    Returns:
        dict: A dictionary containing the surface area or an error message.
    '''
    try:
        surface = int(surface)
        
        if surface < 0:
            return {"error": "Surface area cannot be negative"}
        return {"surface": surface}
    
    except ValueError:
        return {"error": "Invalid input. Please provide a valid integer for surface area."}

#test by pasting http://127.0.0.1:8000/50   in the browser after running the app with: uvicorn main:app --reload
#you should see {"surface": 50}
