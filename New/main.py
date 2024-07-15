from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def index():
    return {"message": "Hello World"}

#Path parameter

#Single parameters
# @app.get("/hello/{name}")
# async def hello(name):
#     return {"name":name} 

# #Multiple parameter
# @app.get("/hello/{name}/{age}")
# async def hello(name,age):
#     return {"name":name,"age":age} 


#Query Parameter
# http://localhost:8000/hello?name=ravi&age=30
@app.get("/hello")
async def hello(name:str,age:int):
    return {"name":name,"age":age} 