from fastapi import FastAPI
class Data:
    def __init__(self) -> None:
        name = "Pewpew"
        age = 10
        straight = True
        pass

app = FastAPI()

@app.get("/")
def root():
    return "Hola"


@app.route("/predict", methods=["GET", "POST"])
def prediction():

    pass
