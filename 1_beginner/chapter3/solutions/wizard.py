"""
Wizard

There are 3 criteria to determine whether
you’re a wizard or not.

Define a variable called is_wizard and
use logic operators to set it to the correct
value based on the criteria.

Here are some example variable values and outputs.
You'll need to figure out the order of logic operators
needed to turn these inputs into these outputs! :)

Example variable values and output:

If you can fly, you’ve not a battled a dragon,
and you’re alive, output “Wizard: True”

If you can fly, you’ve battled a dragon,
and you’re not alive, output “Wizard: True”

If you can’t fly, you’ve battled a dragon,
and you’re not alive, output “Wizard: False”

If you can’t fly, you’ve battled a dragon,
and you’re alive, output “Wizard: True"

The initial variables are given, but you'll have
to change the values to test your code.
"""

can_fly = True
battled_dragon = False
is_alive = True

is_wizard = can_fly or (battled_dragon and is_alive)

print("Wizard:", is_wizard)
