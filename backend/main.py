from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
  return {"Hello": "World"}


@app.get("/health", status_code=200)
def read_health():
  return {"status": 'OK'}