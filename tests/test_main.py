import pytest

from test_ml_project.main import main


def test_main(capsys: pytest.CaptureFixture[str]) -> None:
    main()
    captured = capsys.readouterr()
    assert "Hello from test-ml-project!" in captured.out
