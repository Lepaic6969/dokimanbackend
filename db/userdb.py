from typing import Dict, Optional
from pydantic import BaseModel

class UserInDB(BaseModel):
    email: str
    password: str
    name: str
    last_name: str
    department: str
    clearance: int
    documents: Optional [dict] = None
    
database_users = Dict[str,UserInDB]

database_users = {
    "cinthya@example.com" : UserInDB(**{"email": "cinthya@example.com",
                                        "password": "ejemplo123",
                                        "name": "Cinthya",
                                        "last_name":"Murgas",    
                                        "department": "Gerencia",
                                        "clearance" : 5,
                                        "documents":{"Acuerdo de Paz":"https://docs.google.com/acuerdodepaz","Reforma Tributaria":"www.reformatributaria.com"}}),
    "martin@example.com" : UserInDB(**{"email": "martin@example.com",
                                        "password": "ejemplo987",
                                        "name": "Martin",
                                        "last_name":"Vasquez",
                                        "department": "Finanzas",
                                        "clearance": 4,
                                        "documents":{"Acuerdo de Paz":"https://docs.google.com/acuerdodepaz","Reforma Tributaria":"www.reformatributaria.com"}}),
                                        
    "camilo@example.com" : UserInDB(**{"email": "camilo@example.com",
                                        "password": "example345",
                                        "name": "Camilo",
                                        "last_name":"Zamora",    
                                        "department": "Mercadeo",
                                        "clearance": 3,
                                        "documents":{}}),
                                        
    "edwin@example.com" : UserInDB(**{"email": "edwin@example.com",
                                        "password": "example123",
                                        "name": "Edwin",
                                        "last_name":"Gonzalez",    
                                        "department": "Ventas",
                                        "clearance": 2,
                                        "documents":{}}),

}

def get_user(email:str):
    if email in database_users.keys():
        return database_users[email]
    else:
        return None

def update_user(user_in_db: UserInDB):
    database_users[user_in_db.email] = user_in_db
    return user_in_db
    

            