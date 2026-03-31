from test_ml_project.greet import greet


def test_greet() -> None:
    result = greet("World")
    assert result == "Hello, World! Welcome to test-ml-project."
