def active_settings(**kwargs):
    """
    Returns a list of settings that are set to True.

    Parameters:
        **kwargs: Variable number of keyword arguments representing settings.

    Returns:
        list: A list containing the names of the settings that are set to True.
    """
    active = [key for key, value in kwargs.items() if value is True]
    return active


if __name__ == '__main__':
    # Teste deine Funktion
    print(
        active_settings(wifi=True, bluetooth=False, gps=True)
    )  # Erwarteter Output: "[wifi, gps]"
