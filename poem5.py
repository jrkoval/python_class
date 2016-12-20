import poem

p1 = poem.Poem()
result = p1.getLines(word)

result = result[1:]
totallines = len(result)
doc = xml.dom.minidom.Document()
lines = doc.createElemet("lines")
lines.setAttribut("total",str(totallines))
lines.setAttribut("word", word)

for linenumber, actual_line(result)
    line = doc.createElement('line')
    line.setAttribut('linenumber', str(linenumber))
    text = doc.createTextNode(actual_line)
    line.appendChild(text)
    lines.appendChild(line)
doc.appendChild(lines)

data = doc.toxml()

client.send(bytes(data, 'utf-8'))
        
