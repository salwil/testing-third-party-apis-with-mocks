
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

# with this decorator we can overwrite response parameters of the get-method from the requests library,
# which is called inside the get_todos method
@patch('src.services.requests.get')
def test_get_todos_with_decorator_patch(mock_get):
    # Configure the mock to return a response with an OK status code. Note that this line is actually not needed for
    # the assertions in this test, because the decorator already instantiates the response as a MagicMock object
    # --> response is not None (this just leads to the ok property being explicitly true)
    mock_get.return_value.ok = True

    # Call the service, which will send a request to the server.
    response = get_todos()

    # If the request is sent successfully, then I expect a response to be returned.
    assert_is_not_none(response)

@patch('src.services.requests.get')
def test_get_todos_with_decorator_patch_when_response_is_not_ok(mock_get):
    # Configure the mock to not return a response with an OK status code.
    mock_get.return_value.ok = False

    # Call the service, which will send a request to the server.
    response = get_todos()

    # If the response contains an error, I should get no todos.
    assert_is_none(response)

# we can also patch a function with the context manager instead of using a decorator. This is especially helpful, when
# some of the code in the test function uses a mock and other code references the actual function.
def test_get_todos_with_context_manager_patch():
    with patch('src.services.requests.get') as mock_get:
        # Configure the mock to return a response with an OK status code.
        # mock_get.return_value.ok = True

        # Call the service, which will send a request to the server.
        response = get_todos()

    # If the request is sent successfully, then I expect a response to be returned.
    assert_is_not_none(response)

def test_get_todos_with_patcher_patch():
    mock_get_patcher = patch('src.services.requests.get')

    # Start patching `requests.get`.
    mock_get = mock_get_patcher.start()

    # Configure the mock to return a response with an OK status code.
    mock_get.return_value.ok = True

    # Call the service, which will send a request to the server.
    response = get_todos()

    # Stop patching `requests.get`.
    mock_get_patcher.stop()

    # If the request is sent successfully, then I expect a response to be returned.
    assert_is_not_none(response)

from nose.tools import assert_is_none, assert_list_equal
@patch('src.services.requests.get')
def test_get_todos_with_mocked_data(mock_get):
    todos = [{
        'userId': 1,
        'id': 1,
        'title': 'Make the bed',
        'completed': False
    }]

    # Configure the mock to return a response with an OK status code. Also, the mock should have
    # a `json()` method that returns a list of todos.
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = todos

    # Call the service, which will send a request to the server.
    response = get_todos()

    # If the request is sent successfully, then I expect a response to be returned.
    assert_list_equal(response.json(), todos)
