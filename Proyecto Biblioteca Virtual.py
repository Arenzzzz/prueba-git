# Hecho por: Arenz Peláez - 1556425

print("Bienvenido a la Biblioteca Virtual")

libros = [] # Lista para almacenar los libros

def agregar_libros(*titulos):   # Función para título de lo libros a la biblioteca
    for titulo in titulos:
        libro = {'título':titulo}
        libros.append(libro)
    
def asignar_detalles(titulo, autor, genero, año):   # Función para buscar libros y asignarle sus detalles
    encontrado = False
    for libro in libros:
        if libro['título'] == titulo:
            libro['autor'] = autor
            libro['género'] = genero
            libro['año'] = año
            encontrado = True
    if not encontrado:
        print("Libro no encontrado")
        
def mostrar_biblioteca():   # Función para mostrar los libros de la biblioteca
    print('*' * 50)
    print("BIBLIOTECA:")
    for i, libro in enumerate(libros, 1):   # Itera cada libro en la lista y los muestra enumerados y con sus detalles
        print(f'{i}-{libro.get('título')}')
        
        if len(libro) > 1:  # Verifica si el libro tiene detalles asignados
            print(
                f'\tAutor: {libro.get('autor')} - Género: {libro.get('género')} - Año: {libro.get('año')}'
                )
        else:   # Si no tiene detalles, muestra un mensaje
            print("El libro no cuenta con detalles, agrégalos")
            
def buscar_filtros(**filtros):  # Función para buscar libros por filtros
    print('*' * 50)
    print('BÚSQUEDA POR FILTRO:')
    
    for filtro in filtros:  # Itera sobre los filtros proporcionados
        encontrado = False

        if 'género' in filtro: # Filtra por género
            print(f'\nFiltrado por GÉNERO: {filtros.get('género')}')

            for libro in libros: # Itera sobre los libros para encontrar coincidencias
                if filtros.get('género') == libro.get('género'):
                    print(f'-{libro.get('título')}')
                    print(
                    f'\tAutor: {libro.get('autor')} - Género: {libro.get('género')} - Año: {libro.get('año')}'
                    )
                    encontrado = True
            if not encontrado:  # Avisa si no se encontró ningún libro con el género especificado
                print('NO ENCONTRADO')        
                    
        elif 'autor' in filtro: # Filtra por autor
            print(f'\nFiltrado por AUTOR: {filtros.get('autor')}')

            for libro in libros:    # Itera sobre los libros para encontrar coincidencias
                if filtros.get('autor') == libro.get('autor'):
                    print(f'-{libro.get('título')}')
                    print(
                    f'\tAutor: {libro.get('autor')} - Género: {libro.get('género')} - Año: {libro.get('año')}'
                    )
                    encontrado = True
            if not encontrado:  # Avisa si no se encontró ningún libro con el género especificado
                print('NO ENCONTRADO')
        
        elif 'año_max' in filtro:   # Filtra por año máximo de publicación
            print(f'\nFiltrado por AÑO MÁXIMO: {filtros.get('año_max')}')

            for libro in libros:    # Itera sobre los libros para encontrar coincidencias
                if 'año' in libro:  # Verifica si el libro tiene un año asignado
                    if int(filtros.get('año_max')) >= int(libro.get('año')):
                        print(f'-{libro.get('título')}')
                        print(
                        f'\tAutor: {libro.get('autor')} - Género: {libro.get('género')} - Año: {libro.get('año')}'
                        )
                        encontrado = True
            if not encontrado:  # Avisa si no se encontró ningún libro con el género especificado
                print('NO ENCONTRADO')
            
# Ejemplo de uso de las funciones
agregar_libros(
    'Viaje al centro de la Tierra',
    'Divina Comedia',
    'Hombres de maíz'
)

asignar_detalles(
    'Viaje al centro de la Tierra',
    'Julio Verne',
    'Novela',
    1800
)

asignar_detalles(
    'Divina Comedia',
    'Dante Alighieri',
    'Epopeya',
    1300
)

mostrar_biblioteca()

buscar_filtros(género='Comedia', año_max=2000, autor='Julio Verne')