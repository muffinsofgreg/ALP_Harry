class Celsius:

    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_farenheight(self):
        return (temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting Value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature cannot be below -273")
        print("Setting Value")
        self._temperature = value
