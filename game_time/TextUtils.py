
def split_message(message: str, max_lenght: int) -> list[str]:
    message_parts = []
    message_left = message
    print("split_message -- len(message): " + str(len(message)) + " max_lenght: " + str(max_lenght))
    while len(message_left) > max_lenght:
        split_position: int = message_left.rindex("\n", 0, max_lenght)
        message_parts.append(message_left[0:split_position])
        print("split_message -- len(message_left): " + str(len(message_left))
              + " max_lenght: " + str(max_lenght)
              + " len(message_parts): " + str(len(message_parts)))
        message_left = message_left[split_position:]
    message_parts.append(message_left)
    print("message_parts -- : ", message_parts)
    return message_parts
