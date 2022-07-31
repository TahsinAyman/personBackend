import hashlib
from models import *

try:
    user = input("Enter Your User: ")
    password = input("Enter Your Password: ")
    token = hashlib.md5((user + password).encode()).hexdigest()

    auth = Authentication(token=token, name=user)
    db.session.add(auth)
    db.session.commit()

    print(f"Note: Your Authentication Token is {token}")
except Exception:
    print("Couldn't Add Access")
    
