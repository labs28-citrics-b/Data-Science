from pydantic import BaseModel

class City(BaseModel):
    city_id: int
    city: str
    population: int
    median_age: float
    median_household_income: int
    median_individual_income: int
    median_home_cost: int
    median_rent: float
    Cost_of_Living_Index: float
