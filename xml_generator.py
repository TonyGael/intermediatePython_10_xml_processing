import xml.etree.ElementTree as ET
import random

# Crear el elemento raíz 'group'
group = ET.Element("group")

# Crear 20 nodos 'persons'
for i in range(20):
    # Generar valores aleatorios para cada etiqueta
    name = "Person" + str(i)
    age = str(random.randint(20, 60))
    weight = str(random.uniform(50, 100))
    height = str(random.uniform(150, 200))

    # Crear el nodo 'person'
    person = ET.SubElement(group, "person")

    # Agregar las etiquetas 'name', 'age', 'weight' y 'height' con sus respectivos valores
    ET.SubElement(person, "name").text = name
    ET.SubElement(person, "age").text = age
    ET.SubElement(person, "weight").text = weight
    ET.SubElement(person, "height").text = height

# Crear 18 nodos adicionales 'persons'
for i in range(20, 38):
    # Generar valores aleatorios para cada etiqueta
    name = "Person" + str(i)
    age = str(random.randint(20, 60))
    weight = str(random.uniform(50, 100))
    height = str(random.uniform(150, 200))

    # Crear el nodo 'person'
    person = ET.SubElement(group, "person")

    # Agregar las etiquetas 'name', 'age', 'weight' y 'height' con sus respectivos valores
    ET.SubElement(person, "name").text = name
    ET.SubElement(person, "age").text = age
    ET.SubElement(person, "weight").text = weight
    ET.SubElement(person, "height").text = height

# Crear el árbol XML
tree = ET.ElementTree(group)

# Escribir el árbol XML en el archivo 'data.xml'
tree.write("data.xml")