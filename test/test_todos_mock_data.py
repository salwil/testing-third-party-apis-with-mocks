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

@patch('src.services.requests.get')
def test_getting_todos_when_response_is_not_ok(mock_get):
    # Configure the mock to not return a response with an OK status code.
    mock_get.return_value.ok = False

    # Call the service, which will send a request to the server.
    response = get_todos()

    # If the response contains an error, I should get no todos.
    assert_is_none(response)


@patch('src.services.get_todos')
def test_getting_uncompleted_todos_when_todos_is_not_none(mock_get_todos):
    todo1 = {
        'userId': 1,
        'id': 1,
        'title': 'Make the bed',
        'completed': False
    }
    todo2 = {
        'userId': 1,
        'id': 2,
        'title': 'Walk the dog',
        'completed': True
    }

    # Configure mock to return a response with a JSON-serialized list of todos.
    mock_get_todos.return_value = Mock()
    mock_get_todos.return_value.json.return_value = [todo1, todo2]

    # Call the service, which will get a list of todos filtered on completed.
    uncompleted_todos = get_uncompleted_todos()

    # Confirm that the mock was called.
    assert_true(mock_get_todos.called)

    # Confirm that the expected filtered list of todos was returned.
    assert_list_equal(uncompleted_todos, [todo1])

from nose.tools import assert_list_equal, assert_true
from src.services import get_uncompleted_todos
@patch('src.services.get_todos')
def test_getting_uncompleted_todos_when_todos_is_none(mock_get_todos):
    # Configure mock to return None.
    mock_get_todos.return_value = None

    # Call the service, which will return an empty list.
    uncompleted_todos = get_uncompleted_todos()

    # Confirm that the mock was called.
    assert_true(mock_get_todos.called)

    # Confirm that an empty list was returned.
    assert_list_equal(uncompleted_todos, [])