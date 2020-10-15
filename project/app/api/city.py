from fastapi import APIRouter, HTTPException
from typing import List

from app.database import fetch_query_records
from app import schemas

router = APIRouter()

@router.get('/{city_id}')
async def city(city_id: int):
    """
    Returns database entries if given valid city_id 📈
    
    ### Path Parameter
    `city_id`:  int
    Lookup city id can be found [here](https://github.com/Lambda-School-Labs/Labs27-C-Citrics-DS/blob/data/add_citydata.csv/notebooks/citydata.csv) or [here for raw .csv](https://raw.githubusercontent.com/Lambda-School-Labs/Labs27-C-Citrics-DS/data/add_citydata.csv/notebooks/citydata.csv)

    ### Response
    JSON string containing 
    - **city**: [str] . . . standard format city name, state name
    - **pop**: [int] . . . population estimate
    - **age**: [float] . . . average age of residents
    - **income_household**: [int] . . . median household income
    - **income_individual**: [int] . . . median individual income
    - **home**: [int] . . . median home/condo price
    - **COLI**: [float] . . . Cost of Living Index [ACCRA Cost of Living Index](https://en.wikipedia.org/wiki/ACCRA_Cost_of_Living_Index)
    """

    # Validate the city_id
    
    if city_id not in range(1278): 
        raise HTTPException(status_code=404, detail=f'City id {city_id} not found')

    # if city_id valid, establish sql query statement
    query = '''SELECT *
                FROM
                    citydata
                WHERE
                    city_id = (%s);
    '''

    params = (city_id,)

    if query[:8] == 'SELECT *':
        columns = ['city_id',
                    'city',
                    'population',
                    'median_age',
                    'median_household_income',
                    'median_individual_income',
                    'median_home_cost',
                    'median_rent',
                    'Cost-of-Living-Index']
        results = list(fetch_query_records(query, params)[0])
        return dict(zip(columns, results))

    return fetch_query_records(query, params)

#    return df.loc[city_id].to_json(orient='index')  # orient='split', index=False)

@router.get('/all_cities/', response_model=List[schemas.City])
async def get_all_cities():
    '''
    Returns a list of all cities and their stats

    ### Response
    JSON string containing 
    - **city**: [str] . . . standard format city name, state name
    - **pop**: [int] . . . population estimate
    - **age**: [float] . . . average age of residents
    - **income_household**: [int] . . . median household income
    - **income_individual**: [int] . . . median individual income
    - **home**: [int] . . . median home/condo price
    - **rent**: [int] . . . median rent price
    - **COLI**: [float] . . . Cost of Living Index [ACCRA Cost of Living Index](https://en.wikipedia.org/wiki/ACCRA_Cost_of_Living_Index)

    '''
    query = '''SELECT *
                FROM
                    citydata
    '''
    columns = ['city_id',
                    'city',
                    'population',
                    'median_age',
                    'median_household_income',
                    'median_individual_income',
                    'median_home_cost',
                    'median_rent',
                    'Cost_of_Living_Index']
    citydata = fetch_query_records(query)
    results = []
    for i in citydata:
        # uses schema to validate data type
        city_dict = schemas.City(**dict(zip(columns,i)))
        results.append(city_dict)
    return results