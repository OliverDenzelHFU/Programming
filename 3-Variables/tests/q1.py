OK_FORMAT = False
from otter.test_files import test_case
name = "Create Variables"

@test_case()
def test_q1(beverages, env):
    assert isinstance(beverages, int), "Beverages falscher Datentyp"
    assert env.__contains__("caffeineSodas"), "Caffeine Sodas not present as a variable"
    assert env.__contains__("caffeineEnergy"), "Caffeine Energy not present as a variable"
    assert env.__contains__("energyQuantity"), "Energy Quantity not present as a variable"
    assert env.__contains__("sodaQuantity"), "Soda Quantity not present as a variable"