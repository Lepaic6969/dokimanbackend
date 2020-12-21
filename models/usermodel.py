from pydantic import BaseModel

class UserIn(BaseModel):
    email: str
    password: str


class UserOut(BaseModel):
    name: str
    last_name: str
    department: str
    clearance : int
    documents : dict          

    
class UserAuth(BaseModel):
    name: str
    last_name: str        

class UserUpdatePassword(BaseModel):
    email: str
    password: str
    new_password:str      

class data(BaseModel):
    email:str