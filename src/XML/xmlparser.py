from xml.etree import ElementTree


def test_parsing_xml():
    xml_string = '''
    <Result>
    <name>rahul</name>
    <empno>34569990</empno>
    <marks>78.5</marks>
    <address>
    <housenumber>123</housenumber>
    <roadnumber>5</roadnumber>
    <city>Mysuru</city>
    </address>
    </Result>
    '''

    root = ElementTree.fromstring(xml_string)
    print()

    for child in root:
        print(child.tag)  # print tag names of name, empno, and marks

    y = root.find(".//name")
    print(y.text)  # prints rahul

    first = root.find(".//address/*[1]")
    print(first.text, first.tag)

    parenttag = root.find(".//*[housenumber]")
    print(parenttag.tag)

    c = root.find(".//city[1]")
    print(c.text)

    c = root.findall(".//city[1]")
    print("no of city tag that are occuring firat in their parents: " + str(len(c)))






