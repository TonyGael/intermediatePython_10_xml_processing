import xml.dom.minidom

domtree = xml.dom.minidom.parse('data.xml')
group = domtree.documentElement

persons = group.getElementsByTagName('person')

for person in persons:
    print('_____Person_____')
    if person.hasAttribute('id'):
        print('ID: {}'.format(person.getAttribute('id')))

    print("Name: {}".format(person.getElementsByTagName('name')[0].childNodes[0].data))
    print("Age: {}".format(person.getElementsByTagName('age')[0].childNodes[0].data))
    print("Weight: {}".format(person.getElementsByTagName('weight')[0].childNodes[0].data))
    print("Height: {}".format(person.getElementsByTagName('height')[0].childNodes[0].data))

# persons[1].getElementsByTagName('name')[0].childNodes[0].nodeValue = "Tony Gael"
# persons[0].setAttribute('id', '33')
# persons[3].getElementsByTagName('weight')[0].childNodes[0].nodeValue = '115'
# domtree.writexml(open('data.xml', 'w'))

newperson = domtree.createElement('person')
newperson.setAttribute('id', '111')

name = domtree.createElement('name')
name.appendChild(domtree.createTextNode('Akira Toriyama'))

age = domtree.createElement('age')
age.appendChild(domtree.createElement('67'))

weight = domtree.createElement('weight')
weight.appendChild(domtree.createElement('81'))

height = domtree.createElement('height')
height.appendChild(domtree.createTextNode('167'))

newperson.appendChild(name)
newperson.appendChild(age)
newperson.appendChild(weight)
newperson.appendChild(height)

group.appendChild(newperson)
domtree.writexml(open('data.xml', 'w'))
