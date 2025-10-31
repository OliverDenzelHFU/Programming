OK_FORMAT = False
from otter.test_files import test_case
name = "Create Variables"

@test_case()
def test_q1(env):
    assert env.__contains__("afternoon"), "afternoon not present as a variable"