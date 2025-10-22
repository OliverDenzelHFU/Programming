OK_FORMAT = False
from otter.test_files import test_case
name = "Calculations"

@test_case()
def test_q3(beverages, caffeineSodas, caffeineEnergy, energyQuantity, sodaQuantity, env):
    assert energyQuantity == beverages * caffeineEnergy, "Wrong Result for Energy"
    assert sodaQuantity == beverages * caffeineSodas, "Wrong Result for Soda"