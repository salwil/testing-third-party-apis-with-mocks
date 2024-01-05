from unittest.mock import patch, Mock

from nose.tools import assert_is_none, assert_list_equal

from src.services import get_todos


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