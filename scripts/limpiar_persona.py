#!/usr/bin/env python3
"""Convierte las columnas float64 de persona.csv a entero y exporta un CSV nuevo."""

import pandas as pd

ENTRADA = "casen/tablas/persona.csv"
SALIDA = "casen/tablas/persona_limpia.csv"

# Columnas float64 a convertir
float_cols = [
    "activ",
    "codigo_nivel",
    "codigo_subcampo",
    "codigo_cat_ocup",
    "codigo_subrama",
    "yoprcor",
]

df = pd.read_csv(ENTRADA)

# Int64 (con I mayuscula) = entero nullable: conserva los NaN como celdas vacias
df[float_cols] = df[float_cols].astype("Int64")

df.to_csv(SALIDA, index=False)
print(f"Listo. {len(df)} filas exportadas a {SALIDA}")
