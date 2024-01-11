import experta
import schema
from enum import Enum


class Fuel(experta.Field):
    def __init__(self):
        super().__init__(schema.Schema(str))

    def validate(self, data):
        if data not in ["gas","electric","unknown"]:
            raise Exception(f"Invalid fuel type.  Must be one of gas or electric or unknown")

class Filament(experta.Field):
    def __init__(self):
        super().__init__(schema.Schema(str))

    def validate(self, data):
        if data not in ["led","incandescent"]:
            print(f"Warning: weird Filament value {data}")

class FuelSource(experta.Fact):
    pass

class Province(experta.Fact):
    pass

class HVAC(experta.Fact):
    fuel = Fuel()
    age = experta.Field(schema.Schema(int), default=1)


class Lighting(experta.Fact):
    filament = Filament()
    auto_shutoff = experta.Field(schema.Schema(bool))
