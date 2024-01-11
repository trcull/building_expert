import rules
from facts import * #I don't normally import * but in this case it helps readability

def do_it():
    engine = rules.BuildingOpportunities()
    engine.reset()
    print("\nA gas-cooled building in BC with HVAC more than 25 years old:")
    engine.declare(
        Province("BC"),
        HVAC(fuel="gas",age=25),
        Lighting(filament="incandescent")
    )
    print(engine.facts)
    print("\n...recommendation is....\n")
    engine.run()


    engine.reset()
    print("\nA gas-cooled building in BC with brand new HVAC but incandescent lighting:")
    engine.declare(
        Province("BC"),
        HVAC(fuel="gas",age=1),
        Lighting(filament="incandescent")
    )
    print(engine.facts)
    print("\n...recommendation is....\n")
    engine.run()


    engine.reset()
    print("\nA gas-cooled building in Alberta and incandescent lighting that we don't bother LED-ifying because of shale gas:")
    engine.declare(
        Province("AB"),
        HVAC(fuel="gas",age=12),
        Lighting(filament="incandescent")
    )
    print(engine.facts)
    print("\n...recommendation is....\n")
    engine.run()



if __name__ == '__main__':
    do_it()
