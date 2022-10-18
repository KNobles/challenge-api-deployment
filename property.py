from typing import Optional
from abc import ABC, abstractmethod


class Property(ABC):
    @abstractmethod
    def __init__(
        self,
        area: int,
        zip_code: int,
        rooms_number: int,
        furnished: Optional[bool] = None,
        garden: Optional[bool] = None,
        garden_area: Optional[int] = None,
        equipped_kitchen: Optional[bool] = None,
        land_area: Optional[int] = None,
        building_state: Optional[str] = None,
    ) -> None:

        self.area = area
        self.zip_code = zip_code
        self.room_number = rooms_number
        self.furnished = furnished
        self.land_area = land_area
        self.building_state = building_state


class House(Property):
    def __init__(
        self,
        area: int,
        zip_code: int,
        rooms_number: int,
        furnished: Optional[bool] = None,
        garden: Optional[bool] = None,
        garden_area: Optional[int] = None,
        equipped_kitchen: Optional[bool] = None,
        land_area: Optional[int] = None,
        building_state: Optional[str] = None,
        open_fire: Optional[bool] = None,
        facades_number: Optional[int] = None,
        swimming_pool: Optional[bool] = None,
    ) -> None:

        super().__init__(
            area,
            zip_code,
            rooms_number,
            furnished,
            garden,
            garden_area,
            equipped_kitchen,
            land_area,
            building_state,
        )
        self.property_type = "HOUSE"
        self.open_fire = open_fire
        self.facades_number = facades_number
        self.swimming_pool = swimming_pool


class Apartment(Property):
    def __init__(
        self,
        area: int,
        zip_code: int,
        rooms_number: int,
        furnished: Optional[bool] = None,
        garden: Optional[bool] = None,
        garden_area: Optional[int] = None,
        equipped_kitchen: Optional[bool] = None,
        land_area: Optional[int] = None,
        building_state: Optional[str] = None,
        terrace: Optional[bool] = None,
        terrace_area: Optional[int] = None,
    ) -> None:

        super().__init__(
            area,
            zip_code,
            rooms_number,
            furnished,
            garden,
            garden_area,
            equipped_kitchen,
            land_area,
            building_state,
        )
        self.property_type = "APARTMENT"
        self.terrace = terrace
        self.terrace_area = terrace_area

class Input(Property):
    data: House | Apartment