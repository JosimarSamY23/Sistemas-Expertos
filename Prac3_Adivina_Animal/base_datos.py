import sqlite3

def crear_database():
    crear_tabla_mamiferos()
    crear_tabla_reptiles()
    crear_tabla_anfibios()
    crear_tabla_peces()
    crear_tabla_aves()
    crear_tabla_insectos()
    crear_tabla_aracnidos()
    
    insertar_datos()

def crear_tabla_mamiferos():
    conn = sqlite3.connect("Adivina_Animal.db")
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Animales_Mamiferos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        _nombre TEXT,
        _imagen TEXT,
        _jugado INTEGER,
        nadar INTEGER,
        cavar INTEGER,
        cazar INTEGER,
        volar INTEGER,
        saltar INTEGER,
        es_felino INTEGER,
        es_primate INTEGER,
        es_roedor INTEGER,
        es_marsupial INTEGR,
        es_acuatico INTEGER,
        es_carnivoro INTEGER,
        es_nocturno INTEGER,
        es_domestico INTEGER,
        es_de_granja INTEGER,
        es_del_desierto INTEGER,
        es_del_bosque INTEGER,
        es_de_la_montana INTEGER,
        tiene_manada INTEGER,
        tiene_cuernos INTEGER,
        tiene_pezunas INTEGER
    )''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Preguntas_Mamiferos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pregunta TEXT,
        descripcion TEXT,
        imagen TEXT
    )''')
    
    conn.commit()
    conn.close()

def crear_tabla_reptiles():
    conn = sqlite3.connect("Adivina_Animal.db")
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Animales_Reptiles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        _nombre TEXT,
        _imagen TEXT,
        _jugado INTEGER,
        nadar INTEGER,
        cazar INTEGER,
        muda_piel INTEGER,
        es_carnivoro INTEGER,
        es_nocturno INTEGER,
        es_venenoso INTEGER,
        se_regenera INTEGER,
        se_arrastra INTEGER,
        tiene_escamas INTEGER,
        tiene_caparazon INTEGER
    )''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Preguntas_Reptiles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pregunta TEXT,
        descripcion TEXT,
        imagen TEXT
    )''')
    
    conn.commit()
    conn.close()

def crear_tabla_anfibios():
    conn = sqlite3.connect("Adivina_Animal.db")
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Animales_Anfibios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        _nombre TEXT,
        _imagen TEXT,
        _jugado INTEGER,
        saltar INTEGER,
        muda_piel INTEGER,
        respira_piel INTEGER,
        habitad_humeda INTEGER,
        es_nocturno INTEGER,
        es_carnivoro INTEGER,
        es_venenoso INTEGER,
        se_regenera INTEGER,
        se_arrastra INTEGER
    )''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Preguntas_Anfibios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pregunta TEXT,
        descripcion TEXT,
        imagen TEXT
    )''')
    
    conn.commit()
    conn.close()

def crear_tabla_peces():
    conn = sqlite3.connect("Adivina_Animal.db")
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Animales_Peces (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        _nombre TEXT,
        _imagen TEXT,
        _jugado INTEGER,
        es_nocturno INTEGER,
        es_carnivoro INTEGER,
        es_venenoso INTEGER,
        vive_en_agua_dulce INTEGER,
        es_migratorio INTEGER,
        tiene_escamas INTEGER,
        tiene_aletas_venenosas INTEGER,
        es_luminoso INTEGER
    )''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Preguntas_Peces (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pregunta TEXT,
        descripcion TEXT,
        imagen TEXT
    )''')
    
    conn.commit()
    conn.close()

