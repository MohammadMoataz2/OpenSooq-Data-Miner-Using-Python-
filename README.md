# OpenSooq Data Miner (Using Python)

OpenSooq Data Miner is a web application designed to scrape data from OpenSooq, an online marketplace, based on user-defined parameters such as category URL and number of pages to scrape using python. The application sends the scraped data to an API server, which processes the data using Python scripts with BeautifulSoup and requests libraries. The scraped data is then stored in a CSV file, which users can download and preview.
![Blue and Yellow Modern Data Analysis Presentation (1)](https://github.com/MohammadMoataz2/Diabetes-Insight-and-Model-Mastery-with-KNIME-and-python/assets/123085286/80056d8c-b27b-4feb-a8d8-f3b386508502)
## Features

- **Customizable Scraping**: Users can specify the category URL and the number of pages to scrape data from.
- **API Integration**: Data scraped from OpenSooq is sent to an API server for processing.
- **Scraping with BeautifulSoup**: Python scripts utilize BeautifulSoup library to scrape data from web pages.
- **CSV Export**: Scraped data is stored in a CSV file format for easy download and preview.

## Usage
![image](https://github.com/MohammadMoataz2/Diabetes-Insight-and-Model-Mastery-with-KNIME-and-python/assets/123085286/3761570a-5153-4568-b2f6-14d2e903cfe3)
1. **Input Parameters**: Users provide the category URL and specify the number of pages to scrape on the web page.

![image](https://github.com/MohammadMoataz2/Diabetes-Insight-and-Model-Mastery-with-KNIME-and-python/assets/123085286/54f3933b-3431-49dd-9ed1-196e5391d1f2)
2. **Scraping Process**: When the user presses the button, the web application sends the data to the API server.


3. **Data Scraping**: Python scripts on the API server utilize BeautifulSoup and requests libraries to scrape data from OpenSooq.


4. **CSV Generation**: The scraped data is then stored in a CSV file format.


5. **Download and Preview**: Users can download the CSV file containing the scraped data and preview it.
![image](https://github.com/MohammadMoataz2/Diabetes-Insight-and-Model-Mastery-with-KNIME-and-python/assets/123085286/f132c6bd-c5b2-4624-96dd-b3909e6f98a8)
## Technologies Used

- **Python**: Used for scripting and backend data processing.
- **FastAPI**: Web framework for developing API for Applcation.
- **BeautifulSoup**: Python library for web scraping.
- **Requests**: Python library for making HTTP requests.
- **CSV**: File format used for storing scraped data.
- **HTML/CSS/JavaScript**: Frontend technologies for building the user interface.

## Getting Started

To get started with OpenSooq Data Miner, follow these steps:

1. Clone the repository to your local machine.
2. Install the necessary dependencies by running `pip install -r requirements.txt`.
3. Run the FastAPI application using `python -m uvicorn os_scarper_fastapi:app --reload`.
4. Access the application through your web browser and start scraping data from OpenSooq.


## Contributing
Contributions to this repository are welcome!

