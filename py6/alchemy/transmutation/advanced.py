# relative import — . means same folder (transmutation/)
from .basic import lead_to_gold
# relative import — .. means one folder up (alchemy/)
from ..potions import healing_potion

def philosophers_stone():
    gold = lead_to_gold()
    potion = healing_potion()
    return f"Philosopher's stone created using {gold} and {potion}"

def elixir_of_life():
    return "Elixir of life: eternal youth achieved!"