from fastapi import  status , HTTPException, Depends , APIRouter
from .. import schemas , models , utils
from ..database import get_db
from sqlalchemy.orm import Session

#PATH OPERATION TO CREATE A NEW USER IN USERS TABLE

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.post("/" ,status_code=status.HTTP_201_CREATED, response_model= schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    
    #hash the password - user.password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

#To retrieve or fetch a user by id
@router.get("/{id}", status_code=status.HTTP_200_OK , response_model=schemas.UserResponse)
def get_user(id: int ,  db: Session = Depends(get_db)):
    data = db.query(models.User).filter(models.User.id == id).first()
    

    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id={id} does not exist ! ")
    return data