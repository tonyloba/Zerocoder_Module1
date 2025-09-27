import sys
import os
import requests
from unittest.mock import Mock, patch

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Now import the function to test
from .main import get_random_cat_image

def test_get_random_cat_image_success():
    # Create a mock response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"url": "https://cdn2.thecatapi.com/images/abc.jpg"}]

    # Patch requests.get to return our mock response
    with patch('requests.get', return_value=mock_response) as mock_get:
        result = get_random_cat_image()
        
        # Assert the function returns the expected URL
        assert result == "https://cdn2.thecatapi.com/images/abc.jpg"
        # Verify requests.get was called with the correct URL
        mock_get.assert_called_once_with("https://api.thecatapi.com/v1/images/search", timeout=5)

def test_get_random_cat_image_fail_status():
    # Create a mock response for failed status
    mock_response = Mock()
    mock_response.status_code = 404
    mock_response.json.return_value = {}

    with patch('requests.get', return_value=mock_response):
        result = get_random_cat_image()
        assert result is None

def test_get_random_cat_image_exception():
    # Simulate a network error
    with patch('requests.get', side_effect=requests.RequestException("Network error")):
        result = get_random_cat_image()
        assert result is None