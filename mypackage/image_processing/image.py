import numpy as np
import matplotlib.pyplot as plt
import glob


def get_mean_image(folder):
    """
    Obtiene una imagen promedio a partir de todas las imágenes que se 
    encuentran en la carpeta pasada como argumento.

    Parámetros
    ----------
    folder : str
        Ruta a la carpeta que contiene las imágenes.

    Retornos
    --------
    img : numpy.array
        Imagen promedio.
    """
    print('Función')