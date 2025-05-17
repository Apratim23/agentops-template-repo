# main.py
from fastapi import FastAPI, Query
from utils import load_chunks, find_relevant_chunk
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/info/")
def get_info(query: str = Query(..., description="Ask about booking, menu, etc.")):
    chunks = load_chunks()
    match = find_relevant_chunk(query, chunks)

    if match:
        content = match["content"]
        if len(content.split()) > 600:
            content = " ".join(content.split()[:600]) + "..."  # simulate truncation
        return {"response": content}
    else:
        return JSONResponse(
            status_code=404,
            content={
                "response": "Sorry, I couldn't find relevant info. Please try rephrasing your query or contact support."
            }
        )
