OK_FORMAT = False
from otter.test_files import test_case
name = "q1"

@test_case()
def test_q1(beverages, env):
    assert isinstance(beverages, int), "Beverages falsch"
    print(env)