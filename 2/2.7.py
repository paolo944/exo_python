def rectangle(h: float, l: float) -> None:
    # Précondition: l et h > 0
    triangle1: Image = fill_triangle(-1,-1,-1,h-1,l-1,h-1, "red")
    triangle2: Image = fill_triangle(-1,-1,l-1,-1,l-1,h-1, "yellow")
    rectangle_finale: Image = overlay(triangle1, triangle2)
    return show_image(rectangle_finale)

def tour(h: float, l1: float, l2: float) -> None:
    """Précondition: hauteur correspond à la hauteur de chaque étage.
    largeur1 correspond à la largeur du permier étage et largeur2 à celle du deuxième.
    Ils doivent tous être supérieur à 0."""
    rectangle1_tour: None = rectangle(h, l1)
    rectangle2_tour: None = rectangle(h, l2)
    tour_finale: Image = overlay(rectangle1_tour, rectangle2_tour)
    return show_image(tour_finale)
