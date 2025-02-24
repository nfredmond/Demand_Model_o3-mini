from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import engine
from app.database import Base
from app.routers import auth, data_ingestion, model_computation, llm_services

app = FastAPI(
    title="Transportation Demand Modeling API",
    description="API for transportation demand modeling, data ingestion, and LLM queries.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers (authentication applied in endpoints)
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(data_ingestion.router, prefix="/data", tags=["Data Ingestion"])
app.include_router(model_computation.router, prefix="/model", tags=["Model Computation"])
app.include_router(llm_services.router, prefix="/llm", tags=["LLM Integration"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Transportation Demand Modeling API"}
