from  typing import Union, Annotated
import jwt

from fastapi import FastAPI, Request, Response, HTTPException, Depends, status
from fastapi.responses import FileResponse
from models.models import User
from models.models import Feedback
from models.models import UserCreate
from models.models import SampleProducts
from fastapi.security import HTTPBasic, HTTPBasicCredentials

# user = User(name="John Doe", id=1) #1

security = HTTPBasic()

app = FastAPI()

lst = []

users: list[UserCreate] = []



USER_DATA = [
User(**{"username": "user2", "password": "pass2"}),
User(**{"username": "user1", "password": "pass1"}),
User(**{"username": "user3", "password": "pass3"})
]



# USER_DATA = {
# 1: {"username": "user1", "password": "pass1"},
# 2: {"username": "user2", "password": "pass2"}
# }


fake_users = {
    1: {"username": "john_doe", "email": "john@example.com"},
    2: {"username": "jone_smith", "email": "jone@example.com"}
}

sample_product_1 = {
    "product_id": 123,
    "name": "Smartphone",
    "category": "Electronics",
    "price": 599.99
}

sample_product_2 = {
    "product_id": 456,
    "name": "Phone Case",
    "category": "Accessories",
    "price": 19.99
}

sample_product_3 = {
    "product_id": 789,
    "name": "Iphone",
    "category": "Electronics",
    "price": 1299.99
}

sample_product_4 = {
    "product_id": 101,
    "name": "Headphones",
    "category": "Accessories",
    "price": 99.99
}

sample_product_5 = {
    "product_id": 202,
    "name": "Smartwatch",
    "category": "Electronics",
    "price": 299.99
}

# 4.2 Аутентификация на основе JWT
SECRET_KEY= 'mysectretkey'
def create_jwt_token(data: dict):
    # Функция для создания JWT токена
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM) # кодируем токен, передавая в него наш словарь с тем, что мы хотим там разместить
# Функция получения User'а по токену
def get_user_from_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY,algorithms=[ALGORITHM]) # декодируем токен
        return payload.get("sub")
    except jwt.ExpiredSignatureError:
        pass # тут какая-то логика ошибки истечения срока действия токена
    except jwt.InvalidTokenError:
        pass # тут какая-то логика обработки ошибки декодирования токена
   
# Функция для получения пользовательских данных на основе имени пользователя
def get_user(username: str):
    for user in USER_DATA:
        if user.get("username") == username:
            return user
    return None

# закодируем токен, внеся в него словарь с утверждением о пользователе
token = create_jwt_token({'sub': 'admin'})

print(token)

sample_products = [sample_product_1, sample_product_2, sample_product_3, sample_product_4, sample_product_5]

# декодируем токен и излечем из него информацию о юзере, которую мы туда зашили
username = get_user_from_token(token)

prin(username) # посмотрим, что возвращается то, что ожидаем

current_user = get_user(username) # и теперь пойдем в нашу базу данных искать такого юзера по юзернейму

print(current_user)  # удостоверимся, что нашелся тот, кто нужен

# 4.2 Аутентификация на основе JWT конец

# 4.1 задача логин с защищенной аунтефикацией
# @app.get("/login_security/")



# def authenticate_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
#     return {"username": credentials.username, "password": credentials.password}


def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
# def authenticate_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
        user = get_user_from_db(credentials.username)
        if user is None or user.password != credentials.password:
            # return USER_DATA
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        return user


def get_user_from_db(username: str):
    for user in USER_DATA:
        if user.username == username:
            return user
    return None

@app.get("/protected_resource/")
def get_protected_resource(user: User = Depends(authenticate_user)):
    return {"message": "You got my secret, welcome", "user_info": user}


# конец 4.1 задача логин

@app.get("/product/{product_id}")
def get_product_id(product_id: int):
    for product in sample_products:
        if product["product_id"] == product_id:
            return product
    return{"error": "nochego ne naideno"}

@app.get("/product/")
def return_product(keyword: str, limit: int, category: str = ''):
    for product in sample_products:
        if keyword.lower() in product['name'].lower() and\
                    (category.lower() in product['category'].lower()):
                    product.append(product)
                    return product[:limit]

@app.get("/product/search")
def get_product_search(product_id: int):
    # if limit !=0:
    #     return dict(list(sample_products.items())[:product_id])
    for product in sample_products:
        if product["product_id"] == keyword:
            return product
        # if product["category"] == category:
        #     return product
# keyword
# category
# limit

# Конечная точка получения информации


# задача создать маршрут в систему логин

dbuser = [
    {
        "username":"johndoe",
        "password":"123456",
        "session_token": None
    },
    {
        "username":"janedoe",
        "password":"654321",
        "session_token": None
    }
]
@app.post("/login_1")
async def login_user(user: User, response: Response):
    for u in dbuser:
        if u["username"] == user.username and u["password"] == user.password:
            token = str(random.randint(100, 999))
            u["session_token"] = token
            response.set_cookie(key="session_token", value=token)
            return {"message": "Login successful"}
    return {"message": "Invalid credentinals"}

@app.get("/user")
async def user(request: Request):
    session_token = request.cookies.get("session_token")
    for u in dbuser:
        if u["session_token"] == request.cookies.get("session_token") is not None:
            return {"username": u["username"]}
        return {"message": "Invalid session"}

# ---------

@app.get("/users/{user_id}")
def read_user(user_id: int):
    if user_id in fake_users:
        return fake_users[user_id]
    return{"error": "User not found"}


@app.get("/users/")
def read_users(limit: int=10):
    return dict(list(fake_users.items())[:limit])

@app.post("/feedback")
def feedback_return(feedback: Feedback):
    lst.append({"name": feedback.name, "comments": feedback.message})

    # my_feedback_data: Feedback = Feedback(**second_feedback_data)
    return f"Feedback received. Thank you, {feedback.name}!"

@app.get("/comments")
async def show_feedback():
    return lst

@app.post("/create_user")
def user_return(usercreate: UserCreate):
    users.append(usercreate)
    return usercreate

@app.get("/show_user")
async def show_users():
    return {"users": users}
# @app.post("/feedback")
# def feedback_return(names: str, message: str):
#     # feedback = Feedback(name=names,message=message)
#     # second_feedback_data = {
#     #     "name": name,
#     #     "message": message
#     # }
#     return "Feedback received. Thank you, " + name + " !"

#num1 = 10
#num2 = 5

# @app.get("/")
# def read_root():
#     return {"message": "Hello, world!"}
#
# # новый роут
# @app.get("/custom")
# def read_custom_message():
#     return {"message": "This is a custom message!"}
#
#
# # #1
# # @app.get("/users", response_model=User)
# # def user_root():
# #     return user
#

#
# @app.get("/users")
# def user():
#
#     second_user_data = {
#         "id": 1,
#         "name": "John Doe",
#         "is_adult": True
#     }
#
#     my_second_user: User = User(**second_user_data)
#     return my_second_user
#
#
# @app.post("/users")
# def user(age: int):
#     # is_adult = True
#     if age < 18:
#         is_adult = False
#     else:
#         is_adult = True
#
#     second_user_data = {
#         "id": 1,
#         "name": "Michle",
#         "is_adult": is_adult
#     }
#
#     my_second_user: User = User(**second_user_data)
#     return my_second_user

# @app.post('/calculate')
# def calculate(num1: int, num2: int):
#    return {f'sum of numbers {num1} and {num2} is': f'{num1+num2}'}

# @app.get('/')

#    return FileResponse('index.html')
# async def root():
#    return {"message": "Hello World"}
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#    return {"item_id": item_id, "q": q}
