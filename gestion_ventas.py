"""
MÓDULO: Entornos de Desarrollo (1DM3)
RETO 2: Depuración de Código en VS Code
EJERCICIO: Sistema de Gestión de Ventas (gestion_ventas.py)

"""

def fn_CalcularDescuento_fl(precio_total_fl, tipo_cliente_str):
    """
    Calcula el precio final aplicando un descuento según el tipo de cliente.
    - 'VIP': 20% de descuento.
    - 'HABITUAL': 10% de descuento.
    - 'NUEVO': Sin descuento.
    """

    if tipo_cliente_str == "VIP":
        precio_final_fl = precio_total_fl * 0.20
    elif tipo_cliente_str == "HABITUAL":
        precio_final_fl = precio_total_fl * 0.90
    else:
        precio_final_fl = precio_total_fl
    
    return precio_final_fl

def fn_ProcesarListaVentas_fl(ventas_lst):
    """
    Procesa una lista de importes de ventas y calcula el total acumulado.
    """
    total_fl = 0
    i = 0
    
    while i < len(ventas_lst):
        total_fl += ventas_lst[i]

    return total_fl

def fn_EvaluarObjetivoDiario_bool(total_ventas_fl, objetivo_int=500):
    """
    Evalúa si se ha alcanzado el objetivo mínimo de ventas diarias.
    """

    if total_ventas_fl < objetivo_int: 
        alcanzado_bool = True
    else:
        alcanzado_bool = False
        
    return alcanzado_bool

def main():
    print("=== SISTEMA DE GESTIÓN DE VENTAS - RESTAURANTE ===")
    
    # Datos de prueba de la jornada
    lista_ventas = [120.50, 45.00, 89.90, 210.00, 65.40]
    tipo_cliente_str = "VIP"
    objetivo_diario_fl = 400.0
    
    print("\n1. Procesando lista de ventas del día...")
   
    total_bruto_fl = fn_ProcesarListaVentas_fl(lista_ventas)
    print(f"   Total bruto calculado: {total_bruto_fl:.2f}€")
    
    print(f"\n2. Aplicando descuento para cliente de tipo '{tipo_cliente_str}'...")
    total_neto_fl = fn_CalcularDescuento_fl(total_bruto_fl, tipo_cliente_str)
    print(f"   Total tras descuento: {total_neto_fl:.2f}€ (Valor esperado para 20% dto: {total_bruto_fl * 0.80:.2f}€)")
    
    print("\n3. Evaluando si se superó el objetivo diario...")
    exito_bool = fn_EvaluarObjetivoDiario_bool(total_neto_fl, objetivo_diario_fl)
    
    if exito_bool:
        print(f"   ¡ÉXITO! Se ha alcanzado el objetivo diario de {objetivo_diario_fl:.2f}€.")
    else:
        print(f"   ATENCIÓN: No se ha alcanzado el objetivo diario de {objetivo_diario_fl:.2f}€.")

if __name__ == "__main__":
    main()
