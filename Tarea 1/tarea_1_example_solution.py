def count_char(cadena, caracter):
    #Definición de codigos de exito y erores
    EXITO = 0
    ERROR_TIPO_CADENA = -100
    ERROR_FORMATO_CADENA = -200
    ERROR_CARACTER = -300

    #Primero, verificar que 'cadena' es un string
    if not isinstance(cadena, str):
        return ERROR_TIPO_CADENA, None
