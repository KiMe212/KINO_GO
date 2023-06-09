from fastapi import APIRouter

from app.auth.auth_handler import signJWT, decodeJWT
from app.schemas import User, SignUp
from app.services import add_user_for_db, check_user, check_password_signup, check_email

router = APIRouter()


@router.post("/sign_up")
def sign_up(user: User):
    if check_email(user.email):
        token = signJWT(user.password)
        user.password = token
        status = add_user_for_db(user)
    else:
        return {"status": "This email is taken, try again"}
    return {"status": status}


@router.post("/sign_in")
def sign_in(user: SignUp):
    data_of_user = check_user(user)
    payload = decodeJWT(data_of_user[2])
    status = check_password_signup(user.password, payload['user_id'])
    return {"status": status}

