from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return "Hi, my name is FastAPI"