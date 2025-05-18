import random

cuartadas_samuel = {
    "Baño": "Estaba reparando una fuga en el baño, dejó sus herramientas ahí como prueba.",
    "Biblioteca": "Pasó horas revisando planos antiguos, incluso dejó anotaciones en uno de los libros.",
    "Cocina": "Solo fue a instalar un detector de humo. No permaneció más de 5 minutos.",
    "Habitación": "Estaba verificando una falla eléctrica en la lámpara. Tiene los guantes manchados de hollín.",
    "Sótano": "Estuvo revisando los conductos del sistema de calefacción. El polvo de carbón aún está en sus botas."
}

cuartadas_catty = {
    "Baño": "Lo dejó impecable esa mañana. Dice que nadie más entró hasta después del crimen.",
    "Biblioteca": "Estuvo limpiando estantes y organizando libros, tiene alergia al polvo y estuvo estornudando todo el rato.",
    "Cocina": "Lavó todos los platos del desayuno, y luego salió a ventilar la habitación.",
    "Habitación": "Estaba haciendo la cama y encontró un pendiente que entregó al dueño.",
    "Sótano": "Le da miedo bajar ahí, asegura que no ha puesto una pata desde hace días."
}

cuartadas_foxy = {
    "Baño": "Estaba probando un sistema automático de ducha que acabó inundando el lugar.",
    "Biblioteca": "Instaló un microlector de huellas en un libro raro. Dice que puedes verificarlo tú mismo.",
    "Cocina": "Estaba diseñando un robot chef, pero solo logró que quemara la sopa.",
    "Habitación": "Probó un colchón con sensor de sueño, asegura que nunca se activó esa noche.",
    "Sótano": "Tenía una máquina experimental funcionando ahí. Hace tanto ruido que nadie más se atreve a bajar."
}

cuartadas_rene = {
    "Baño": "Hace inspecciones diarias de higiene militar. Dice que el baño estaba en orden.",
    "Biblioteca": "Leyó sobre estrategias de guerra antiguas, anotó citas exactas que puedes buscar.",
    "Cocina": "Supervisó la limpieza como si fuera una cocina de cuartel. Todo estaba en su sitio.",
    "Habitación": "Tomaba una siesta táctica de 15 minutos exactos. Tiene una alarma programada como prueba.",
    "Sótano": "Practicaba salto desde el último escalón. El cronómetro en su reloj lo respalda."
}

cuartadas_angela = {
    "Baño": "Se inspiró en los reflejos del espejo para un nuevo cuadro. Estuvo pintando ahí por media hora.",
    "Biblioteca": "Esbozó paisajes usando libros de arte. Dejó sus bocetos tirados entre los estantes.",
    "Cocina": "Solo entró a buscar pigmentos naturales en las especias. No cocinó nada.",
    "Habitación": "Pintaba un mural en la pared, aún puedes ver la pintura fresca.",
    "Sótano": "Dice que el eco del sótano inspira sus poemas, aunque jura que no bajó ese día."
}

cuartadas_personajes = {
    "Samuel": cuartadas_samuel,
    "Catty": cuartadas_catty,
    "Foxy": cuartadas_foxy,
    "Rene": cuartadas_rene,
    "Angela": cuartadas_angela
}

def obtener_cuartada(personaje, lugar):
    return cuartadas_personajes.get(personaje, {}).get(lugar, "No se encontró cuartada para este lugar.")

pistas_samuel = {
    "Baño": "Samuel dejó una llave inglesa manchada de grasa cerca del lavabo, como si hubiera tenido prisa al salir.",
    "Biblioteca": "Entre los libros técnicos, se halló una hoja con cálculos hechos a mano. La caligrafía parece de Samuel.",
    "Cocina": "Una toalla con marcas de quemaduras fue dejada cerca del horno. Samuel negó haberla usado.",
    "Habitación": "Detrás de la lámpara, hay un cable cortado con precisión. Solo alguien con conocimientos técnicos lo haría.",
    "Sótano": "Unas huellas de botas con carbón marcan el camino hasta un armario cerrado con candado forzado."
}

pistas_catty = {
    "Baño": "Una flor marchita en un jarrón indica que Catty estuvo allí decorando, aunque dice que no entró ese día.",
    "Biblioteca": "Un plumero olvidado en el segundo estante superior parece indicar limpieza reciente.",
    "Cocina": "Un delantal mojado con olor a detergente fue colgado torpemente. Catty asegura que lo dejó seco.",
    "Habitación": "Sobre la mesita de noche hay un pendiente brillante, igual al que Catty menciona haber encontrado.",
    "Sótano": "Una marca de garras en la puerta del sótano sugiere que alguien lo evitó a toda costa... como Catty mencionó."
}

pistas_foxy = {
    "Baño": "Un pequeño sensor de humedad estaba pegado a la pared, con un microcircuito aún activo.",
    "Biblioteca": "Uno de los libros tenía un microchip en la portada, como si hubiera sido usado para vigilancia.",
    "Cocina": "El robot cocinero está en modo error. Su registro muestra que alguien lo usó a medianoche.",
    "Habitación": "El colchón tiene sensores arrancados violentamente. Foxy asegura que no funcionaron nunca.",
    "Sótano": "Una válvula de escape tenía cinta aislante con iniciales 'FX' escritas a mano."
}

