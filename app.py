from fastapi import FastAPI, Request, HTTPException,Response,status
import uuid
from pydantic import BaseModel
app=FastAPI()

tanks=[
 
]



@app.get("/tank")
def get_tanks():
    return tanks

@app.get("/tank/{id}")
def get_tank_id(id:str):
    tank_index=0
    
    for i in range(len(tanks)):
        if tanks[i]["id"]== id:
            return{i}

@app.post("/tank")
async def alter_thing(request:Request, response:Response):
    tank= await request.json()
    new_uuid = uuid.uuid4()
    tank['id'] = str(new_uuid)
    tanks.append(tank)
    response.status_code=status.HTTP_201_CREATED
    #raise HTTPException(status_code=201, detail= "tank with id:"+ "not found")
    return tank

@app.delete("/tank/{id}")
def delete_tank(id:str):
    tank_index=0

    for i in range(len(tanks)):
        if tanks[i]["id"]== id:
            tank_index=i
            break
    del tanks[tank_index]

    return{
        "message":"tank deleted"
    }




