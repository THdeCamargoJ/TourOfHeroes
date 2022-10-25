from pydantic import BaseModel



class HeroBase(BaseModel):
    name: str


class HeroCreate(HeroBase):
    pass


class HeroUpdate(HeroBase):
    pass


class HeroDelete(HeroBase):
    pass


class HeroSearch(HeroBase):
    pass


class Hero(HeroBase):
    id: int

    class Config:
        orm_mode = True

