import pytest
from project import get_stock_data, calculate_value, format_portfolio
from unittest.mock import patch, MagicMock


def test_calculate_value():
    assert calculate_value(100, 10) == 1000
    assert calculate_value(50.5, 2) == 101.0
    assert calculate_value(0, 5) == 0
    assert calculate_value(150.25, 0) == 0


@patch("project.yf.Ticker")
def test_get_stock_data_success(mock_ticker):
    mock_info = {"currentPrice": 150.0, "previousClose": 145.0}
    mock_instance = MagicMock()
    mock_instance.info = mock_info
    mock_ticker.return_value = mock_instance
    result = get_stock_data("AAPL")
    assert result is not None
    assert result["price"] == 150.0
    assert result["change"] == 5.0
    assert result["change_pct"] == pytest.approx(3.448, 0.1)


@patch("project.yf.Ticker")
def test_get_stock_data_no_price(mock_ticker):
    mock_instance = MagicMock()
    mock_instance.info = {}
    mock_ticker.return_value = mock_instance
    assert get_stock_data("UNKNOWN") is None


@patch("project.yf.Ticker")
def test_get_stock_data_exception(mock_ticker):
    mock_ticker.side_effect = Exception("API error")
    assert get_stock_data("AAPL") is None


@patch("project.get_stock_data")
def test_format_portfolio(mock_get):
    mock_get.return_value = {"price": 150.0, "change": 5.0, "change_pct": 3.45}
    portfolio = {"AAPL": 10, "GOOGL": 5}
    result = format_portfolio(portfolio)
    assert "AAPL" in result
    assert "GOOGL" in result
    assert "$1500.00" in result
    assert "+5.00" in result
