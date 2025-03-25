# Decoder for J2735 BSM messages (hex to xml or json)

import J2735_201603_combined_mobility
from binascii import unhexlify
import json
import xml.etree.ElementTree as ET
from json2xml import json2xml
import xmltodict

class J2735_decode:
    '''
    Class to decode J2735 UPER hex to XML or JSON.
    Supported messages - BSM, MAP, SPaT
    Input - UPER hex payload
    Output - XML and JSON decoded J2735 message 
    '''
    def __init__(self, payload,save=False):
        decode = J2735_201603_combined_mobility.DSRC.MessageFrame
        decode.from_uper(unhexlify(payload))
        # print(type(decode()['value'][0]))
        msgId = decode()['messageId']
        j2735_dict = {}
        j2735_dict["MessageFrame"] = decode()
        # print(j2735_dict)

        cleanObj = convertBytes(decode())
        jsonString = json.dumps(cleanObj, indent=2)
        print(jsonString)


        j2735_dict = self.checkDict(j2735_dict, msgId)
        self.xml = self.dict2xml(j2735_dict,save)
        self.json = self.xml2json(self.xml,save)

    def convertBytes(self, obj):
        if isinstance(obj, dict):
            return {k: self.convertBytes(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [self.convertBytes(item) for item in obj]
        elif isinstance(obj, tuple):
            return [self.convertBytes(item) for item in obj]
        elif isinstance(obj, bytes):
            return obj.hex()
        else:
            return obj

    def dict2xml(self, j2735_dict, save=False):
        xml_str = json2xml.Json2xml(j2735_dict,item_wrap=True,attr_type=False).to_xml()
        # print(xml_str)
        xml_root = ET.fromstring(xml_str) # convert xml string to python xml root tree
        xml_root = xml_root[0] # remove additional root created by json2xml

        for elem in xml_root.iter():
            if elem.tag.find('_') >= 0:
                elem.tag = elem.tag[:elem.tag.find('_')]            

        xml_string = ET.tostring(xml_root, encoding='unicode')
        xml_bytes = ET.tostring(xml_root)
        if save:
            with open("j2735decode.xml","wb") as f:
                f.write(xml_bytes)
        return xml_string
    
    def xml2json(self, j2735_xml, save=False):
        dict = xmltodict.parse(j2735_xml)
        j2735_json = json.dumps(dict, indent=4).replace("null",'""')
        if save:
            with open("j2735decode.json", "w") as f:
                f.write(j2735_json)
        return j2735_json
