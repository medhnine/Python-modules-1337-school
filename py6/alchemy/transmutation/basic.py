# absolute import used here — full path from project root
from alchemy.elements import create_fire, create_earth

def lead_to_gold():
    fire = create_fire()
    return f"Lead transmuted to gold using {fire}"

def stone_to_gem():
    earth = create_earth()
    return f"Stone transmuted to gem using {earth}"