OK_FORMAT = False
from otter.test_files import test_case
name = "Variable Types"

@test_case()
def test_q2(beverages, caffeineSodas, caffeineEnergy, energyQuantity, sodaQuantity, env):
    assert isinstance(beverages, int), "Wrong data type for beverages"
    assert isinstance(caffeineSodas, int), "Wrong data type for caffeineSodas"
    assert isinstance(caffeineEnergy, int), "Wrong data type for caffeineEnergy"
    assert isinstance(energyQuantity, int), "Wrong data type for energyQuantity"
    assert isinstance(sodaQuantity, int), "Wrong data type for sodaQuantity"