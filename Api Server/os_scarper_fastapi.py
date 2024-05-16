from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import FileResponse
import os
from os_scraper_py import open_souq_scraping

app = FastAPI()

# CORS configuration
origins = [
    "http://localhost",
    'http://127.0.0.1:5501',
    'http://127.0.0.1:5502',
    'http://127.0.0.1:5500',
    

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


#uvicorn os_scarper_fastapi:app --reload

class Scraping_URL_Page(BaseModel):
    url: str
    page : int




@app.post("/scarper/")
async def scarper_df(data: Scraping_URL_Page):
    try:
        print(type(data))
        url = data.url
        page = data.page

        print("Data before ETL:", url, page)
        print("_________")
        scraping_df, scraping_json = open_souq_scraping(url, page)
        print("_________")
        print(scraping_df)
        print(scraping_json)

  

        return {"scraping_json": "http://127.0.0.1:8000/apa_test.csv"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@app.get("/apa_test.csv")
async def get_csv_file():
    file_path = "apa_test.csv"

    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="text/csv")
    else:
        raise HTTPException(status_code=404, detail="CSV file not found")