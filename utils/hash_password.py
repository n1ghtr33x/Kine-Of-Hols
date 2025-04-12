import hashlib


async def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

async def verify_password(plain_password: str, hashed_password: str) -> bool:
    return await hash_password(plain_password) == hashed_password
