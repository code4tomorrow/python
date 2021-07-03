"""
Write a function that provides the nutrition facts of an item
within the provided dictionary 'nutrition_facts'. It should
provide the calories by default. It should accept the other
keys within the item's dictionary as keyword arguments. Use **.
If that keyword argument is True, then print out the value
stored by the key in addition to the default string that
says the number of calories.

---Example 1---
parameters: "lays potato chips", allergens=True

output: 
"Lays potato chips have/has 220 calories"
"allergens: ["processed on equipment that also processes peanuts",
"contains milk ingredients"]

---Example 2---
parameters: "lays potato chips"

output:
"Lays potato chips have/has 220 calories"

---Example 3---
parameters: "lays potato chips", main_ingredients= True

output:
"Lays potato chips have/has 220 calories"
"main_ingredients" : ["potato, "salt", "canola oil"]
"""

nutrition_facts = {
    "lays potato chips": {
        "item": "Lays potato chips",
        "calories": 220,
        "all_ingredients": [
            "potato",
            "salt",
            "canola oil",
            "msg",
            "yeast extract",
            "onion extract",
            "milk protein concentrate",
            "sour cream",
            "xantham gum",
            "maltodextrin",
            "sunflower oil",
        ],
        "main_ingredients": ["potato", "salt", "canola oil"],
        "description": "Sour Cream and Onion Flavor",
        "allergens": [
            "processed on equipment that also processes peanuts",
            "contains milk ingredients",
        ],
    },
    "nutella": {
        "item": "Nutella",
        "calories": 200,
        "all_ingredients": [
            "sugar",
            "palm oil",
            "hazelnuts",
            "skim milk",
            "cocoa",
            "lecithin",
            "vanillin (artificial flavor)",
        ],
        "main_ingredients": ["sugar", "palm oil", "hazelnuts"],
        "description": "Hazelnut spread with cocoa",
        "allergens": ["Contains Tree Nuts", "Contains milk", "Contains soy"],
    },
}
