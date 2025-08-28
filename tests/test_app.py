from app import handler

def test_handler():
    result = handler()
    assert result == "Hello from AWS CodeBuild experiment!"

    