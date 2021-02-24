import logging
import os

DEBUG = os.getenv("DEBUG", None)
log_level = logging.INFO if DEBUG is None else logging.DEBUG

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=log_level, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
