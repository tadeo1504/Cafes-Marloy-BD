from backend.db.conexion import crear_conexion, cerrar_conexion

def reporte_total_mensual_por_cliente(mes=None, anio=None):
    """Suma del costo de alquiler de máquinas + insumos consumidos por cliente"""
    
    # Si no se recibieron parámetros, solicitarlos por consola
    if mes is None or anio is None:
        print("=== Reporte Total Mensual por Cliente ===")
        print("Este reporte muestra el total a cobrar a cada cliente por alquiler de máquinas e insumos consumidos.")
        
        while True:
            try:
                mes = int(input("Ingrese el mes (1-12): "))
                anio = int(input("Ingrese el año (YYYY): "))
                if not (1 <= mes <= 12):
                    raise ValueError("Mes debe estar entre 1 y 12.")
                if anio < 2000 or anio > 2100:
                    raise ValueError("Año debe estar entre 2000 y 2100.")
                break
            except ValueError as e:
                print(f"❌ Error: {e}. Intente nuevamente.")
    else:
        # Validar si los parámetros recibidos desde el front son correctos
        if not isinstance(mes, int) or not (1 <= mes <= 12):
            return {"ok": False, "mensaje": "Mes inválido"}
        if not isinstance(anio, int) or anio < 2000 or anio > 2100:
            return {"ok": False, "mensaje": "Año inválido"}
    
    # Una vez validados, continuar con la lógica
    conexion = crear_conexion(tipo="admin")
    if not conexion:
        return {"ok": False, "mensaje": "Error de conexión"}

    try:
        cursor = conexion.cursor(dictionary=True)
        query = """
            SELECT 
                c.nombre AS cliente,
                SUM(m.costo_alquiler_mensual) AS total_alquiler,
                SUM(rc.cantidad_usada * i.precio_unitario) AS total_consumo,
                SUM(m.costo_alquiler_mensual) + SUM(rc.cantidad_usada * i.precio_unitario) AS total
            FROM clientes c
            LEFT JOIN maquinas m ON m.id_cliente = c.id
            LEFT JOIN registro_consumo rc ON rc.id_maquina = m.id 
                AND MONTH(rc.fecha) = %s AND YEAR(rc.fecha) = %s
            LEFT JOIN insumos i ON i.id = rc.id_insumo
            GROUP BY c.id
            HAVING total > 0
            ORDER BY total DESC;
        """
        cursor.execute(query, (mes, anio))
        resultados = cursor.fetchall()
        
        if not resultados:
            print("📭 No se encontraron registros para el mes y año especificados.")
            return []

        print("\n📊 Reporte generado:\n")
        print(f"{'Cliente':<20} {'Alquiler ($)':>15} {'Consumo ($)':>15} {'Total ($)':>15}")
        print("-" * 65)
        for row in resultados:
            print(f"{row['cliente']:<20} {row['total_alquiler'] or 0:>15.2f} {row['total_consumo'] or 0:>15.2f} {row['total'] or 0:>15.2f}")
            return resultados
    finally:
        cerrar_conexion(conexion)


def reporte_insumos_mas_consumidos():
    """Top 10 de insumos más usados y su costo total"""
    conexion = crear_conexion(tipo="admin")
    if not conexion:
        return

    try:
        cursor = conexion.cursor(dictionary=True)
        query = """
        SELECT 
            i.descripcion,
            SUM(rc.cantidad_usada) AS total_usado,
            i.precio_unitario,
            SUM(rc.cantidad_usada * i.precio_unitario) AS costo_total
        FROM insumos i
        JOIN registro_consumo rc ON rc.id_insumo = i.id
        GROUP BY i.id
        ORDER BY total_usado DESC
        LIMIT 10
        """
        cursor.execute(query)
        resultados = cursor.fetchall()
        if not resultados:
            print("📭 No se encontraron insumos consumidos.")
            return
        print("\n📊 Top 10 Insumos Más Consumidos:\n")
        print(f"{'Descripción':<30} {'Total Usado':>15} {'Precio Unitario':>15} {'Costo Total':>15}")
        print("-" * 75) #esto es para alinear las columnas jsakjs
        for row in cursor.fetchall():
            print(f"{row['descripcion']:<30} {row['total_usado']:>15} {row['precio_unitario']:>15} {row['costo_total']:>15}")

        return resultados
    finally:
        cerrar_conexion(conexion)


def reporte_tecnicos_mas_mantenimientos():
    """Técnicos que realizaron más mantenimientos"""
    conexion = crear_conexion(tipo="admin")
    if not conexion:
        return

    try:
        cursor = conexion.cursor(dictionary=True)
        query = """
        SELECT 
            t.nombre,
            t.apellido,
            COUNT(m.id) AS total_mantenimientos
        FROM tecnicos t
        LEFT JOIN mantenimientos m ON m.ci_tecnico = t.ci
        GROUP BY t.ci
        ORDER BY total_mantenimientos DESC
        """
        cursor.execute(query)
        # Verificar si se encontraron resultados
        resultados = cursor.fetchall()
        if  not resultados:
            print("📭 No se encontraron mantenimientos registrados.")
            return
        print("\n📊 Técnicos con Más Mantenimientos:\n")
        print(f"{'Nombre':<20} {'Apellido':<20} {'Total Mantenimientos':>20}")
        print("-" * 60)
        for row in resultados:
            print(f"{row['nombre']:<20} {row['apellido']:<20} {row['total_mantenimientos']:>20}")
        return resultados
    finally:
        cerrar_conexion(conexion)


def reporte_clientes_con_mas_maquinas():
    """Clientes con más máquinas instaladas"""
    conexion = crear_conexion(tipo="admin")
    if not conexion:
        return

    try:
        cursor = conexion.cursor(dictionary=True)
        query = """
        SELECT 
            c.nombre,
            COUNT(m.id) AS cantidad_maquinas
        FROM clientes c
        LEFT JOIN maquinas m ON m.id_cliente = c.id
        GROUP BY c.id
        HAVING cantidad_maquinas > 0
        ORDER BY cantidad_maquinas DESC
        """
        cursor.execute(query)
        resultados = cursor.fetchall()
        if not resultados:
            print("📭 No se encontraron clientes con máquinas registradas.")
            return []
        print("\n📊 Clientes con Más Máquinas Instaladas:\n")
        print(f"{'Cliente':<30} {'Cantidad de Máquinas':>20}")
        print("-" * 60)
        for row in resultados:
            print(f"{row['nombre']:<30} {row['cantidad_maquinas']:>20}")
        return resultados
    finally:
        cerrar_conexion(conexion)
