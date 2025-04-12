import random
import string

async def generate_unique_id(db, max_attempts=10, length=6):
    for _ in range(max_attempts):
        new_id = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        if not await db.user_exists_by_id(new_id):
            return new_id
    raise Exception("Не удалось сгенерировать уникальный ID")
