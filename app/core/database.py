from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/ecommerce"

# 1. Create engine
engine = create_engine(DATABASE_URL)

# 2. Configure session builder
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. Quick startup check
try:
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
        print("✅ Connection successful!")
except OperationalError as e:
    print(f"❌ Connection failed: {e}")

# 4. Dependency injector for routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
        
class Base(DeclarativeBase):
    pass

