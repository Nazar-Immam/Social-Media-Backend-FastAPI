from fastapi import status , HTTPException, Depends ,APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .. import database , utils , schemas ,models , oauth2
from sqlalchemy.orm import Session


router = APIRouter(
    tags=['Authentication']
)

@router.post("/login")
def user_login(user_credentials : OAuth2PasswordRequestForm = Depends() 
               ,db: Session= Depends(database.get_db) ):

    #search the user with the email,
    user_f = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user_f:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Invalid Credentials")
    
    #now user is found, we need to check the password
    check = utils.verify(user_credentials.password , user_f.password)

    if not check:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= "Invalid Credentials")               

    #now 
    #create a token
    access_token = oauth2.create_access_token(data={"user_id": user_f.id})
    
    return {"access token": access_token, "token_type":"bearer" }

    #return a token