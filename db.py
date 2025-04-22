from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database configuration
DATABASE_URL = "postgresql://postgres:Quiet%402310@localhost:5433/postgres" 
engine = create_engine(DATABASE_URL, echo=True)

# Create a session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declare Base class for models
Base = declarative_base()
