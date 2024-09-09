# XML is a markup language designed for storing and transporting data with a focus on hierarchical structures.
# xml.etree.ElementTree, lxml, xml.dom.minidom - Several libraries for working with XML
# XML files are used for hierarchical data structures, often requiring parsing and string manipulations.
# Writing to an XML file
import xml.etree.ElementTree as ET

root = ET.Element('root')
child1 = ET.SubElement(root, 'child1')
child1.text = 'This is child 1'

child2 = ET.SubElement(root, 'child2', attrib={'name': 'second'})
child2.text = 'This is child 2'
# Save to file
tree = ET.ElementTree(root)
tree.write('output.xml')
# Reading an XML file
tree = ET.parse('data.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib, child.text)

# Stripping Text Content from XML Elements
xml_data = '''
<root>
    <name> Alice </name>
    <age> 30 </age>
    <city> New York </city>
</root>
'''

root = ET.fromstring(xml_data)

# Stripping text from each element
for child in root:
    print(child.tag, child.text.strip())
# Output is
# name Alice
# age 30
# city New York

# strip() removes extra whitespace around the text content of each element.

xml_data = '''
<root>
    <item>One</item>
    <item>Two</item>
    <item>Three</item>
    <item>Four</item>
</root>
'''

root = ET.fromstring(xml_data)

# Slicing the first three items
items = list(root)[:3]    # converts the root's children to a list and slices the first three items.
for item in items:
    print(item.text)

# Using next() to Iterate Over XML Elements

xml_data = '''
<root>
    <item>One</item>
    <item>Two</item>
    <item>Three</item>
</root>
'''

root = ET.fromstring(xml_data)
iterator = iter(root)

# Using next() to get the first item
first_item = next(iterator)
print(first_item.text)    # Output is One




