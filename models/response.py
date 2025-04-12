from pydantic import BaseModel

class UserData(BaseModel):
    id: str
    name: str
    elixir: int
    gold: int
    gems: int

class LoginResponseSuccess(BaseModel):
    status: str
    data: UserData

class LoginResponseFail(BaseModel):
    status: str
    data: str

async def login_success(data: UserData):
    return LoginResponseSuccess(
        status='success',
        data=data
    )

async def login_fail(data: str):
    return LoginResponseFail(
        status="fail",
        data=data
    )