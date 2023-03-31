from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define the database connection parameters
from envVariables import envObj

# Create the database connection URL
db_url = f'mysql+pymysql://{envObj.DB_USER}:{envObj.DB_PASSWORD}@{envObj.DB_HOST}:{envObj.DB_PORT}/{envObj.DB_NAME}'

# Create the SQLAlchemy engine
engine = create_engine(db_url)

SessionLocal = sessionmaker(autoflush=False,autocommit= False,bind= engine)

Base= declarative_base()



# dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# # Test the database connection
# try:
#     conn = engine.connect()
#     print("Connected to database")
# except Exception as e:
#     print(f"Error connecting to database: {str(e)}")

