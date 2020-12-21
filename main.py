import datetime
from fastapi import FastAPI
from fastapi import HTTPException

from db.userdb import UserInDB
from db.userdb import database_users
from db.userdb import update_user, get_user
from models.usermodel import UserIn, UserOut,UserAuth,UserUpdatePassword,data

api = FastAPI()

##########################################################################################
from fastapi.middleware.cors import CORSMiddleware
origins = [
"http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
"http://localhost", "http://localhost:8080","http://localhost:8081","https://dokimanapp.herokuapp.com",
]
api.add_middleware(
CORSMiddleware, allow_origins=origins,
allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)


##########################################################################################

@api.get("/")
async def home():
    return{"message":"Dokiman: File Management"}

@api.post("/user/login/")
async def login(user_in: UserIn):
    user_in_db = get_user(user_in.email)
    if user_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    if user_in_db.password != user_in.password:
        return {"Autenticado": False}
    return {"Autenticado": True}

@api.get("/user/data/")
async def get_document(datos:data):
    user_in_db = get_user(datos.email)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    user_out = UserOut(**user_in_db.dict())
    return user_out

@api.post("/user/signup/")
async def create_user(new_user: UserInDB):
    new_key = get_user(new_user.email)
    if new_key != None:
        raise HTTPException(status_code=409, detail="Este usuario ya existe")
    database_users[new_user.email]= new_user
    user_auth = UserAuth(**new_user.dict())
    return {"mensaje": "Usuario creado exitosamente", "usuario": user_auth}


@api.put("/user/update/")
async def update(user_in:UserUpdatePassword):
    user_in_db=get_user(user_in.email)
    if user_in_db==None:
        raise HTTPException(status_code=404,
                           detail="El usuariono no existe")
    if user_in_db.password != user_in.password:
        raise HTTPException(status_code=400,
                            detail="La clave del usuario es incorrecta")
        return  {"password":"incorrecta"}
    
    user_in_db.password=user_in.new_password
    update_user(user_in_db)
    return  {"password":"actualizada"}