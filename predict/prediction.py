from typing import Optional
from abc import ABC, abstractmethod


class Property(ABC):

    @abstractmethod
    def __init__(self, area: int, zip_code: int, rooms_number: int, furnished: Optional[bool], 
    garden: Optional[bool], garden_area: Optional[int], equipped_kitchen: Optional[bool], 
    land_area: Optional[int], building_state: Optional[list[str]]) -> None:
        self.area = area
        self.room_number = rooms_number
        self.furnished = furnished
        self.land_area = land_area
        self.building_state = building_state

class House(Property):

    def __init__(self, area: int, rooms_number: int, furnished: Optional[bool],
    garden: Optional[bool], garden_area: Optional[int], equipped_kitchen: Optional[bool],
    land_area: Optional[int], building_state: Optional[list[str]], open_fire: Optional[bool],
    facades_number: Optional[int], swimming_pool: Optional[bool]) -> None:
        super().__init__(area, rooms_number, furnished, garden, garden_area,
        equipped_kitchen, land_area, building_state)


# input_data = {
#   "data": {
#     "area":int,
#     "property-type": "APARTMENT" | "HOUSE" | "OTHERS",
#     "rooms-number": int,
#     "zip-code": int,
#     "land-area": Optional[int],
#     "garden": Optional[bool],
#     "garden-area": Optional[int],
#     "equipped-kitchen": Optional[bool],
#     "full-address": Optional[str],
#     "swimming-pool": Optional[bool],
#     "furnished": Optional[bool],
#     "open-fire": Optional[bool],
#     "terrace": Optional[bool],
#     "terrace-area": Optional[int],
#     "facades-number": Optional[int],
#     "building-state": Optional[
#       "NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"
#     ]
#   }
# }