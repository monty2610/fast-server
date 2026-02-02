from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get_books():
    return [{
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald"
    }]