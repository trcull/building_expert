
This example uses an "expert systems" library in Python to encode a bunch of business rules that the library then evaluates when given facts.  Expert systems are actually a very old kind of AI technology that's historically used in systems automation.  I've never used them before, but as I was hearing about the general problem of trying to encode a bunch of rules that might be very complicated and interdependent, it occured to me that an expert systems approach might be intersting.

This particular example uses a library called "experta" which, unfortunately, doesn't appear to be actively maintained: https://github.com/nilp0inter/experta.  That's not the end of the world because there are other libraries.  Experta is LGPL and so couldn't be used in commercial software, anyway.  But I thought its syntax was useful for illustrating the general concept. There are other libraries, too, especially Drools in Java.

All of these libraries use a specific algorithm that makes evaluating even extremely convolued sets of rules very efficient: https://en.m.wikipedia.org/wiki/Rete_algorithm

The general idea is that you encode a universe of "things you can say about things" in terms of a bunch of "facts" classes, which I've done in https://github.com/trcull/building_expert/blob/main/lib/facts.py.

Then you encode a bunch of independent "rules" that are just annotated python methods that, essentially, say "when this and this and this are true, then run me", which I've done in https://github.com/trcull/building_expert/blob/main/lib/rules.py.

Then you declare a particular scenario of facts and hand them to the rules engine and ask it, basically, "what should I do given this particular scenario?" which I've done in https://github.com/trcull/building_expert/blob/main/lib/supervisor.py with a handful of scenarios.

I've just hardcoded the rules and the declaration of facts straight in python.  But one could imagine reading those in more dynamically from a file or a database or a Google Sheet that building engineers maintain themselves, instead, which would achieve the goal of giving building experts more direct control.  



To run this, do these two on a command line:
 ```
 pip install -r requirements.txt
 python lib/supervisor.py
 ```

 Here's an example of running it on my macbook:

 ```
 (base) trcull@Tims-MacBook-Pro building_expert % python lib/supervisor.py                                       

A gas-cooled building in BC with HVAC more than 25 years old:
<f-0>: InitialFact()
<f-1>: Province('BC')
<f-2>: HVAC(fuel='gas', age=25)
<f-3>: Lighting(filament='incandescent')

...recommendation is....

Upgrade lighting to LED
Electrify HVAC

A gas-cooled building in BC with brand new HVAC but incandescent lighting:
<f-0>: InitialFact()
<f-1>: Province('BC')
<f-2>: HVAC(fuel='gas', age=1)
<f-3>: Lighting(filament='incandescent')

...recommendation is....

Upgrade lighting to LED

A gas-cooled building in Alberta and incandescent lighting that we don't bother LED-ifying because of shale gas:
<f-0>: InitialFact()
<f-1>: Province('AB')
<f-2>: HVAC(fuel='gas', age=12)
<f-3>: Lighting(filament='incandescent')

...recommendation is....

Electrify HVAC
(base) trcull@Tims-MacBook-Pro building_expert %
```
