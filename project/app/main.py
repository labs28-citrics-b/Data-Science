from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.api import city  # predict, viz

app = FastAPI(
    title='Citrics DS API',
    description='Returns city metrics on a per-city basis, provided unique city_id . . . 🌇📈📊📉⛅',
    version='0.1',
    docs_url='/',
)

# app.include_router(predict.router)
# app.include_router(viz.router)
app.include_router(city.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    uvicorn.run(app)
