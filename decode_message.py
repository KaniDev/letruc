import base64
# Fonction pour détecter la base et décoder
def decode_message(encoded_message):
    try:
        # Base 32
        decoded = base64.b32decode(encoded_message).decode('utf-8')
        return decoded
    except Exception:
        pass

    try:
        # Base 64
        decoded = base64.b64decode(encoded_message).decode('utf-8')
        return decoded
    except Exception:
        pass

    try:
        # Base 85
        decoded = base64.b85decode(encoded_message).decode('utf-8')
        return decoded
    except Exception:
        pass

    return "Impossible de décoder"