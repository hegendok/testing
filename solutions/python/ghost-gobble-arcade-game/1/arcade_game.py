def eat_ghost(power_pellet_active, touching_ghost):
    """Verify if the player consumes a ghost

    Parameters:
        power_pellet_active(bool): Is the power pellet active?
        touching_ghost(bool): Is the player touching the ghost?

    Returns:
        bool: Is the ghost eaten?
    """
    if touching_ghost and power_pellet_active == True:
        return True
    elif power_pellet_active == False:
        return False
    else:
        return False


def score(touching_power_pellet, touching_dot):
    """Verify has the player scored a point.

    Parameters:
        touching_power_pellet(bool): Is the player touching the power pellet?
        touching_dot(bool): Is the player touching a dot?

    Returns:
        bool: Has the player scored a point?
    """
    if touching_power_pellet or touching_dot == True:
        return True
    else:
        return False


def lose(power_pellet_active, touching_ghost):
    """Verify has the player lost

    Parameters:
        power_pellet_active(bool): Is the power pellet active?
        touching_ghost(bool): Is the player touching a ghost?

    Returns:
        bool: Has the player touched a ghost without an active
        power pellet?
    """
    if power_pellet_active and touching_ghost == True:
        return False
    elif touching_ghost == True:
        return True
    else:
        return False

def win(has_eaten_all_dots, touching_ghost, power_pellet_active):
    if has_eaten_all_dots and not (touching_ghost or power_pellet_active):
        return True
    elif power_pellet_active and has_eaten_all_dots and touching_ghost:
        return True
    else:
        return False












