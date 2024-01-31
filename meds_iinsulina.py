import math

def calcular_entrega_lapiceras(dosis_diaria, tipo_insulina):
    dosis_total = dosis_diaria * 30

    limite_mensual_1000 = 30  # Cantidad máxima de frascos de 1000 UI para un mes
    limite_mensual_450 = 30  # Cantidad máxima de lapiceras de 450 UI para un mes
    limite_mensual_300 = 30  # Cantidad máxima de lapiceras de 300 UI para un mes

    if tipo_insulina == "glarg300":
        if dosis_total > limite_mensual_450 * 450:
            print("La dosis solicitada excede el límite mensual.")
            dosis_total = limite_mensual_450 * 450

        lapiceras_450ui = math.ceil(dosis_total / 450)
        return lapiceras_450ui, 0, 0
    elif tipo_insulina == "ur" or tipo_insulina == "degludec" or tipo_insulina == "detemir":
        if dosis_total > limite_mensual_300 * 300:
            print("La dosis solicitada excede el límite mensual.")
            dosis_total = limite_mensual_300 * 300

        lapiceras_300ui = math.ceil(dosis_total / 300)
        return 0, lapiceras_300ui, 0
    elif tipo_insulina == "frasco":
        if dosis_total > limite_mensual_1000 * 1000:
            print("La dosis solicitada excede el límite mensual.")
            dosis_total = limite_mensual_1000 * 1000

        frascos_1000ui = math.ceil(dosis_total / 1000)
        return 0, 0, frascos_1000ui
    else:
        print("Tipo de insulina no válido.")
        return 0, 0, 0


# Ejemplo de uso
dosis_diaria = int(input("Ingrese la dosis diaria requerida de insulina (en UI): "))
tipo_insulina = input("Ingrese el tipo de insulina (glargina u300, ultra rápida, degludec, detemir, frasco): ")

lapiceras_450, lapiceras_300, frascos_1000 = calcular_entrega_lapiceras(dosis_diaria, tipo_insulina)

print("Número de lapiceras de 450 UI a entregar durante el mes:", lapiceras_450)
print("Número de lapiceras de 300 UI a entregar durante el mes:", lapiceras_300)
print("Número de frascos de 1000 UI a entregar durante el mes:", frascos_1000)
