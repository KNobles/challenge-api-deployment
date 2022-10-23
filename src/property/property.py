from pydantic import BaseModel
from typing import Literal, Optional
class Property(BaseModel):
    area: int = 50
    zip_code: int = 2000
    rooms_number: int = 2
    furnished: Optional[bool] = False
    garden: Optional[bool] = False
    garden_area: Optional[int] = None
    equipped_kitchen: Optional[bool] = False
    full_address: Optional[str] = ""
    property_type: str = "HOUSE"
    land_area: Optional[int] = None
    building_state: Optional[Literal[
        "NEW",
        "GOOD",
        "TO_RENOVATE",
        "JUST_RENOVATED",
        "TO_REBUILD"]] = None
    open_fire: Optional[bool] = False
    facades_number: Optional[int] = None
    swimming_pool: Optional[bool] = False
    terrace: Optional[bool] = True
    terrace_area: Optional[int] = 10