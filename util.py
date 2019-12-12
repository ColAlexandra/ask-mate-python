import bcrypt


def hash_password(password_text):
    # By using bcrypt, the salt is saved into the hash itself
    hashed_pw = bcrypt.hashpw(password_text.encode('utf-8'), bcrypt.gensalt())
    return hashed_pw.decode('utf-8')


