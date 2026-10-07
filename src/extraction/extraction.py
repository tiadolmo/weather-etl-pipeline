import requests
import pandas as pd
from src.config.api_config import api_settings
import logging


# log configuration
logging.basicConfig(
    level = logging.INFO, format = "%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/extraction.log"),  # log directory location
        logging.StreamHandler(),  
    ],
)
logger = logging.getLogger(__name__)


def get_data(api_key, city):
    url = f"https://api.tomorrow.io/v4/weather/forecast?location={city}"
    headers = {
        "accept-encoding" : "deflate, gzip, br",
        "accept" : "application/json"
    }
    params = {
        "apikey" : api_key
    }

    try:
        response = requests.get(url=url, headers = headers, params = params )
    
        if response.status_code == 200:
            response_data = response.json()
            # print(response_data)
            raw_data = response_data["timelines"]["minutely"]
            # print(report_date)
            df = pd.json_normalize(raw_data)
            print(df)
            logger.info(f"Successfully fetched a weather data for {city}. Rows: {len(df)}"        )
            return df

    except requests.RequestException as e:
        logger.error(f"API request failed: {e}")
        return None
    except (KeyError, ValueError) as e:
        logger.error(f"Failed to parse JSON structure from response: {e}")
        return None

if __name__ == "__main__":

    api_key = api_settings.tomorrow_api_key.get_secret_value()
    # print("Checking api key null or not :", bool(api_key))
    logger.info(f"API key is loaded successfully: {bool(api_key)}")

    city = "kathmandu"

    get_data(api_key, city)
