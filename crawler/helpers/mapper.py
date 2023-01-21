def generate_ids_map():
    """
    Return generator of generators.
    Used for creating intigers that will be used as products IDs.
    """
    stp = 100
    genex = ((y for y in range(x, stp + x)) for x in range(1, 2500000, stp))

    return genex
