import sqlite3

def crear_database():
    crear_tablas()
    insertar_datos()

def crear_tablas():
    conn = sqlite3.connect("Clue.db")
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS PERSONAJES (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        _nombre TEXT,
        _oficio TEXT,
        _imagen TEXT
    )''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS LUGARES (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        _nombre TEXT,
        _descripcion TEXT,
        _imagen TEXT
    )''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ARMAS (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        _nombre TEXT,
        _descripcion TEXT,
        _imagen TEXT
    )''')
    
    conn.commit()
    conn.close()
    
def insertar_datos():
    conn = sqlite3.connect("Clue.db")
    cursor = conn.cursor()
    
    personajes = [
        ("Samuel", "Ingeniero", "imagenes/Personajes/Ingeniero.png"),
        ("Catty", "Mucama",     "imagenes/Personajes/Mucama.png"),
        ("Foxy", "Inventor",    "imagenes/Personajes/Inventor.png"),
        ("Rene",  "General",    "imagenes/Personajes/General.png"),
        ("Angela", "Artista",   "imagenes/Personajes/Artista.png")
    ]
    cursor.executemany("INSERT OR IGNORE INTO PERSONAJES VALUES (NULL, ?,?,?)", personajes)
    
    lugares = [
        ("Habitación",  "Descripción", "imagenes/Lugares/Habitacion.png"),
        ("Cocina",      "Descripción", "imagenes/Lugares/Cocina.png"),
        ("Biblioteca",  "Descripción", "imagenes/Lugares/Biblioteca.png"),
        ("Baño",        "Descripción", "imagenes/Lugares/Bano.png"),
        ("Sótano",      "Descripción", "imagenes/Lugares/Zotano.png")
    ]
    cursor.executemany("INSERT OR IGNORE INTO LUGARES VALUES (NULL, ?,?,?)", lugares)
    
    armas = [
        ("Pistola",     "Descripcion", "imagenes/Armas/Pistola.png"),
        ("Grillete",    "Descripcion", "imagenes/Armas/Grillete.png"),
        ("Espada",      "Descripcion", "imagenes/Armas/Espada.png"),
        ("Cuerda",      "Descripcion", "imagenes/Armas/Cuerda.png"),
        ("Candelabro",  "Descripcion", "imagenes/Armas/Candelabro.png")
    ]
    cursor.executemany("INSERT OR IGNORE INTO ARMAS VALUES (NULL, ?,?,?)", armas)
    
    conn.commit()
    conn.close()
    
def obtener_datos():
    conn = sqlite3.connect("Clue.db")
    cursor = conn.cursor()
    
    personajes = "SELECT * FROM PERSONAJES"
    cursor.execute(personajes)
    lista_personajes = cursor.fetchall()
    
    lugares = "SELECT * FROM LUGARES"
    cursor.execute(lugares)
    lista_lugares = cursor.fetchall()
    
    armas = "SELECT * FROM ARMAS"
    cursor.execute(armas)
    lista_armas = cursor.fetchall()
    
    conn.close()
    
    return lista_personajes, lista_lugares, lista_armas