from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def root():
    return {"word":"hello world"}

#Single parameters
@app.get("/hello/{name}/{age}")
async def hello(name,age):
    return {"name":name,"age":age} 

@app.get("/hello1")
async def hello1(name:str,age:int):
    return {"name":name,"age":age} 