# -*- coding: utf-8 -*-
"""Konversi suhu

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uqrMYQ7JeuDwdIFOUjxrViff1SagwB99
"""

suhu_C = float(input("Masukkan suhu dalam Celsius: "))

suhu_F = (suhu_C * 9/5) + 32
print(f"Suhu dalam Fahrenheit: {suhu_F:.2f}")

suhu_C = float(input("Masukkan suhu dalam Celsius: "))

suhu_F = (suhu_C * 9/5) + 32
print(f"Suhu dalam Fahrenheit: {suhu_F:.2f}")

if suhu_F > 150:
  print("Sekarang suhunya panas")
elif suhu_F > 100:
  print("Sekarang suhunya normal")
else:
  print("Sekarang suhunya dingin")