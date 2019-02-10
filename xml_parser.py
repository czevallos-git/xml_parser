import os
import time
import xml.etree.ElementTree as ET

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))


def main():
    print('-----start-----')
    root = ET.parse(os.path.join(ROOT_DIR, 'data.xml')).getroot()
    # for child in root.findall('.//neighbor[@direction="E"][city="San Jose"]'):
    #     print(child.get('name'))

    time.sleep(15)


    for child in root.findall(".//neighbor[1]"):
        print(child.get('name'))
    # print([e.get('name') for e in tree.findall('country/neighbor')])

    # print(tree)
    # node = tree.find('country')
    # print('attrib: ', node.attrib)
    # print('get(): ', node.get('currency'))
    # print('items(): ', node.items())
    # print('keys(): ', node.keys())
    # print('find(): ', node.find('neighbor').get('name'))
    # for e in node.findall('neighbor'):
    #     print(e.get('name'))
    # print('findtext(): ', node.findtext('neighbor'))
    # print([e.tag for e in list(node)])
    # # node.insert(1, ET.fromstring('<add>plus</add>'))
    # print([e.tag for e in list(node)])
    # print('iter(): ', [i.tag for i in node.iter()])
    # print([i.get('name') for i in node.iterfind('neighbor')])
    # print(node.iterfind('neighbor'))
    # print([i.get('name') for i in node.findall('neighbor')])
    # print(node.findall('neighbor'))
    # ET.dump(node)
    # print(node.find('neighbor/neighbor').get('name'))


if __name__ == '__main__':
    main()

