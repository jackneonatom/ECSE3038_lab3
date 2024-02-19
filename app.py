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
async def get_tank_id(id:str):
    
    for i in tanks:
        if i["id"]== id:
                
            return i
    raise HTTPException(status_code=404, detail= "tank no find")

@app.post("/tank")
async def alter_thing(request:Request, response:Response):
    tank= await request.json()
    new_uuid = uuid.uuid4()
    tank['id'] = str(new_uuid)
    tanks.append(tank)
    response.status_code=status.HTTP_201_CREATED
    # raise HTTPException(status_code=201, detail= "tank with id:"+ "not found")
    return tank

@app.patch("/tank/{id}")
async def patch_tank(id: str, request:Request):
    patched_tank = await request.json()

    for i, tank in enumerate(tanks):
        if tank["id"] == id:
            patched_tank.pop("id", None)  # Remove the ID from the patched data
            tanks[i] = {**tank, **patched_tank}
            return tanks[i]
    raise HTTPException(status_code=404, detail="Tank not found :/")



@app.delete("/tank/{id}")
def delete_tank(id: str, response: Response):

    for i in range(len(tanks)):
        if tanks[i]["id"] == id:
            del tanks[i]
            response.status_code = status.HTTP_204_NO_CONTENT
            return()
    
    raise HTTPException(status_code=404, detail="tank no find  :/")
