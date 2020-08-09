import sbol2

doc = sbol2.Document()
doc.read('dummy.xml')

print(len(doc))
print(doc)

for obj in doc:
    print(obj)

print('\n\n')

for cd in doc.componentDefinitions:
    print(cd)