import re
import socket
from datetime import datetime

from decode_braille import decode_braille
from decode_hex_message import decode_hex_message
from decode_message import decode_message
from decode_morse import decode_morse
from get_closest_color_name import get_closest_color_name
from get_color_name_from_rgb import get_color_name_from_rgb
from get_last_letter import get_last_letter

# Préparer les réponses dynamiques
def generate_response(question):
    # Extraire le numéro de la question
    question_number_match = re.search(r"Question (\d+):", question)
    if question_number_match:
        question_number = question_number_match.group(1)
    else:
        return "Format de question invalide\n"
    
    # Si la réponse a déjà été donnée, retourner la réponse précédente
    if question_number in responses:
        return responses[question_number]
    
    # Réponses en fonction de la question
    if question_number == '1':
        response = "lise/buniowski/3SI6"
    elif question_number == '2':
        response = datetime.now().strftime("%d/%m")
    elif question_number == '3':
        match = re.search(r"(\d+)\s*([+\-*/])\s*(\d+)", question)
        if match:
            num1 = int(match.group(1))
            operator = match.group(2)
            num2 = int(match.group(3))
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 // num2
            else:
                result = "Erreur"
            response = f"{result}"
        else:
            response = "Erreur de calcul\n"
    
    elif question_number == '4':
        match = re.search(r"Décoder ce message:\s*(\S+)", question)
        if match:
            encoded_message = match.group(1)
            decoded_message = decode_message(encoded_message).strip()
            response = f"{decoded_message.lower()}"
    
    elif question_number == '5':
        match = re.search(r"Décoder ce message en majuscule:\s*([0-9a-fA-F\s]+)", question)
        if match:
            hex_message = match.group(1)
            decoded_message = decode_hex_message(hex_message).strip()  # Décodage du message hexadécimal en ASCII
            if decoded_message:
                decoded_morse = decode_morse(decoded_message)
                response = f"{decoded_morse.upper()}"
            else:
                response = "Erreur de décodage\n"
    
    elif question_number == '6':
        match = re.search(r"Décoder ce message en majuscule:\s*([0-9a-fA-F\s]+)", question)
        if match:
            hex_message = match.group(1)
            decoded_message = decode_hex_message(hex_message).strip()  # Décodage du message hexadécimal en ASCII
            if decoded_message:
                braille_message = decode_braille(decoded_message)
                response = f"{braille_message}"
            else:
                response = "Erreur de décodage\n"
    
    elif question_number == '7':
        # Extraire les valeurs RGB
        match = re.search(r"RGB\s*\((\d+),\s*(\d+),\s*(\d+)\)", question)
        if match:
            r, g, b = map(int, match.groups())
            rgb = (r, g, b)
            color_name = get_color_name_from_rgb(rgb)
            response = color_name.encode('utf-8')
        else:
            response = "Format RGB invalide"
        
    elif question_number == '8':
        # Vérifier la question demandée et renvoyer uniquement la réponse correspondante
        if '1' in responses:
            response_1 = responses['1']
        else:
            response_1 = "Réponse à la question 1 non disponible\n"
    
        if '2' in responses:
            response_2 = responses['2']
        else:
            response_2 = "Réponse à la question 2 non disponible\n"
    
        if '3' in responses:
            response_3 = responses['3']
        else:
            response_3 = "Réponse à la question 3 non disponible\n"
    
        if '4' in responses:
            response_4 = responses['4']
        else:
            response_4 = "Réponse à la question 4 non disponible\n"
    
        if '5' in responses:
            response_5 = responses['5']
        else:
            response_5 = "Réponse à la question 5 non disponible\n"
    
        if '6' in responses:
            response_6 = responses['6']
        else:
            response_6 = "Réponse à la question 6 non disponible\n"
    
        if '7' in responses:
            response_7 = responses['7']
        else:
            response_7 = "Réponse à la question 7 non disponible\n"

        # Initialiser la réponse par défaut au cas où
        response = "Réponse non reconnue"

        # Vérifier la question demandée et renvoyer uniquement la réponse correspondante
        match = re.search(r"Question 8: Redonné moi la réponse de la question (\d+)", question)
        if match:
            question_requested = match.group(1)  # Numéro de la question demandée
        
            # Renvoyer uniquement la réponse à la question spécifique demandée
            if question_requested == '1':
                response = response_1
            elif question_requested == '2':
                response = response_2
            elif question_requested == '3':
                response = response_3
            elif question_requested == '4':
                response = response_4
            elif question_requested == '5':
                response = response_5
            elif question_requested == '6':
                response = response_6
            elif question_requested == '7':
                response = response_7
            else:
                response = "Question non reconnue."

    elif question_number == '9':
        # Extraire la position et la liste des mots
        match_question = re.search(r"dern.* (\d+).*liste: (.+)", question, re.IGNORECASE)
        if match_question:
            word_position = int(match_question.group(1))  # Position du mot
            word_list = match_question.group(2).strip()  # Liste des mots
            words = word_list.split()
            if word_position <= len(words):
                selected_word = words[word_position - 1]  # Récupérer le mot demandé
                last_letter = selected_word[-1]  # Dernière lettre
                response = f"{last_letter}"
            else:
                response = f"Erreur: seulement {len(words)} mots disponibles, mais demandé {word_position}\n"
        else:
            response = "Format invalide pour la question 9\n"

    elif question_number == '10':
        # Rassembler toutes les réponses précédentes en les triant par ordre de numéro de question
        all_responses = "_".join(
            response.decode('utf-8').strip() if isinstance(response, bytes) else response.strip()
            for i, response in sorted(responses.items(), key=lambda x: int(x[0]))
        )
        response = all_responses + "\n"

        # Stocker la réponse pour pouvoir la réutiliser
    responses[question_number] = response

    return response


# Connexion au serveur
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(5)  # Timeout pour éviter les blocages
    s.connect((HOST, PORT))

    while True:
        try:
            # Réception des données
            data = s.recv(1024).decode('utf-8')
            if not data:
                print("Connexion terminée par le serveur.")
                break

            print("Reçu:", data.strip())

            # Vérifier si c'est une question et générer une réponse
            if "Question" in data:
                response = generate_response(data)
                print(f"Debug: Réponse brute envoyée = {response}")
                print("Envoi de la réponse:", response)

                # Envoi de la réponse
                if isinstance(response, bytes):
                    s.sendall(response)  # Si déjà en binaire
                else:
                    s.sendall(response.encode('utf-8'))  # Si c'est une chaîne, encoder en UTF-8
            else:
                print("Message reçu:", data.strip())

        except socket.timeout:
            print("Aucun message reçu, connexion fermée pour inactivité.")
            break
        except Exception as e:
            print(f"Erreur : {e}")
            break