# Spatial Data API
Please find below steps to make it run and test with any inputs :-
## Overview
This is a FastAPI-based **Spatial Data API** that allows users to store and retrieve **points (latitude & longitude)** and **polygons (spatial regions)** using **PostgreSQL with PostGIS**. The API enables spatial queries and geometric operations efficiently.

## Features
✅ Store **geographical points** (latitude, longitude).  
✅ Store **polygon boundaries** (spatial regions).  
✅ Retrieve and query spatial data using **PostGIS**.  
✅ Integrated with **FastAPI** for high-performance API handling.  

## Prerequisites
Ensure you have the following installed:
- Python 3.8+
- PostgreSQL with PostGIS enabled
- Virtual Environment (`venv`)

## Installation & Setup
### 1️⃣ **Clone the Repository**
```bash
$ git clone <repository-url>
$ cd spatial_api
```

### 2️⃣ **Setup PostgreSQL with PostGIS**
Start **PostgreSQL CLI** and create the database:
```sql
CREATE DATABASE spatial_db;
\c spatial_db;
CREATE EXTENSION postgis;
```

### 3️⃣ **Create Required Tables**
```sql
CREATE TABLE points (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    coordinates GEOMETRY(POINT, 4326) NOT NULL
);

CREATE TABLE polygons (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    boundary GEOMETRY(POLYGON, 4326) NOT NULL
);
```

### 4️⃣ **Setup Virtual Environment & Install Dependencies**
```bash
$ python3 -m venv venv
$ source venv/bin/activate   # For Linux/Mac
$ venv\Scripts\activate     # For Windows
$ pip install -r requirements.txt
```

### 5️⃣ **Configure `.env` File**
Create a `.env` file in the project root and add:
```
DATABASE_URL=postgresql://postgres:password@localhost/spatial_db
```

### 6️⃣ **Run the API Server**
```bash
$ uvicorn app.main:app --reload
```
Expected Output:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

## API Endpoints
### 📌 **Add a Point**
```bash
curl -X 'POST' 'http://127.0.0.1:8000/api/points/' \
     -H 'Content-Type: application/json' \
     -d '{"name": "City Center", "latitude": 12.9716, "longitude": 77.5946}'
```
Response:
```json
{
  "id": 1,
  "name": "City Center",
  "coordinates": "POINT(77.5946 12.9716)"
}
```

### 🔳 **Add a Polygon**
```bash
curl -X 'POST' 'http://127.0.0.1:8000/api/polygons/' \
     -H 'Content-Type: application/json' \
     -d '{"name": "Zone A", "coordinates": [[77.5, 12.9], [77.6, 12.9], [77.6, 13.0], [77.5, 13.0], [77.5, 12.9]]}'
```
Response:
```json
{
  "id": 1,
  "name": "Zone A",
  "boundary": "POLYGON((77.5 12.9, 77.6 12.9, 77.6 13.0, 77.5 13.0, 77.5 12.9))"
}
```

## Running Tests
### 🔍 **Run API Tests**
```bash
pytest tests/
```
Example test file (`tests/test_api.py`):
```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_point():
    response = client.post("/api/points/", json={"name": "Test Point", "latitude": 10.0, "longitude": 20.0})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Point"

def test_add_polygon():
    response = client.post("/api/polygons/", json={"name": "Test Polygon", "coordinates": [[10, 10], [20, 10], [20, 20], [10, 20], [10, 10]]})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Polygon"
```

