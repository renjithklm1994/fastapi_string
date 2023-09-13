from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

class ReverseRequest(BaseModel):
    input_string: str


@app.post("/reverse/")
async def reverse_string(request_data: ReverseRequest):
    input_string = request_data.input_string
    reversed_string = input_string[::-1]
    return {"reversed_string": reversed_string}

@app.get("/reverse/", status_code=405)
async def get_method_not_allowed():
    raise HTTPException(status_code=405, detail="Method Not Allowed")

@app.exception_handler(HTTPException)
async def unprocessable_entity_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": "Unprocessable Entity", "detail": exc.detail},
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
