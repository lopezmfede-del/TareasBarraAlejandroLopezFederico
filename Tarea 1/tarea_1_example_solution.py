def count_char(cadena, caracter):
    # Definición de codigos de exito y erores
    EXITO = 0
    ERROR_TIPO_CADENA = -100
    ERROR_FORMATO_CADENA = -200
    ERROR_CARACTER = -300

    # Primero, verificar que 'cadena' es un string
    if not isinstance(cadena, str):
        return ERROR_TIPO_CADENA, None
    
    # Segundo, verificar que la cadena solo tenga numeros y letras
    if not all (c.isalnum() for c in cadena):
        return ERROR_FORMATO_CADENA, None
    
    # Tercero, verificar que 'caracter' sea un único carácter alfanumérico
    if not (isinstance(caracter, str) and len(caracter) == 1 and caracter.isalnum()):
        return ERROR_CARACTER, None
    
    # Cuarto, contar cantidad de veces que aparece 'caracter' en 'cadena'
    cantidad = cadena.count(caracter)
    
    # Finalmente, retornar el código de éxito y la cantidad
    return EXITO, cantidad

def multiplo_2(base,multiplo):
    ERROR_PARAMETROS = -400
    ERROR_MULTIPLO = -500
    EXITO = 0
    # Los dos tienen que ser enteros y no negativos (0 permitido por el test)
    if not isinstance(base, int) or not isinstance(multiplo,int) or base < 0 or multiplo < 0:
        return ERROR_PARAMETROS, None
    # Multiplo debe estar en el conjunto permitido
    if multiplo not in (1, 2, 4, 8, 16):
        return ERROR_MULTIPLO, None
    
    return EXITO, base*multiplo
    

