from fastapi import FastAPI

app = FastAPI()

@app.post("/reverse/")
async def reverse_string(input_string: str):
    reversed_string = input_string[::-1]
    return {"reversed_string": reversed_string}
