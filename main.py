
from fastapi import FastAPI
import nest_asyncio
from pyngrok import ngrok
import uvicorn

# Allow nested event loops
nest_asyncio.apply()

app = FastAPI()
views = {"reel1": 0}

@app.post("/views/{reel_id}")
def add_view(reel_id: str):
    views[reel_id] = views.get(reel_id, 0) + 1
    return {"views": views[reel_id]}

@app.get("/views/{reel_id}")
def get_views(reel_id: str):
    return {"views": views.get(reel_id, 0)}

# Expose server
public_url = ngrok.connect(8000)
print("Public URL:", public_url)

uvicorn.run(app, host="0.0.0.0", port=8000)
