import pytest
from src.report_engine import run_report


def test_run_report_success():
    rows = [
        {"position": "Backend", "performance": "5"},
    ]

    result = run_report("performance", rows)

    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0]["position"] == "Backend"


def test_run_report_invalid_value():
    with pytest.raises(ValueError):
        run_report("does_not_exist", [])
