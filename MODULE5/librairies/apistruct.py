from pydantic import BaseModel


class DeviseBase(BaseModel):
    devise: str
    achat: float
    vente: float
    new_devise: float
    xof_conversion: float
    pays: str
    flag: str



class DeviseCreate(DeviseBase):
    pass


class Devise(DeviseBase):
    id: int
    devise: str
    achat: float
    vente: float
    new_devise: float
    xof_conversion: float
    pays: str
    flag: str

    class Config:
        orm_mode = True