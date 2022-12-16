import questionary

# Entity Name
entity_name = questionary.text("What's the entity name?").ask()


# Attributes
next_attribute = True
while next_attribute:
    attribute_name = questionary.text("What's the attribute name?").ask()
    attribute_type = questionary.select(
        "What's the attribute type?",
        choices=["Boolean", "String", "Float", "Integer"],
    ).ask()
    next_attribute = questionary.confirm("There are next attribute?", default=False).ask()

