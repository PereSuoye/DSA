def two_fer(name=None):
    """Return a string with a message when given a name."""
    if name==None:
        return "One for you, one for me."
    else:
        return f"One for {name.title()}, one for me."