def crear_tabla_aves():
    conn = sqlite3.connect("Adivina_Animal.db")
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Animales_Aves (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        _nombre TEXT,
        _imagen TEXT,
        _jugado INTEGER,
        volar INTEGER,
        nadar INTEGER,
        migrar INTEGER,
        es_nocturno INTEGER,
        es_carnivoro INTEGER,
        tiene_plumas INTEGER,
        es_domestica INTEGER,
        pone_huevos_coloreados INTEGER,
        es_cantora INTEGER,
        tiene_pico_curvo INTEGER
    )''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Preguntas_Aves (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pregunta TEXT,
        descripcion TEXT,
        imagen TEXT
    )''')
    
    conn.commit()
    conn.close()
    
def crear_tabla_insectos():
    conn = sqlite3.connect("Adivina_Animal.db")
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Animales_Insectos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        _nombre TEXT,
        _imagen TEXT,
        _jugado INTEGER,
        cazar INTEGER,
        volar INTEGER,
        es_venenoso INTEGER,
        es_carnivoro INTEGER,
        se_arrastra INTEGER,
        tiene_exoesqueleto INTEGER,
        tiene_metamorfosis INTEGER,
        tiene_caparazon INTEGER,
        tiene_antenas INTEGER,
        vive_en_colonia INTEGER,
        es_nocturno INTEGER
    )''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Preguntas_Insectos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pregunta TEXT,
        descripcion TEXT,
        imagen TEXT
    )''')
    
    conn.commit()
    conn.close()
    
