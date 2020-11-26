"""
Problem Name: pokemon_presentation
You’re a teacher giving a presentation on the types
(https://pokemon.fandom.com/wiki/Types) of pokemons
(https://www.pokemon.com/us/pokedex/). You have a list pokemons_list,
and you have another list types_list(this has the types of the
pokemons in pokemons_lists in the same order). Since you are
presenting, print “[insert pokemon] is a [insert type] type” for all
the pokemons in pokemons_list with their corresponding types in
types_list. Use zip to solve this problem.
"""

# the lists are already given to you
pokemons_list = ["Charmander", "Squirtle", "Bulbasaur", "Pikachu"]
types_list = ["Fire", "Water", "Grass and Poison", "Electric"]

# write your code below
for pokemon, tp in zip(pokemons_list, types_list):
    print(pokemon + " is a " + tp + " type")
