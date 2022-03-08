"""This test the homepage"""


def test_request_example(client):
    """This makes the index page"""
    response = client.get("/")
    assert b"Hello, welcome to my website for Project 1" in response.data
