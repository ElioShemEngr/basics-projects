class Character():
    """
    Clase base para los personajes del juego.
    Define atributos y métodos generales que son compartidos por todas las clases derivadas.
    """
    def __init__(self, name, gender, hp, ep, level=1):
        self.name = name # Nombre del personaje
        self.gender = gender # Genero (M/F)
        self.hp = hp  # Puntos de vida
        self.ep = ep  # Puntos de energía
        self.level = level  # Nivel inicial

    def attack(self):
        # Método básico de ataque que calcula el daño según el nivel del personaje.
        return self.level * 10
    
    def take_damage(self, damage):
        # Reduce los puntos de vida del personaje al recibir daño.
        self.hp -= damage
        self.hp = max(self.hp, 0)  # Evitar que los puntos de vida sean negativos.

    def heal_self(self, amount):
        # Cura al personaje, aumentando los puntos de vida.
        self.hp += amount

    def consume_energy(self, amount):
        # Reduce los puntos de energía al usar habilidades especiales.
        # amount: Cantidad de energía consumida.
        #return: True si la energía fue suficiente, False en caso contrario.

        if self.ep >= amount:
            self.ep -= amount
            return True
        return False

    def is_alive(self):
        # Verifica si el personaje está vivo (HP > 0).
        #return: True si el personaje está vivo, False en caso contrario.
        return self.hp > 0

    def show_stats(self):
        # Devuelve las estadísticas del personaje en formato de diccionario.
        #return: Diccionario con las estadísticas actuales del personaje.

        return {
            "Nombre": self.name,
            "Género": self.gender,
            "HP": self.hp,
            "EP": self.ep,
            "Nivel": self.level
        }

# --------------------------------------------------------------------

# Subclases derivadas de Character
class Guerrero(Character):
    def __init__(self, name, gender, level=1):
        super().__init__(name, gender, hp=150, ep=50, level=level)

    def heavy_strike(self):
        """Golpe fuerte que consume energía."""
        if self.consume_energy(10):
            return self.level * 20  # Daño aumentado
        return 0  # Sin suficiente energía


class Mago(Character):
    def __init__(self, name, gender, level=1):
        super().__init__(name, gender, hp=100, ep=100, level=level)

    def fireball(self):
        """Lanza una bola de fuego que consume energía."""
        if self.consume_energy(15):
            return self.level * 25  # Daño mágico potente
        return 0  # Sin suficiente energía


class Picaro(Character):
    def __init__(self, name, gender, level=1):
        super().__init__(name, gender, hp=120, ep=70, level=level)

    def backstab(self):
        """Ataque furtivo que consume energía."""
        if self.consume_energy(20):
            return self.level * 30  # Daño crítico
        return 0  # Sin suficiente energía


class Sanador(Character):
    def __init__(self, name, gender, level=1):
        super().__init__(name, gender, hp=110, ep=80, level=level)

    def heal(self, target):
        """Cura a un objetivo."""
        if self.consume_energy(10):
            healing = self.level * 15
            target.heal_self(healing)
            return healing
        return 0  # Sin suficiente energía

# ----------------------------------------------------------
# Función para la creación de personajes
def crear_personaje():
    print("¡Bienvenido a la creación de personajes!")
    print("Elige una clase:")
    print("1. Guerrero")
    print("2. Mago")
    print("3. Pícaro")
    print("4. Sanador")

    # Solicitar entrada del usuario
    opcion = int(input("Ingresa el número de tu elección: "))

    # Verificar que la opción sea válida
    if opcion not in [1, 2, 3, 4]:
        print("Opción inválida. Por favor, elige entre 1 y 4.")
        return None

    # Solicitar nombre y género
    nombre = input("Ingresa el nombre de tu personaje: ")
    genero = input("Ingresa el género de tu personaje (Masculino/Femenino): ")

    # Crear personaje según la elección
    if opcion == 1:
        personaje = Guerrero(name=nombre, gender=genero)
    elif opcion == 2:
        personaje = Mago(name=nombre, gender=genero)
    elif opcion == 3:
        personaje = Picaro(name=nombre, gender=genero)
    elif opcion == 4:
        personaje = Sanador(name=nombre, gender=genero)

    print("\n¡Personaje creado con éxito!")
    print("Estadísticas iniciales:")
    print(personaje.show_stats())

    return personaje

# Probar la creación de personajes
if __name__ == "__main__":
    nuevo_personaje = crear_personaje()