def crear_tabla_aracnidos():
    conn = sqlite3.connect("Adivina_Animal.db")
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Animales_Aracnidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        _nombre TEXT,
        _imagen TEXT,
        _jugado INTEGER,
        cazar INTEGER,
        es_venenoso INTEGER,
        es_carnivoro INTEGER,
        tiene_exoesqueleto INTEGER,
        tiene_metamorfosis INTEGER,
        tiene_caparazon INTEGER,
        tiene_antenas INTEGER,
        tiene_multiples_patas INTEGER,
        teje_tela INTEGER,
        es_nocturno INTEGER
    )''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Preguntas_Aracnidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pregunta TEXT,
        descripcion TEXT,
        imagen TEXT
    )''')
    
    conn.commit()
    conn.close()

def insertar_datos():
    insertar_mamiferos()
    insetar_reptiles()
    insertar_anfibios()
    insertar_peces()
    insertar_aves()
    insertar_insectos()
    insertar_aracnidos()

def insertar_mamiferos():
    conn = sqlite3.connect("Adivina_Animal.db")
    cursor = conn.cursor()
                                                ##|1| 2| 3| 4| 5| 6| 7| 8| 9|10|11|12|13|14|15|16|17|18|19|20|
    animales_mamiferos = [
    ("León", "imagenes/leon.jpg",               0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1),
    ("Tigre", "imagenes/tigre.jpg",             0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1),
    ("Perro", "imagenes/perro.jpg",             0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1),
    ("Gato", "imagenes/gato.jpg",               0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1),
    ("Elefante", "imagenes/elefante.jpg",       0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1),
    ("Delfín", "imagenes/delfin.jpg",           0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0),
    ("Ballena", "imagenes/ballena.jpg",         0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0),
    ("Murciélago", "imagenes/murcielago.jpg",   0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0),
    ("Canguro", "imagenes/canguro.jpg",         0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1),
    ("Vaca", "imagenes/vaca.jpg",               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1),
    ("Mono", "imagenes/mono.jpg",               0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1),
    ("Oso", "imagenes/oso.jpg",                 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1),
    ("Caballo", "imagenes/caballo.jpg",         0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1),
    ("Ratón", "imagenes/raton.jpg",             0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1),
    ("Conejo", "imagenes/conejo.jpg",           0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1),
    ("Mapache", "imagenes/mapache.jpg",         0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1),
    ("Zorro", "imagenes/zorro.jpg",             0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1),
    ("Burro", "imagenes/burro.jpg",             0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1),
    ("Chinchilla", "imagenes/chinchilla.jpg",   0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1),
    ("Armadillo", "imagenes/armadillo.jpg",     0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1),
    ("Ciervo", "imagenes/ciervo.jpg",           0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1),
    ("Reno", "imagenes/reno.jpg",               0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1),
    ("Hipopótamo", "imagenes/hipopotamo.jpg",   0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1),
    ("Rinoceronte", "imagenes/rinoceronte.jpg", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1),
    ("Jirafa", "imagenes/jirafa.jpg",           0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1),
    ("Nutria", "imagenes/nutria.jpg",           0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1),
    ("Topo", "imagenes/topo.jpg",               0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1),
    ("Ornitorrinco", "imagenes/ornito.jpg",     0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1),
    ("Puercoespín", "imagenes/puercoespin.jpg", 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1),
    ("Erizo", "imagenes/erizo.jpg",             0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1),
    ("Búfalo", "imagenes/bufalo.jpg",           0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1),
    ("Camello", "imagenes/camello.jpg",         0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1),
    ("Lobo", "imagenes/lobo.jpg",               0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1),
    ("Chita", "imagenes/chita.jpg",             0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1),
    ("Cabra", "imagenes/cabra.jpg",             0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1),
    ("Cerdo", "imagenes/cerdo.jpg",             0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1),
    ("Koala", "imagenes/koala.jpg",             0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1),
    ("Oveja", "imagenes/oveja.jpg",             0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1),
    ("Toro", "imagenes/toro.jpg",               0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1)
    ]
    cursor.executemany("INSERT OR IGNORE INTO Animales_Mamiferos VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", animales_mamiferos)
    
    preguntas_mamiferos = [
    ("¿Puede nadar de forma natural o instintiva?", "Nada", ""),
    ("¿Cava tierra o túneles como parte de su comportamiento?", "Cava", ""),
    ("¿Caza presas para alimentarse?", "Caza", ""),
    ("¿Es capaz de volar? (aunque sea planeando)", "Vuela", ""),
    ("¿Puede saltar distancias considerables para moverse?", "Salta", ""),
    ("¿Pertenece a la familia de los felinos (gatos, leones, tigres, etc.)?", "Felino", ""),
    ("¿Es un primate? (monos, simios, etc.)", "Primate", ""),
    ("¿Es un roedor? (ratones, ratas, ardillas, etc.)", "Roedor", ""),
    ("¿Es un marsupial? (tiene una bolsa para sus crías, como el canguro o el koala)", "Marsupial", ""),
    ("¿Vive principalmente en ambientes acuáticos?", "Acuático", ""),
    ("¿Se alimenta principalmente de carne?", "Carnívoro", ""),
    ("¿Es activo principalmente durante la noche?", "Nocturno", ""),
    ("¿Comúnmente convive con humanos como mascota o en el hogar?", "Doméstico", ""),
    ("¿Comúnmente se cría en granjas?", "De granja", ""),
    ("¿Está adaptado para vivir en climas áridos como los desiertos?", "Vive desierto", ""),
    ("¿Vive principalmente en ecosistemas de bosques?", "Vive bosque", ""),
    ("¿Habita en zonas montañosas o altas altitudes?", "Vive montaña", ""),
    ("¿Vive y se desplaza en grupos (manadas, rebaños, etc.)?", "Grupo", ""),
    ("¿Tiene cuernos visibles en su cabeza?", "Cuernos", ""),
    ("¿Tiene pezuñas en lugar de garras o patas con dedos?", "Pezuñas", "")
    ]
    cursor.executemany("INSERT OR IGNORE INTO Preguntas_Mamiferos VALUES (NULL, ?, ?, ?)", preguntas_mamiferos)
    
    conn.commit()
    conn.close()

def insetar_reptiles():
    conn = sqlite3.connect("Adivina_Animal.db")
    cursor = conn.cursor()
                                                ##|1| 2| 3| 4| 5| 6| 7| 8| 9|10|
    animales_reptiles = [
    ("Cocodrilo", "imagenes/cocodrilo.jpg",     0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0),
    ("Serpiente", "imagenes/serpiente.jpg",     0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0),
    ("Iguana", "imagenes/iguana.jpg",           0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0),
    ("Camaleón", "imagenes/camaleon.jpg",       0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0),
    ("Tortuga", "imagenes/tortuga.jpg",         0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1),
    ("Lagarto", "imagenes/lagarto.jpg",         0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0),
    ("Gecko", "imagenes/gecko.jpg",             0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0),
    ("Anolis", "imagenes/anolis.jpg",           0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0),
    ("Boa", "imagenes/boa.jpg",                 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0),
    ("Víbora", "imagenes/vibora.jpg",           0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0),
    ("Komodo", "imagenes/dragon_komodo.jpg",    0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0),
    ("Escinco", "imagenes/escinco.jpg",         0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0),
    ]
    cursor.executemany("INSERT OR IGNORE INTO Animales_Reptiles VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", animales_reptiles)
    
    preguntas_reptiles = [
    ("¿Puede nadar o pasa tiempo en el agua?", "Nada", ""),
    ("¿Caza para alimentarse?", "Caza", ""),
    ("¿Muda su piel regularmente?", "Muda de piel", ""),
    ("¿Se alimenta principalmente de carne?", "Carnivoro", ""),
    ("¿Es activo principalmente durante la noche?", "Nocturno", ""),
    ("¿Posee veneno?", "es_venenoso", ""),
    ("¿Puede regenerar partes de su cuerpo como la cola?", "Se regenera", ""),
    ("¿Se mueve arrastrándose?", "Se arrastra", ""),
    ("¿Tiene escamas en su cuerpo?", "Escamas", ""),
    ("¿Tiene un caparazón?", "Caparazon", "")
    ]
    cursor.executemany("INSERT OR IGNORE INTO Preguntas_Reptiles VALUES (NULL, ?, ?, ?)", preguntas_reptiles)
    
    conn.commit()
    conn.close()

def insertar_anfibios():
    conn = sqlite3.connect("Adivina_Animal.db")
    cursor = conn.cursor()
                                                    ##|1| 2| 3| 4| 5| 6| 7| 8| 9|
    animales_anfibios = [
    ("Rana", "imagenes/rana.jpg",                   0, 1, 1, 1, 1, 0, 1, 0, 0, 0),
    ("Sapo", "imagenes/sapo.jpg",                   0, 1, 1, 1, 1, 1, 1, 0, 0, 0),
    ("Axolote", "imagenes/axolote.jpg",             0, 0, 1, 1, 1, 0, 0, 0, 1, 0),
    ("Tritón", "imagenes/triton.jpg",               0, 0, 1, 1, 1, 1, 1, 0, 1, 1),
    ("Cecilia", "imagenes/cecilia.jpg",             0, 0, 1, 1, 1, 1, 1, 0, 1, 1),
    ("Salamandra", "imagenes/salamandra.jpg",       0, 0, 1, 1, 1, 1, 1, 0, 1, 1)
    ]
    cursor.executemany("INSERT OR IGNORE INTO Animales_Anfibios VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", animales_anfibios)
    
    preguntas_anfibios = [
    ("¿Puede saltar?", "Saltar", ""),
    ("¿Muda su piel regularmente?", "Muda de piel", ""),
    ("¿Puede respirar a través de la piel?", "Respira por la piel", ""),
    ("¿Vive en un hábitat húmedo?", "Habitad humeda", ""),
    ("¿Es activo principalmente durante la noche?", "Nocturno", ""),
    ("¿Se alimenta principalmente de carne?", "Carnivoro", ""),
    ("¿Posee veneno?", "Venenoso", ""),
    ("¿Puede regenerar partes de su cuerpo?", "Regenera", ""),
    ("¿Se mueve arrastrándose?", "Arrastra", "")
    ]
    cursor.executemany("INSERT OR IGNORE INTO Preguntas_Anfibios VALUES (NULL, ?, ?, ?)", preguntas_anfibios)
    
    conn.commit()
    conn.close()
    
def insertar_peces():
    conn = sqlite3.connect("Adivina_Animal.db")
    cursor = conn.cursor()
                                                        ##|1| 2| 3| 4| 5| 6| 7| 8|
    animales_peces = [
    ("Salmón", "imagenes/salmon.jpg",                   0, 0, 1, 0, 1, 1, 1, 0, 0),
    ("Pez payaso", "imagenes/pez_payaso.jpg",           0, 0, 0, 0, 0, 0, 1, 0, 0),
    ("Pez globo", "imagenes/pez_globo.jpg",             0, 0, 1, 1, 0, 0, 1, 0, 0),
    ("Pez león", "imagenes/pez_leon.jpg",               0, 1, 1, 1, 0, 1, 1, 1, 0),
    ("Tiburón", "imagenes/tiburon.jpg",   0, 0, 1, 0, 0, 0, 0, 0, 0),
    ("Anguila eléctrica", "imagenes/anguila.jpg",       0, 1, 1, 0, 1, 0, 0, 0, 0),
    ("Pez linterna", "imagenes/pez_linterna.jpg",       0, 1, 1, 0, 0, 0, 0, 0, 1),
    ("Trucha", "imagenes/trucha.jpg",                   0, 0, 1, 0, 1, 1, 1, 0, 0),
    ("Pez gato", "imagenes/pez_gato.jpg",               0, 1, 1, 0, 1, 1, 1, 0, 0),
    ("Caballito de mar", "imagenes/caballito_mar.jpg",  0, 0, 0, 0, 0, 1, 0, 0, 0),
    ]
    cursor.executemany("INSERT OR IGNORE INTO Animales_Peces VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", animales_peces)
    
    preguntas_peces = [
    ("¿Es activo principalmente durante la noche?", "Nocturno", ""),
    ("¿Se alimenta principalmente de carne?", "Carnivoro", ""),
    ("¿Es venenoso?", "Venenoso", ""),
    ("¿Vive en agua dulce?", "vive agua dulce", ""),
    ("¿Migra durante su vida?", "Migratorio", ""),
    ("¿Tiene escamas visibles?", "Escamas", ""),
    ("¿Tiene aletas venenosas?", "Aletas venenosas", ""),
    ("¿Emite luz propia?", "Luminoso", "")
    ]
    cursor.executemany("INSERT OR IGNORE INTO Preguntas_Peces VALUES (NULL, ?, ?, ?)", preguntas_peces)
    
    conn.commit()
    conn.close()
    
def insertar_aves():
    conn = sqlite3.connect("Adivina_Animal.db")
    cursor = conn.cursor()
                                                ##|1| 2| 3| 4| 5| 6| 7| 8| 9|10|
    animales_aves = [
    ("Águila", "imagenes/aguila.jpg",           0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1),
    ("Pingüino", "imagenes/pinguino.jpg",       0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0),
    ("Loro", "imagenes/loro.jpg",               0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1),
    ("Búho", "imagenes/buho.jpg",               0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1),
    ("Colibrí", "imagenes/colibri.jpg",         0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0),
    ("Pato", "imagenes/pato.jpg",               0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0),
    ("Canario", "imagenes/canario.jpg",         0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0),
    ("Avestruz", "imagenes/avestruz.jpg",       0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0),
    ("Flamenco", "imagenes/flamenco.jpg",       0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0),
    ("Gallo", "imagenes/gallo.jpg",             0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0)
    ]
    cursor.executemany("INSERT OR IGNORE INTO Animales_Aves VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", animales_aves)
    
    preguntas_aves = [
    ("¿Puede volar?", "Volar", ""),
    ("¿Puede nadar?", "Nadar", ""),
    ("¿Realiza migraciones?", "Migrar", ""),
    ("¿Es activa principalmente de noche?", "Nocturno", ""),
    ("¿Se alimenta principalmente de carne?", "Carnivoro", ""),
    ("¿Tiene plumas visibles?", "Plumas", ""),
    ("¿Es un ave doméstica o de granja?", "Domestica", ""),
    ("¿Pone huevos con colores distintos al blanco?", "Huevos coloreados", ""),
    ("¿Es conocida por su canto?", "Cantora", ""),
    ("¿Tiene el pico curvado?", "Pico curvo", "")
    ]
    cursor.executemany("INSERT OR IGNORE INTO Preguntas_Aves VALUES (NULL, ?, ?, ?)", preguntas_aves)
    
    conn.commit()
    conn.close()
    
def insertar_insectos():
    conn = sqlite3.connect("Adivina_Animal.db")
    cursor = conn.cursor()
                                                    ##|1| 2| 3| 4| 5| 6| 7| 8| 9|10|11|
    animales_insectos = [
    ("Hormiga", "imagenes/hormiga.jpg",             0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0),
    ("Abeja", "imagenes/abeja.jpg",                 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0),
    ("Mariposa", "imagenes/mariposa.jpg",           0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0),
    ("Escarabajo", "imagenes/escarabajo.jpg",       0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0),
    ("Mantis religiosa", "imagenes/mantis.jpg",     0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0),
    ("Cucaracha", "imagenes/cucaracha.jpg",         0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1),
    ("Polilla", "imagenes/polilla.jpg",             0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1),
    ("Grillo", "imagenes/grillo.jpg",               0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1),
    ("Mosquito", "imagenes/mosquito.jpg",           0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1),
    ("Libélula", "imagenes/libelula.jpg",           0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0)
    ]
    cursor.executemany("INSERT OR IGNORE INTO Animales_Insectos VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", animales_insectos)
    
    preguntas_insectos = [
    ("¿Caza a otros insectos?", "Cazar", ""),
    ("¿Puede volar?", "Volar", ""),
    ("¿Es venenoso?", "Venenoso", ""),
    ("¿Se alimenta de carne?", "Carnivoro", ""),
    ("¿Se arrastra?", "Arrastra", ""),
    ("¿Tiene un exoesqueleto visible?", "Exoesqueleto", ""),
    ("¿Pasa por una metamorfosis?", "Metamorfosis", ""),
    ("¿Tiene un caparazón duro?", "Caparazon", ""),
    ("¿Tiene antenas visibles?", "Antenas", ""),
    ("¿Vive en colonia con otros insectos?", "vive en colonia", ""),
    ("¿Es activo principalmente durante la noche?", "Nocturno", "")
    ]
    cursor.executemany("INSERT OR IGNORE INTO Preguntas_Insectos VALUES (NULL, ?, ?, ?)", preguntas_insectos)
    
    conn.commit()
    conn.close()
    
def insertar_aracnidos():
    conn = sqlite3.connect("Adivina_Animal.db")
    cursor = conn.cursor()
                                                        ##|1| 2| 3| 4| 5| 6| 7| 8| 9|10|
    animales_aracnidos = [
    ("Tarántula", "imagenes/tarantula.jpg",             0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1),
    ("Escorpión", "imagenes/escorpion.jpg",             0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1),
    ("Viuda negra", "imagenes/viuda_negra.jpg",   0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1),
    ("Ácaro", "imagenes/acaro.jpg",                     0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0),
    ("Araña saltarina", "imagenes/arana_saltarina.jpg", 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1)
    ]
    cursor.executemany("INSERT OR IGNORE INTO Animales_Aracnidos VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", animales_aracnidos)
    
    preguntas_aracnidos = [
    ("¿Caza para alimentarse?", "Cazar", ""),
    ("¿Es venenoso?", "Venenoso", ""),
    ("¿Se alimenta de carne?", "Carnivoro", ""),
    ("¿Tiene un exoesqueleto visible?", "Exoesqueleto", ""),
    ("¿Pasa por metamorfosis?", "Metamorfosis", ""),
    ("¿Tiene un caparazón?", "Caparazon", ""),
    ("¿Tiene antenas?", "Antenas", ""),
    ("¿Tiene múltiples patas?", "Multiples patas", ""),
    ("¿Teje telarañas?", "Tejedora", ""),
    ("¿Es activo principalmente durante la noche?", "Nocturno", "")
    ]
    cursor.executemany("INSERT OR IGNORE INTO Preguntas_Aracnidos VALUES (NULL, ?, ?, ?)", preguntas_aracnidos)
    
    conn.commit()
    conn.close()
    
def obtener_datos(categoria, animales=True, preguntas=True):
    conn = sqlite3.connect("Adivina_Animal.db")
    cursor = conn.cursor()
    
    if animales:
        tabla_animales  = "SELECT * FROM Animales_"+categoria
        cursor.execute(tabla_animales)
        animales = cursor.fetchall()
    
    if preguntas:
        tabla_preguntas = "SELECT * FROM Preguntas_"+categoria
        cursor.execute(tabla_preguntas)
        preguntas = cursor.fetchall()
    
    conn.close()
    
    return animales, preguntas

def insertar_animal(nuevo_animal, categoria):
    if categoria == "Mamiferos":
        insertar_mamifero(nuevo_animal)
        
    elif categoria == "Reptiles":
        insertar_reptil(nuevo_animal)
        
    elif categoria == "Anfibios":
        insertar_anfibio(nuevo_animal)
        
    elif categoria == "Peces":
        insertar_pez(nuevo_animal)
        
    elif categoria == "Aves":
        insertar_ave(nuevo_animal)
        
    elif categoria == "Insectos":
        insertar_insecto(nuevo_animal)
        
    elif categoria == "Aracnidos":
        insertar_aracnido(nuevo_animal)

def insertar_mamifero(nuevo_animal):
    conn = sqlite3.connect("Adivina_Animal.db")
    cursor = conn.cursor()
    
    query = '''INSERT INTO Animales_Mamiferos (
            _nombre, _imagen, _jugado, nadar, cavar, cazar, volar, saltar, es_felino, es_primate, es_roedor,
            es_marsupial, es_acuatico, es_carnivoro, es_nocturno, es_domestico, es_de_granja, es_del_desierto,
            es_del_bosque, es_de_la_montana, tiene_manada, tiene_cuernos, tiene_pezunas 
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    
    cursor.execute(query, nuevo_animal)
    conn.commit()
    conn.close()

def insertar_reptil(nuevo_animal):
    conn = sqlite3.connect("Adivina_Animal.db")
    cursor = conn.cursor()
    
    query = '''INSERT INTO Animales_Reptiles (
            _nombre, _imagen, _jugado, nadar, cazar, muda_piel, es_carnivoro, es_nocturno, es_venenoso, se_regenera,
            se_arrastra, tiene_escamas, tiene_caparazon) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            
    cursor.execute(query, nuevo_animal)
    conn.commit()
    conn.close()
    
def insertar_anfibio(nuevo_animal):
    conn = sqlite3.connect("Adivina_Animal.db")
    cursor = conn.cursor()
    
    query = '''INSERT INTO Animales_Anfibios (
            _nombre, _imagen, _jugado, saltar, muda_piel, respira_piel, habitad_humeda, es_nocturno, es_carnivoro, 
            es_venenoso, se_regenera, se_arrastra) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            
    cursor.execute(query, nuevo_animal)
    conn.commit()
    conn.close()
    
def insertar_pez(nuevo_animal):
    conn = sqlite3.connect("Adivina_Animal.db")
    cursor = conn.cursor()
    
    query = query = '''INSERT INTO Animales_Peces (
            _nombre, _imagen, _jugado, es_nocturno, es_carnivoro, es_venenoso, vive_en_agua_dulce, es_migratorio,
            tiene_escamas, tiene_aletas_venenosas, es_luminoso) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            
    cursor.execute(query, nuevo_animal)
    conn.commit()
    conn.close()
    
def insertar_ave(nuevo_animal):
    conn = sqlite3.connect("Adivina_Animal.db")
    cursor = conn.cursor()
    
    query = '''INSERT INTO Animales_Aves (
            _nombre, _imagen, _jugado, volar, nadar, migrar, es_nocturno, es_carnivoro, tiene_plumas,
            es_domestica, pone_huevos_coloreados, es_cantora, tiene_pico_curvo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            
    cursor.execute(query, nuevo_animal)
    conn.commit()
    conn.close()
    
def insertar_insecto(nuevo_animal):
    conn = sqlite3.connect("Adivina_Animal.db")
    cursor = conn.cursor()
    
    query = '''INSERT INTO Animales_Insectos (
            _nombre, _imagen, _jugado, cazar, volar, es_venenoso, es_carnivoro, se_arrastra, tiene_exoesqueleto, tiene_metamorfosis,
            tiene_caparazon, tiene_antenas, vive_en_colonia, es_nocturno) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            
    cursor.execute(query, nuevo_animal)
    conn.commit()
    conn.close()
    
def insertar_aracnido(nuevo_animal):
    conn = sqlite3.connect("Adivina_Animal.db")
    cursor = conn.cursor()
    
    query = '''INSERT INTO Animales_Aracnidos (
            _nombre, _imagen, _jugado, cazar, es_venenoso, es_carnivoro, tiene_exoesqueleto, tiene_metamorfosis,
            tiene_caparazon, tiene_antenas, tiene_multiples_patas, teje_tela, es_nocturno) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            
    cursor.execute(query, nuevo_animal)
    conn.commit()
    conn.close()
    
def actualizar_valor(categoria, nombre_animal, valor_nuevo):
    if categoria == "Mamiferos":
        actualizar_mamifero(nombre_animal,valor_nuevo)
                
    elif categoria == "Reptiles":
        actualizar_reptil(nombre_animal,valor_nuevo)
        
    elif categoria == "Anfibios":
        actualizar_anfibio(nombre_animal,valor_nuevo)
        
    elif categoria == "Peces":
        actualizar_pez(nombre_animal,valor_nuevo)
        
    elif categoria == "Aves":
        actualizar_ave(nombre_animal,valor_nuevo)
        
    elif categoria == "Insectos":
        actualizar_insecto(nombre_animal,valor_nuevo)
    
    elif categoria == "Aracnidos":
        actualizar_aracnido(nombre_animal,valor_nuevo)
    
def actualizar_mamifero(nombre_animal,valor_nuevo):
    conn = sqlite3.connect("Adivina_Animal.db")
    cursor = conn.cursor()
    
    cursor.execute("""UPDATE Animales_Mamiferos SET _jugado = ? WHERE _nombre = ?""", (valor_nuevo, nombre_animal))
    
    conn.commit()
    conn.close()
    
def actualizar_reptil(nombre_animal,valor_nuevo):
    conn = sqlite3.connect("Adivina_Animal.db")
    cursor = conn.cursor()
    
    cursor.execute("""UPDATE Animales_Reptiles SET _jugado = ? WHERE _nombre = ?""", (valor_nuevo, nombre_animal)) 
    
    conn.commit()
    conn.close()
    
def actualizar_anfibio(nombre_animal,valor_nuevo):
    conn = sqlite3.connect("Adivina_Animal.db")
    cursor = conn.cursor()
    
    cursor.execute("""UPDATE Animales_Anfibios SET _jugado = ? WHERE _nombre = ?""", (valor_nuevo, nombre_animal))
    
    conn.commit()
    conn.close()
    
def actualizar_pez(nombre_animal,valor_nuevo):
    conn = sqlite3.connect("Adivina_Animal.db")
    cursor = conn.cursor()
    
    cursor.execute("""UPDATE Animales_Peces SET _jugado = ? WHERE _nombre = ?""", (valor_nuevo, nombre_animal))
    
    conn.commit()
    conn.close()
    
def actualizar_ave(nombre_animal,valor_nuevo):
    conn = sqlite3.connect("Adivina_Animal.db")
    cursor = conn.cursor()
    
    cursor.execute("""UPDATE Animales_Aves SET _jugado = ? WHERE _nombre = ?""", (valor_nuevo, nombre_animal))
    
    conn.commit()
    conn.close()
    
def actualizar_insecto(nombre_animal,valor_nuevo):
    conn = sqlite3.connect("Adivina_Animal.db")
    cursor = conn.cursor()
    
    cursor.execute("""UPDATE Animales_Insectos SET _jugado = ? WHERE _nombre = ?""", (valor_nuevo, nombre_animal))
    
    conn.commit()
    conn.close()
    
def actualizar_aracnido(nombre_animal,valor_nuevo):
    conn = sqlite3.connect("Adivina_Animal.db")
    cursor = conn.cursor()
    
    cursor.execute("""UPDATE Animales_Aracnidos SET _jugado = ? WHERE _nombre = ?""", (valor_nuevo, nombre_animal))
    
    conn.commit()
    conn.close()