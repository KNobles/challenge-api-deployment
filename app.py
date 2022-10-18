from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from property import House
from property import Apartment
from property import Input
app = FastAPI()

@app.get("/")
def root():
    return "Hola"


@app.route("/predict", methods=["GET", "POST"])
def prediction():

    pass

test = House(500, 7033, 4)
apt = Apartment(100, 6000, 1, True)

def testing(item: Input):
    print(jsonable_encoder(item))

testing(test)
testing(apt)