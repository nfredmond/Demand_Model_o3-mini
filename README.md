============================================================
        ADVANCED TRANSPORTATION DEMAND MODELING WEB APP
============================================================

OVERVIEW
---------
This is a full-stack web application for transportation demand modeling, 
providing real-time insights and interactive analysis tools.

KEY FEATURES:
- BACKEND (FastAPI):
  - Authentication (JWT-based)
  - Geospatial data ingestion (various formats supported)
  - Advanced model computation (AequilibraE for multi-user isolation, GPU-accelerated CuPy)
  - LLM integration for AI-driven policy simulation

- FRONTEND (React + TypeScript):
  - Interactive mapping with React-Leaflet
  - File uploads for custom geospatial data
  - Model configuration & execution
  - Results visualization
  - AI-powered chat interface

- DEPLOYMENT (Docker-based):
  - PostgreSQL/PostGIS for geospatial data storage
  - Redis & Celery for handling background tasks
  - JWT authentication for secure user management

============================================================
                      SETUP INSTRUCTIONS
============================================================

BACKEND SETUP:
---------------
1. Navigate to the backend directory:
   $ cd backend/

2. Install dependencies:
   $ pip install -r requirements.txt

3. Set environment variables:
   $ export DATABASE_URL="your_postgresql_connection_string"
   $ export OPENAI_API_KEY="your_openai_api_key"

4. Start the backend server:
   $ uvicorn app.main:app --reload

-----------------------------------------

FRONTEND SETUP:
---------------
1. Navigate to the frontend directory:
   $ cd frontend/

2. Install dependencies:
   $ npm install

3. Start the frontend:
   $ npm start

-----------------------------------------

DOCKER DEPLOYMENT:
-------------------
1. Ensure Docker and Docker Compose are installed.
2. From the project root, run:
   $ docker-compose up --build
   This will start all services, including:
   - Backend (FastAPI)
   - Frontend (React)
   - Database (PostGIS)
   - Redis & Celery for background tasks

============================================================
                     AUTHENTICATION
============================================================

For demonstration, the backend requires the following HTTP header:

   Authorization: Bearer secret-token

In production, replace this with proper JWT token handling 
and secure key management.