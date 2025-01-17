# Fonction pour trouver la couleur CSS la plus proche

def get_closest_color_name(rgb):
    import webcolors
    min_diff = None
    closest_name = None
    for name, hex_value in webcolors.CSS3_NAMES_TO_HEX.items():
        r, g, b = webcolors.hex_to_rgb(hex_value)
        diff = (r - rgb[0])**2 + (g - rgb[1])**2 + (b - rgb[2])**2
        if min_diff is None or diff < min_diff:
            min_diff = diff
            closest_name = name
    return closest_name