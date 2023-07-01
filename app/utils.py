from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    """takes in a string or characters and runs them through an algorithm to create a hash

    Args:
        password (str): password from the user in string format

    Returns:
        _type_: str
    """
    return pwd_context.hash(password)

def verify_password(password: str, hashed_password: str):
    """takes in a password and a hashed password and compares them

    Args:
        password (str): the password user is using to login
        hashed_password (str): the password that is stored in the database

    Returns:
        _type_: bool
    """
    return pwd_context.verify(password, hashed_password)