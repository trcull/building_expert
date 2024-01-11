from experta import Rule, KnowledgeEngine, AS, GT
from facts import * #I don't normally import * but in this case it helps readability

class BuildingOpportunities(KnowledgeEngine):
    @Rule(
        Province("BC"),
        Lighting(filament="incandescent")
    )
    def switch_to_led_lighting(self):
        print("Upgrade lighting to LED")

    @Rule(
        HVAC(fuel="gas", age=GT(10))
    )
    def electrify_hvac(self):
        print("Electrify HVAC")
