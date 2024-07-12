from fastapi import FastAPI


app = FastAPI(
    title="Task Traker"
)


@app.get("/")
async def main_page():
    return "Hello World!"
