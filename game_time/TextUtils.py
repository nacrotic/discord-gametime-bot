def split_message(message: str, max_lenght: int = 2000) -> list[str]:
    """Coupe un message en plusieurs pour se conformer aux limites de discord si besoin

    :param message: Le message complet a envoyer
    :param max_lenght: La longeur max des messages (2000 par defaut)
    :return: une liste de message sur laquelle il faut iterrer pour faire le send
    """
    message_parts = []
    message_left = message
    while len(message_left) > max_lenght:
        split_position: int = message_left.rindex("\n", 0, max_lenght)
        message_parts.append(message_left[0:split_position])
        message_left = message_left[split_position:]
    message_parts.append(message_left)
    return message_parts
