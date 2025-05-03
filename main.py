from fastapi import FastAPI
import uvicorn
import requests

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


@app.get("/getquote")
def get_quote():
    try:
        response = requests.get("https://api.quotable.io/random", verify=False)
        data = response.json()

        if "content" in data and "author" in data:
            quote = data["content"]
            author = data["author"]
            return {"quote": quote, "author": author}

        else:
            return {"error": "Failed to fetch quote"}
    except Exception as e:
        return {"error": str(e)}
