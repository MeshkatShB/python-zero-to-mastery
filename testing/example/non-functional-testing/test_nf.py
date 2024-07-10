import pytest
from testing.example.unit_testing.application import add


@pytest.mark.benchmark
def test_add_performance(benchmark):
    result = benchmark(add, 1000, 2000)
    assert result == 3000
