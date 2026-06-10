"""A Small Project used to learn how to understand boolean
and how to apply it to a game logic such as leggally bonding
Pac-Man"""


def eat_ghost(power_pellet_active, touching_ghost):
    """Verify if the player consumes a ghost

    Parameters:
        power_pellet_active(bool): Is the power pellet active?
        touching_ghost(bool): Is the player touching the ghost?

    Returns:
        bool: Is the ghost eaten?
    """
    consume_ghost = touching_ghost and power_pellet_active
    return consume_ghost


def score(touching_power_pellet, touching_dot):
    """Verify has the player scored a point.

    Parameters:
        touching_power_pellet(bool): Is the player touching the power pellet?
        touching_dot(bool): Is the player touching a dot?

    Returns:
        bool: Has the player scored a point?
    """
    score_increase = touching_power_pellet or touching_dot
    return score_increase


def lose(power_pellet_active, touching_ghost):
    """Verify has the player lost

    Parameters:
        power_pellet_active(bool): Is the power pellet active?
        touching_ghost(bool): Is the player touching a ghost?

    Returns:
        bool: Has the player touched a ghost without an active
        power pellet?
    """
    player_lose = touching_ghost and not power_pellet_active
    return player_lose


def win(has_eaten_all_dots, touching_ghost, power_pellet_active):
    """Verify has the player won

    Parameters:
        has_eaten_all_dots(bool): has the player eaten all the dots?
        touching_ghost(bool): is the player touching a ghost?
        power_pellet_active(bool): is the power pellet active?

    Returns:
        bool: Has the player eaten all the dots without touching a ghost
            or if they are touching a ghost and eat all the dots it was
            done with the power pellet active.
    """
    return has_eaten_all_dots and not lose(touching_ghost, power_pellet_active)
