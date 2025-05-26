from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def data1():
    return {"message":" hello my dear class I am here for you. "}

@app.get("/api")
def data2():
    return [
        {
            "name":"humera",
            "age": 23,
            "class":"MS Artificial Intelligence"
        },
           {
            "name":"ahmad",
            "age": 23,
            "class":"MS Artificial Intelligence"
        },
           {
            "name":"Moeez",
            "age": 23,
            "class":"MS Artificial Intelligence"
        },
    ]
