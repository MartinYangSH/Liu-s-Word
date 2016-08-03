def validXML(xmlString,position,openXml):
    if xmlString == None:
        return True
    elif position  == len(xmlString) and openXml==[]:
        return True
    elif position < len(xmlString):
        if xmlString[position] == '<':
            if xmlString[position+1]!='/':
                openTag = ''
                for i in xmlString[position:]:
                    if i !='>':
                        openTag += i
                    else:
                        break
                position += len(openTag)+1
                openXml.append(openTag.strip('<'))
                return validXML(xmlString, position, openXml)
            elif xmlString[position+1] == '/':
                closeTag = ''
                for i in xmlString[position:]:
                    if i !='>':
                        closeTag += i
                    else:
                        break
                position += len(closeTag)+1
                if closeTag.strip('</')==openXml[len(openXml)-1]:
                    openXml.pop()
                    return validXML(xmlString, position,openXml)
                else:
                    return False
        else:
            return validXML(xmlString, position+1, openXml)
    else:
        return False
                
xmlString = '''<ava>
                <asd>
                    <asdas>asdf</asdas>
                    <as>asdf</as>
                </asd>
               </ava>'''
if validXML(xmlString,0,[]):
    print 'Valid'
else:
    print 'Invalid'