pistas_rene = {
    "Baño": "Todo está perfectamente alineado, excepto una toalla que parece haber sido arrojada con fuerza.",
    "Biblioteca": "Un libro de estrategias está marcado con una señal militar. Solo Rene parece usar ese código.",
    "Cocina": "Una lista de tareas tachadas en orden militar cuelga de la nevera. Falta la última línea.",
    "Habitación": "El cronómetro de su reloj marcaba una cuenta regresiva que terminó justo a la hora del crimen.",
    "Sótano": "Un saco de entrenamiento militar cuelga, con marcas de golpes recientes."
}

pistas_angela = {
    "Baño": "Sobre el espejo hay trazos de pintura que simulan lágrimas. Angela los llamó 'arte espontáneo'.",
    "Biblioteca": "Entre las páginas de un libro de arte, hay un boceto de una figura caída con un arma en la mano.",
    "Cocina": "Hay frascos con pigmentos mezclados con especias. Uno de ellos tiene restos de sangre seca.",
    "Habitación": "En la pared, bajo la pintura fresca, se nota un contorno oculto como si algo hubiese sido cubierto.",
    "Sótano": "Un poema críptico escrito en la pared habla de oscuridad, culpa y silencio profundo."
}

pistas_personajes = {
    "Samuel": pistas_samuel,
    "Catty": pistas_catty,
    "Foxy": pistas_foxy,
    "Rene": pistas_rene,
    "Angela": pistas_angela
}

def obtener_pista(personaje, lugar):
    return pistas_personajes.get(personaje, {}).get(lugar, "No se encontró pista para este lugar.")

def generar_historia(asesino, victima, lugar, arma):
    arma = "No encontrada."
    historias = [
        f"Una noche silenciosa en la {lugar[1]}, un grito rompió el mutismo. {victima[1]} fue hallado sin vida. "
        f"Las sospechas recaen sobre {asesino[1]}, el/la {asesino[2]}, que fue visto/a cerca del lugar.",

        f"Durante la cena, un extraño suceso ocurrió en la {lugar[1]}. El cuerpo de {victima[1]} fue encontrado. "
        f"Un/a {asesino[2]} como {asesino[1]} tenía acceso a la {lugar[1]}... ¿fue coincidencia?.",

        f"En lo profundo del {lugar[1]}, {victima[1]} encontró su fin."
        f"Todos los indicios apuntan a {asesino[1]}, cuyo comportamiento ha sido... sospechoso.",

        f"La habitación estaba cerrada desde dentro. Sin embargo, {victima[1]} fue encontrado/a sin vida. "
        f"¿Cómo pudo hacerlo {asesino[1]}, el/la {asesino[2]}? ¿O fue alguien más?",

        f"Entre el vapor del {lugar[1]}, alguien cometió un crimen. {victima[1]} no sobrevivió al ataque. "
        f"Los testigos afirman que {asesino[1]} estuvo allí minutos antes. ¿Será culpable o solo un testigo desafortunado?"
    ]
    return random.choice(historias)

def historia_final_buena(asesino, arma, lugar):
    finales_buenos = [
        f"¡Felicidades! Lograste resolver el caso. {asesino[1]}, el/la {asesino[2]}, fue arrestado gracias a tu astucia. "
        f"La {arma[1]} encontrada en la {lugar[1]} fue la prueba clave.",

        f"Con inteligencia y observación, diste con el culpable. {asesino[1]} no pudo esconder su crimen en la {lugar[1]}. "
        f"La {arma[1]} selló su destino. Justicia servida.",

        f"El misterio llegó a su fin. {asesino[1]}, que actuaba como si nada, fue desenmascarado como asesino. "
        f"La escena en la {lugar[1]} y la {arma[1]} fueron evidencia suficiente para encerrarlo.",

        f"Nadie creía que el/la {asesino[2]} pudiera ser culpable, pero tú lo descubriste. "
        f"Gracias a la pista dejada junto a la {arma[1]} en la {lugar[1]}, resolviste el crimen.",

        f"Has sido más astuto que el culpable. {asesino[1]} fue atrapado. La escena en la {lugar[1]} y la {arma[1]} revelaron la verdad. ¡Caso cerrado!"
    ]
    return random.choice(finales_buenos)

def historia_final_mala(asesino, arma, lugar):
    finales_malos = [
        f"Tu deducción fue errónea... mientras investigabas, {asesino[1]} escapó de la escena. "
        f"La {arma[1]} encontrada en la {lugar[1]} fue una pista que dejaste pasar.",

        f"Elegiste al sospechoso equivocado. Mientras tanto, {asesino[1]}, el verdadero asesino, se mezcla entre los demás. "
        f"La {arma[1]} aún sigue en la {lugar[1]}... esperando justicia.",

        f"Confiar en las apariencias fue tu error. El verdadero culpable, {asesino[1]}, ha logrado escapar. "
        f"La evidencia en la {lugar[1]} con la {arma[1]} no fue suficiente sin tu deducción acertada.",

        f"Fallaste. El crimen queda sin resolver. {asesino[1]}, el/la {asesino[2]}, se aleja lentamente, sin levantar sospechas. "
        f"La {arma[1]} aún guarda silencio en la {lugar[1]}.",

        f"Has sido engañado. El verdadero asesino, {asesino[1]}, sigue libre. La escena del crimen en la {lugar[1]} con la {arma[1]} permanece intacta..."
    ]
    return random.choice(finales_malos)
