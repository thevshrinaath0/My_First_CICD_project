"""
Tests for calculator CLI
"""

from mylib.calculator import add, subtract
from click.testing import CliRunner
from main import add_cli, sub_cli


def test_add_function():
    """Test the add() function directly"""
    assert add(1, 2) == 3


def test_subtract_function():
    """Test the subtract() function directly"""
    assert subtract(2, 1) == 1


def test_add_cli_help():
    """Test help message for add_cli"""
    runner = CliRunner()
    result = runner.invoke(add_cli, ["--help"])
    assert result.exit_code == 0
    assert "Show this message and exit." in result.output


def test_sub_cli_help():
    """Test help message for sub_cli"""
    runner = CliRunner()
    result = runner.invoke(sub_cli, ["--help"])
    assert result.exit_code == 0
    assert "Show this message and exit." in result.output
