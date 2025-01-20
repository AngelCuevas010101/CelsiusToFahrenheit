# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 2025

@author: Angel Cuevas
"""

def celsius_to_fahrenheit(celsius):
    """
    Convierte una temperatura de Celsius a Fahrenheit.
    
    Fórmula: F = C * 9/5 + 32
    """
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit

# Solicitar al usuario que ingrese una temperatura en Celsius
try:
    celsius_input = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit_output = celsius_to_fahrenheit(celsius_input)
    print(f"{celsius_input} °C son {fahrenheit_output:.2f} °F.")
except ValueError:
    print("Por favor, ingrese un número válido.")

