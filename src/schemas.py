from pydantic import BaseModel

class _PostRegiter(BaseModel):
    field_1: str
    author: str
    description: str
    my_numeric_field: int

class _GetRegiter(BaseModel):
    id: int
    field_1: str
    author: str
    description: str
    my_numeric_field: int

class _ReturnId(BaseModel):
    id: int