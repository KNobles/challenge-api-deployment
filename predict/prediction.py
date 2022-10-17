from typing import Optional



class Property:

    def __init__(self, area:int, rooms_number:int, furnished:Optional[bool], 
    garden:Optional[bool], garden_area:Optional[int], equipped_kitchen:Optional[bool], 
    land_area:Optional[int], building_state:Optional[list[str]], ) -> None:
        
        pass

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