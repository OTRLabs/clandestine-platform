import bcrypt

class Hashing:
    def __init__(self):
        pass

    async def hash_with_bcrypt(self, password):
        try:
            salt = await self.generate_salt()
            hashed_password = await self.hash_password(password, salt)
            return hashed_password.decode()
        except Exception as e:
            # Handle any specific exceptions here
            raise e

    async def verify_with_bcrypt(self, password, hashed):
        try:
            return await self.check_password(password, hashed)
        except Exception as e:
            # Handle any specific exceptions here
            raise e

    async def generate_salt(self):
        try:
            return await bcrypt.gensalt()
        except Exception as e:
            # Handle any specific exceptions here
            raise e

    async def hash_password(self, password, salt):
        try:
            return await bcrypt.hashpw(password.encode(), salt)
        except Exception as e:
            # Handle any specific exceptions here
            raise e

    async def check_password(self, password, hashed):
        try:
            return await bcrypt.checkpw(password.encode(), hashed.encode())
        except Exception as e:
            # Handle any specific exceptions here
            raise e