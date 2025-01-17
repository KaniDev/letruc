import re

def get_last_letter(data):
    try:
        # Extraire le numéro de question et la position du mot
        match_question = re.search(r"Question (\\d+):.*dern.* (\\d+).*liste: (.+)", data, re.IGNORECASE)
        if not match_question:
            return "Format invalide\n"
        
        question_number = match_question.group(1)  # Numéro de la question
        word_position = int(match_question.group(2))  # Position du mot
        word_list = match_question.group(3).strip()  # Liste des mots
        
        # Diviser la liste en mots
        words = word_list.split()
        if word_position > len(words):
            return f"Erreur: seulement {len(words)} mots disponibles, mais demandé {word_position}\n"
        
        # Sélectionner le mot demandé et récupérer la dernière lettre
        selected_word = words[word_position - 1]
        last_letter = selected_word[-1]
        return f"{last_letter}\n"
    except Exception as e:
        return f"Erreur: {e}\n"