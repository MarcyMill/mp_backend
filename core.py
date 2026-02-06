from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_methods=["*"],
	allow_headers=["*"],
)

@app.get("/")
def root():
	return {"message": "mp_backend is running"}

@app.get("/")
def add(a: int, b: int):
	return {"result": a + b}

@app.get("/search")
def search_system(name: str):
	existing_systems = {"lybams"}

	return {
		"exists": name.lower() in existing_systems
	}