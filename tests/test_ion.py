from ion import __version__
from ion.app import app


app.testing = True
client = app.test_client()


def test_version():
    assert __version__ == "0.1.0"


def test_index():
    response = client.get("/")
    assert "Hello, Notion!" == response.get_data(as_text=True)
