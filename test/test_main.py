from pytest import approx

import package_name.main as main_module


def test_add_2_numbers():
    assert main_module.add_2_numbers(1, 2) == 3
    assert main_module.add_2_numbers(1.0, -2) == approx(-1.0)
    assert main_module.add_2_numbers(-1.0, 4.0) == approx(3.0)
