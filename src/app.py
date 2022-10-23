from fastapi import FastAPI
from property.property import Property
from predict.prediction import predict
from preprocessing.cleaning_data import preprocess

app = FastAPI()

@app.get("/")
def root():
    return "Alive"

@app.post("/predict")
async def price_predict(item: Property):
    prep = preprocess(item)
    print(prep)
    pred = predict(prep)
    return pred

@app.get('/predict')
async def explain():
    """
    GET request returning a string to explain what the POST expect (data and format).
    """
    return('''
    This model is takes the next information as an input:
    area: int
    property_type: str #"APARTMENT" | "HOUSE" | "OTHERS",
    rooms_number: int
    zip_code: int
    land_area: int | None #Optional[int]
    garden: bool | None #Optional[bool],
    garden_area: int | None #Optional[int],
    equipped_kitchen: bool | None #Optional[bool],
    full_address: str | None #Optional[str],
    swimming_pool: bool | None #Optional[bool],
    furnished: bool | None #Optional[bool],
    open_fire: bool | None #Optional[bool],
    terrace: bool | None #Optional[bool],
    terrace_area: int | None #Optional[int],
    facades_number: int | None #Optional[int],
    building_state: str | None # Optional["NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"]
    ''')