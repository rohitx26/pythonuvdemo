from fastapi import FastAPI
import uvicorn

app = FastAPI()


def main():
    print("Hello from pythonuvdemo!")
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)


if __name__ == "__main__":
    main()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users")
def read_users():
    return {"users": ["alice", "bob", "charlie"]}
