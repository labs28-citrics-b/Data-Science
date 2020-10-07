from fastapi import APIRouter, HTTPException
import pandas as pd

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
    # city_ids = json.load(i
    # with open(os.path.join(path, 'city_ids.json'), 'r') as f:
    
    city_ids = pd.read_csv('/usr/src/app/city_id_lookup.csv')
    
    if city_id not in range(1278): 
        raise HTTPException(status_code=404, detail=f'City id {city_id} not found')

    # pull in preliminary dataframe
    df = pd.read_csv('citydata.csv', index_col='city_id') 

#     # Make Plotly figure
#     statename = statecodes[statecode]
#     fig = px.line(df, x='Date', y='Percent', title=f'{statename} Unemployment Rate')
# 
#     # Return Plotly figure as JSON string
#     return fig.to_json()

    return df.loc[city_id].to_json(orient='index')  # orient='split', index=False)

