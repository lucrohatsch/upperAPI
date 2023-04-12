from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from db_conect import create_db, session_db
from model import Registers
from schemas import _GetRegiter, _PostRegiter, _ReturnId
import os
import logging

app = FastAPI()
create_db()

oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")

#
@app.post("/token")
async def token_generator(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Verifica que el usuario sea el configurado en el ambiente.
    En caso de ser correcto genera un token para el resto de las urls
    """
    if form_data.username == os.getenv("USR") and form_data.password == os.getenv("PSW"):
        return {"acccess_token": form_data.username, "token_type": "bearer"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

@app.post("/input/{my_target_field}", response_model=_ReturnId)
def read_root(register: _PostRegiter, my_target_field: str, token: str = Depends(oauth_scheme)):
    """
    Recibe un json y un campo a modificar
    Modifca el campo a mayusculas y guarda en base de datos
    deviuelve el id en la base de datos
    """
    register = register.__dict__
    if my_target_field in register and my_target_field != "my_numeric_field":
        register[my_target_field]=register[my_target_field].upper()
        deb_register = Registers(**register)
        ss = session_db()
        ss.add(deb_register)
        ss.commit()
        ss.refresh(deb_register)
        result={"id":deb_register.id}
        logging.info(result)
        return {"id":deb_register.id}
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(f"El campo '{my_target_field}' no es válido para convertir a mayúscula"),
            headers={"WWW-Authenticate": "Bearer"},
        )


@app.get("/get_data/{id}", response_model=_GetRegiter)
def get_data(id:int,token: str = Depends(oauth_scheme)):
    """
    Busca en BD y devuelve el registro correspondiente al id
    """
    ss = session_db()
    register = ss.query(Registers).filter(Registers.id == id).first()
    print(register)
    if register is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=(f"El id {id} no existe"),
            headers={"WWW-Authenticate": "Bearer"},
        )
    return register.__dict__
