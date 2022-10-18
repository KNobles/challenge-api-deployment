from typing import Optional
from abc import ABC, abstractmethod


class Property(ABC):
    @abstractmethod
    def __init__(
        self,
        area: int,
        zip_code: int,
        rooms_number: int,
        furnished: Optional[bool],
        garden: Optional[bool],
        garden_area: Optional[int],
        equipped_kitchen: Optional[bool],
        land_area: Optional[int],
        building_state: Optional[list[str]],
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
        furnished: Optional[bool],
        garden: Optional[bool],
        garden_area: Optional[int],
        equipped_kitchen: Optional[bool],
        land_area: Optional[int],
        building_state: Optional[list[str]],
        open_fire: Optional[bool],
        facades_number: Optional[int],
        swimming_pool: Optional[bool],
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
        self.open_fire = open_fire
        self.facades_number = facades_number
        self.swimming_pool = swimming_pool


class Apartment(Property):
    def __init__(
        self,
        area: int,
        zip_code: int,
        rooms_number: int,
        furnished: Optional[bool],
        garden: Optional[bool],
        garden_area: Optional[int],
        equipped_kitchen: Optional[bool],
        land_area: Optional[int],
        building_state: Optional[list[str]],
        terrace: Optional[bool],
        terrace_area: Optional[int],
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
        self.terrace = terrace
        self.terrace_area = terrace_area

