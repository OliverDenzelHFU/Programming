import datetime
OK_FORMAT = False
from otter.test_files import test_case
name = "Calculations"

@test_case()
def test_q3(afternoon, env):
    assert afternoon.hour == 13 and afternoon.minute==0, "Wrong Time for afternoon"