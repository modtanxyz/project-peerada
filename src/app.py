def login(username, password):
    if  username == "admin" and \
        password == "secure_pw":
        return "Login Success"
    return "Login Failed"
