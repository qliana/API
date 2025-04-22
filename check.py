from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://postgres:Quiet%402310@localhost:5433/postgres"
engine = create_engine(DATABASE_URL)

try:
    # Try to connect and fetch the version of PostgreSQL
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        print(result.fetchone())
except Exception as e:
    print(f"Error: {e}")
