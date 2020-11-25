# import pytest
import requests
import DLFunctions as dlf


def test_for_200(monkeypatch):
    class mock_network_response:
        def __init__(self):
            self.status_code = 200

    def mock_url(url):
        return mock_network_response()

    monkeypatch.setattr(requests, "get", mock_url)
    assert dlf.single_link_status_checker("https://google.com") == 200


def test_for_400(monkeypatch):
    class mock_network_response:
        def __init__(self):
            self.status_code = 404

    def mock_url(url):
        return mock_network_response()

    monkeypatch.setattr(requests, "get", mock_url)
    assert dlf.single_link_status_checker("https://google.com") == 404
