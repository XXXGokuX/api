from fastapi import FastAPI
from database import Base,engine
from routes import userRoutes

app= FastAPI()

# create the tables (if they don't exist)
Base.metadata.create_all(bind= engine)

app.include_router(userRoutes.router)


    
