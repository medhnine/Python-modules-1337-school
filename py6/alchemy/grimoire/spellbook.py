def record_spell(spell_name: str, ingredients: str) -> str:
    # LATE IMPORT — imported inside the function, not at the top of the file
    # this avoids circular dependency because by the time this function
    # is called, both modules are already fully loaded
    from .validator import validate_ingredients
    
    validation = validate_ingredients(ingredients)
    
    if "VALID" in validation and "INVALID" not in validation:
        return f"Spell recorded: {spell_name} ({validation})"
    else:
        return f"Spell rejected: {spell_name} ({validation})"