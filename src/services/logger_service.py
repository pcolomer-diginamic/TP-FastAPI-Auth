#TP Vuln
#Logger et gestion exceptions HTTP 
import logging
from fastapi import HTTPException, status


def get_logger():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", handlers=[ logging.StreamHandler(), logging.FileHandler("app.log")])
    #setup_logging()
    logger = logging.getLogger(__name__)
    yield logger