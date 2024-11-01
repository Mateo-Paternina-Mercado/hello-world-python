import random

# Preguntas y opciones de respuesta
questions = [
    {
        "question": "¿Cuál de estas cualidades valoras más?",
        "options": [
            ("A) Valentía", "Gryffindor"),
            ("B) Inteligencia", "Ravenclaw"),
            ("C) Lealtad", "Hufflepuff"),
            ("D) Ambición", "Slytherin")
        ]
    },
    {
        "question": "¿Cómo reaccionarías si alguien te desafía?",
        "options": [
            ("A) Aceptaría el reto sin dudarlo", "Gryffindor"),
            ("B) Planearía una estrategia", "Ravenclaw"),
            ("C) Intentaría mediar para evitar conflictos", "Hufflepuff"),
            ("D) Buscaría la forma de ganar a toda costa", "Slytherin")
        ]
    },
    {
        "question": "¿Qué tipo de actividad te gustaría hacer en tu tiempo libre?",
        "options": [
            ("A) Hacer algo extremo como escalar", "Gryffindor"),
            ("B) Leer un libro interesante", "Ravenclaw"),
            ("C) Pasar tiempo con amigos", "Hufflepuff"),
            ("D) Trabajar en un proyecto personal", "Slytherin")
        ]
    },
    {
        "question": "Si encuentras un billete en la calle, ¿qué harías?",
        "options": [
            ("A) Lo devolvería a su dueño", "Hufflepuff"),
            ("B) Lo usaría para una aventura", "Gryffindor"),
            ("C) Lo ahorraría para algo importante", "Ravenclaw"),
            ("D) Lo gastaría en algo que me beneficie", "Slytherin")
        ]
    },
    {
        "question": "¿Cuál de estas frases te identifica más?",
        "options": [
            ("A) 'La valentía es la clave para el éxito'", "Gryffindor"),
            ("B) 'El conocimiento es poder'", "Ravenclaw"),
            ("C) 'La amistad es lo más importante'", "Hufflepuff"),
            ("D) 'El fin justifica los medios'", "Slytherin")
        ]
    }
]

# Inicialización de puntuaciones
scores = {
    "Gryffindor": 0,
    "Ravenclaw": 0,
    "Hufflepuff": 0,
    "Slytherin": 0
}

# Función para hacer preguntas
def ask_questions():
    for question in questions:
        print(question["question"])
        for option in question["options"]:
            print(option[0])  # Imprimir las opciones
        
        # Inicializar respuesta como incorrecta
        answer = ""
        while answer not in ["A", "B", "C", "D"]:
            answer = input("Elige una opción (A, B, C, D): ").strip().upper()
            if answer not in ["A", "B", "C", "D"]:
                print("Respuesta inválida. Por favor, elige A, B, C o D.")
        
        # Procesar respuesta
        for option in question["options"]:
            if answer == option[0][0]:
                house = option[1]
                scores[house] += 1

# Función para determinar la casa
def determine_house():
    max_score = max(scores.values())
    houses_with_max_score = [house for house, score in scores.items() if score == max_score]
    
    # En caso de empate, elegir una casa al azar
    assigned_house = random.choice(houses_with_max_score)
    
    return assigned_house

# Ejecución del programa
def main():
    print("¡Bienvenido al cuestionario de Hogwarts!")
    ask_questions()
    assigned_house = determine_house()
    print(f"\nHas sido asignado a la casa: {assigned_house}!")

if __name__ == "__main__":
    main()