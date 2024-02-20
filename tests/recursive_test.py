# Unit tests for Recursive Algorithm by Taras
"""This file runs the Recursive Algorithm and
compares the result to output for accuracy."""

# Import pytest framework to execute tests
# Import recursive function from floyd_warshall_algorithm
# Import test cases from tests

import pytest
from floyd_warshall_algorithm.floyd_warshall_recursive import floyd_warshall
from tests.test_cases import sample_a, sample_b, sample_c, sample_d, sample_e, sample_f
from tests.test_cases import output_a, output_b, output_c, output_d, output_e, output_f


# Define test cases with pytest for 4 vertices small graphs
# Parametrized tests for convenience of time saving and having
# multiple test scenarios for small graphs.


@pytest.mark.parametrize("dist, expected_result", [
    (sample_a, output_a),
    (sample_b, output_b)
])

def test_smallgraphs(dist, expected_result):
    result = floyd_warshall(dist)
    assert result == expected_result


# Define test cases with pytest for 8 vertices large graphs
# Parametrized tests for convenience of time saving and having
# multiple test scenarios for large graphs.


@pytest.mark.parametrize("dist, expected_result", [
    (sample_c, output_c),
    (sample_d, output_d)
])


def test_largegraphs(dist, expected_result):
    result = floyd_warshall(dist)
    assert result == expected_result


# Define test cases with pytest for negative graphs
# Parametrized tests for convenience of time saving and having
# multiple test scenarios for negative graphs.


@pytest.mark.parametrize("dist, expected_result", [
    (sample_e, output_e),
    (sample_f, output_f)
])


def test_negativegraphs(dist, expected_result):
    result = floyd_warshall(dist)
    assert result == expected_result
