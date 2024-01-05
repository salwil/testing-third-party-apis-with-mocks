
from nose.tools import assert_true
from nose.tools import assert_is_not_none
import requests


def test_request_response():
    # Send a request to the API server and store the response.
    response = requests.get('http://jsonplaceholder.typicode.com/todos')

    # Confirm that the request-response cycle completed successfully.
    assert_true(response.ok)
    # If the request is sent successfully, then I expect a response to be returned.
    assert_is_not_none(response)