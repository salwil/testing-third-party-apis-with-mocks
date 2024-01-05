
from nose.tools import assert_true
from nose.tools import assert_is_not_none
import requests

"""
First, we just write a simple nose test to confirm the life of the server. 
We're only concerned with whether the server returns an OK response.
"""
def test_request_response_direct():
    # Send a request to the API server and store the response.
    response = requests.get('http://jsonplaceholder.typicode.com/todos')

    # Confirm that the request-response cycle completed successfully.
    assert_true(response.ok)

"""
Now we test the get_todos function which itself does a request to the above URL
"""
def test_get_todos():
    response = get_todos()
    # If the request is sent successfully, then I expect a response to be returned.
    assert_is_not_none(response)
    # Obviously we still expect the same response code as if we do the call inside the test directly (ok, 200)
    assert_true(response.ok)

"""
With the above test we still access the external API by calling get_todos(). Below we detach our programming logic from
the actual external API by swapping the real request with a fake one that returns the same data.
"""

from unittest.mock import Mock, patch

from nose.tools import assert_is_not_none
from nose.tools import assert_is_none

from src.services import get_todos
@patch('src.services.requests.get')
def test_get_todos_with_mock(mock_get):
    # Configure the mock to return a response with an OK status code.
    mock_get.return_value.ok = True

    # Call the service, which will send a request to the server.
    response = get_todos()

    # If the request is sent successfully, then I expect a response to be returned.
    assert_is_not_none(response)