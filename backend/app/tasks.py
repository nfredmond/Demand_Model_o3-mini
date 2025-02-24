from celery import Celery
import osmnx as ox
import aequilibrae.project as ae
import cupy as cp
import numpy as np
from app.models import Zone, TripMatrix
from app.database import SessionLocal
from app.utils.model_utils import create_aequilibrae_project, compute_trip_matrix
import logging

logger = logging.getLogger(__name__)

celery_app = Celery('tasks', broker='redis://redis:6379/0', backend='redis://redis:6379/0')

def gpu_available():
    try:
        cp.cuda.Device(0).use()
        return True
    except Exception as e:
        logger.warning(f"GPU not available: {e}")
        return False

@celery_app.task
def run_demand_model(project_id: int):
    logger.info(f"Starting demand model for project {project_id}")
    try:
        project_path = create_aequilibrae_project(project_id)
        logger.info(f"AequilibraE project created at: {project_path}")
    except Exception as e:
        logger.error(f"Error creating AequilibraE project: {e}")
        return

    # Use GPU if available, else fall back to NumPy.
    array_module = cp if gpu_available() else np

    # (Optional) Fetch a network via OSMnx if needed.
    # For demonstration, we skip network extraction.
    
    db = SessionLocal()
    try:
        zones = db.query(Zone).all()
        trip_matrix = compute_trip_matrix(zones, use_chunking=True, array_module=array_module)
        for trip in trip_matrix:
            db.add(TripMatrix(origin_zone_id=trip["origin"], dest_zone_id=trip["dest"], trips=trip["trips"]))
        db.commit()
        logger.info(f"Demand model run completed for project {project_id}")
    except Exception as e:
        db.rollback()
        logger.error(f"Error during model computation: {e}")
    finally:
        db.close()
