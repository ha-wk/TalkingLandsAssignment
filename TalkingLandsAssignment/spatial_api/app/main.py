from fastapi import FastAPI
from app.routes import points, polygons

app = FastAPI(title="Spatial Data API", version="1.0")

# Register routes
app.include_router(points.router, prefix="/api", tags=["Points"])
app.include_router(polygons.router, prefix="/api", tags=["Polygons"])

@app.get("/")
def root():
    return {"message": "Welcome to the Spatial Data API!"}
