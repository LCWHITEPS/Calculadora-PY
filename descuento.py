
def descuento(precio, porcentaje):
    """
    Calcula el precio final después de aplicar un descuento.

    Args:
        precio: Precio original del producto.
        porcentaje: Porcentaje de descuento entre 0 y 100.

    Returns:
        Precio final con el descuento aplicado.

    Raises:
        TypeError: Si los valores no son numéricos.
        ValueError: Si el precio o porcentaje son inválidos.
    """
    if isinstance(precio, bool) or not isinstance(precio, (int, float)):
        raise TypeError("El precio debe ser numérico.")

    if isinstance(porcentaje, bool) or not isinstance(porcentaje, (int, float)):
        raise TypeError("El porcentaje debe ser numérico.")

    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")

    if porcentaje < 0 or porcentaje > 100:
        raise ValueError("El porcentaje debe estar entre 0 y 100.")

    return round(precio - (precio * porcentaje / 100), 2)