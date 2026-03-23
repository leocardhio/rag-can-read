from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import chat, healthcheck, documents

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