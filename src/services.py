# Standard library imports...
from urllib.parse import urljoin

# Third-party imports...
import requests

# Local imports...
from src.constants import BASE_URL

TODOS_URL = urljoin(BASE_URL, 'todos')

def get_todos():
    response = requests.get(TODOS_URL)
    if response.ok:
        return response
    else:
        return None