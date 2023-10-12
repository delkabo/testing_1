from  typing import Union

from fastapi import FastAPI
from fastapi.responses import FileResponse
from models.models import User
from models.models import Feedback
from models.models import UserCreate
from models.models import SampleProducts

# user = User(name="John Doe", id=1) #1

app = FastAPI()

lst = []

users: list[UserCreate] = []

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

sample_products = [sample_product_1, sample_product_2, sample_product_3, sample_product_4, sample_product_5]


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
