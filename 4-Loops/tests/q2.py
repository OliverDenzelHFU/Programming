import datetime
OK_FORMAT = False
from otter.test_files import test_case
name = "Variable Types"

@test_case()
def test_q2(afternoon, env):
    assert isinstance(afternoon, datetime.date), "Wrong data type for afternoon"