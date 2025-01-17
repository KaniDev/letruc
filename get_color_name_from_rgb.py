# Fonction pour trouver le nom de la couleur

def get_color_name_from_rgb(rgb):
    import webcolors
    try:
        # Nom exact de la couleur
        color_name = webcolors.rgb_to_name(rgb)
        return color_name  # Retourner uniquement le nom sans "Couleur exacte :"
    except ValueError:
        # Si aucune correspondance exacte, trouver la couleur la plus proche
        closest_name = get_closest_color_name(rgb)
        return closest_name  # Retourner uniquement le nom de la couleur la plus proche
