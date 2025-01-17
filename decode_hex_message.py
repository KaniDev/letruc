# Fonction pour décoder un message hexadécimal
def decode_hex_message(hex_message):
    try:
        # Vérifier que la chaîne est valide
        if not all(c in "0123456789abcdefABCDEF" for c in hex_message.replace(" ", "")):
            return "Format hexadécimal invalide"
        
        # Convertir la chaîne hexadécimale en texte
        bytes_message = bytes.fromhex(hex_message)
        decoded_message = bytes_message.decode('utf-8')
        return decoded_message.upper()
    except Exception as e:
        return f"Erreur de décodage: {e}"