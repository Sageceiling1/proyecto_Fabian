def clasificar_altura(msnm):
    if 400 <= msnm <= 800:
        return "sumamente apto"
    elif 0 <= msnm < 400 or 801 <= msnm <= 999:
        return "moderadamente apto"
    elif 1000 <= msnm <= 1200:
        return "marginalmente apto"
    else:
        return "no apto"

def clasificar_profundidad(cm):
    if cm > 100:
        return "sumamente apto"
    elif 50 <= cm <= 100:
        return "moderadamente apto"
    elif 25 <= cm < 50:
        return "marginalmente apto"
    else:
        return "no apto"

def peor_categoria(cat1, cat2):
    categorias = ["sumamente apto", "moderadamente apto", "marginalmente apto", "no apto"]
    return cat1 if categorias.index(cat1) > categorias.index(cat2) else cat2

def main():
    num_lecturas = int(input("Ingrese el número de lecturas: "))

    alturas = []
    profundidades = []

    conteo_categorias = {
        "sumamente apto": 0,
        "moderadamente apto": 0,
        "marginalmente apto": 0,
        "no apto": 0
    }

    for i in range(num_lecturas):
        altura = float(input(f"Ingrese la altura #{i+1} (msnm): "))
        profundidad = float(input(f"Ingrese la profundidad #{i+1} (cm): "))

        alturas.append(altura)
        profundidades.append(profundidad)

        cat_altura = clasificar_altura(altura)
        cat_profundidad = clasificar_profundidad(profundidad)

        if cat_altura == cat_profundidad:
            final_cat = cat_altura
        else:
            final_cat = peor_categoria(cat_altura, cat_profundidad)

        conteo_categorias[final_cat] += 1

    promedio_altura = sum(alturas) / len(alturas)
    promedio_profundidad = sum(profundidades) / len(profundidades)

    print(f"\nPromedio de altura: {promedio_altura:.2f}")
    print(f"Promedio de profundidad: {promedio_profundidad:.2f}")

    for categoria, conteo in conteo_categorias.items():
        print(f"{categoria} {conteo}")

if __name__ == "__main__":
    main()