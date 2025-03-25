import logging
import importlib
from .cleaner import clean_text
from .counter import word_count

__all__ = ['clean_text','word_count']

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("textutils package initialized")

#na żądanie ladowanie dodatkowych modułów
def load_extra(name):
    return importlib.import_module(f'.{name}',package=__name__)

class TextProcessor:
    def process(self,text):
        return text.lower()

processor = TextProcessor()
