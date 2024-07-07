from fastapi import FastAPI
from pydantic import BaseModel
import math

class Math(BaseModel):
    number: float
    
app=FastAPI()

@app.get('/')
def home_page():
    return {'welcome'}

@app.post('/math')
def cal_math(data: Math): 
    i=float(data.number)
    sq=math.pow(i,2)
    cube=i*i*i
    sqroot=math.sqrt(i)
    #cube_root=math.cbrt(i)
    log_value=math.log(i)
    mathx={"square": sq, "cube": cube, "square root": sqroot, "log value": log_value}
    return mathx
    
    
