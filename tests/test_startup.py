from app import app


def test_index():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """

    # Create a test client using the Flask application configured for testing
    with app.test_client() as test_client:
        response = test_client.get('/')
        # assert response.status_code == 200
        assert response.json.get('status') == 'OK'

def test_health():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """

    # Create a test client using the Flask application configured for testing
    with app.test_client() as test_client:
        response = test_client.get('/health')
        # assert response.status_code == 200
        # print(response.json)
        assert response.json.get('status') == 'OK'