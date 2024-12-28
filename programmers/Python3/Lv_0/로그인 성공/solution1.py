def solution(id_pw, db):
    pw_error = False
    for user in db:
        if user[0] == id_pw[0]:
            if user[1] == id_pw[1]:
                return "login"
            else:
                pw_error = True
    if pw_error:
        return "wrong pw"
    else:
        return "fail"
        