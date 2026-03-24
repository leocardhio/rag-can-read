import psycopg
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import chat, healthcheck, documents
from config import get_settings

db_connection = psycopg.connect(
  database=get_settings().postgres_db,
  host=get_settings().postgres_host,
  user=get_settings().postgres_user,
  password=get_settings().postgres_password,
  port=get_settings().postgres_port
)

app = FastAPI(debug=True)
origins = [
  "http://localhost:3000"
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(healthcheck.router)
app.include_router(chat.router)
app.include_router(documents.router)