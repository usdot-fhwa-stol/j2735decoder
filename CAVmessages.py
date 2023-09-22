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
        j2735_dict = self.checkDict(j2735_dict, msgId)
        self.xml = self.dict2xml(j2735_dict,save)
        self.json = self.xml2json(self.xml,save)

    def fixJ2735dict(self,j2735_dict,messageId):
        for key in j2735_dict:
            # print(key, type(j2735_dict[key]))
            if type(j2735_dict[key]) is tuple:
                error_tuple = j2735_dict[key]
                
                if type(error_tuple[0]) is int and type(error_tuple[1]) is int:  
                    if error_tuple[0] == 0 and error_tuple[1] == 0:
                        j2735_dict[key] = ""
                    else:
                        j2735_dict[key] = format(error_tuple[0],'0'+str(error_tuple[1])+'b')
                
                elif type(error_tuple[0]) is str and type(error_tuple[1]) is dict or list or tuple:
                    # print('here')
                    j2735_dict[key] = {}
                    j2735_dict[key][error_tuple[0]] = error_tuple[1]
                    # print('tulap',type(error_tuple[0]))
                
                else:
                    print(key, type(j2735_dict[key]))
                    print(type(error_tuple[0]),type(error_tuple[1]))
                
            elif type(j2735_dict[key]) is str and j2735_dict[key] != '':
                error_str = j2735_dict[key]
                j2735_dict[key] = {}
                j2735_dict[key][error_str] = ''
            elif type(j2735_dict[key]) is bytes:
                j2735_dict[key] = j2735_dict[key].hex().upper()
            
            elif type(j2735_dict[key]) is list:  #and key != "PathHistoryPoint": #Fixing List data type
                # print(key, type(j2735_dict[key]))
                # print(key)
                error_list = j2735_dict[key]
                # print(error_list)
                
                # STOL BSM part-II data
                if key == 'partII':
                    j2735_dict[key] = {}
                    j2735_dict[key]['PartIIcontent'] = error_list[0]       
                elif key == 'crumbData':
                    # print(error_list)
                    # print(len(error_list))
                    j2735_dict[key] = {}
                    for i in range(len(error_list)):
                        j2735_dict[key]['PathHistoryPoint_'+str(i)] = error_list[i]
                
                # MAP and SPaT Intersections data fix
                elif key == 'intersections':
                    j2735_dict[key] = {}
                    if messageId == 19: # For SPaT
                        j2735_dict[key]['IntersectionState'] = error_list[0] 
                    elif messageId == 18: # For MAP
                        j2735_dict[key]['IntersectionGeometry'] = error_list[0]
                
                # SPaT list data fix
                elif key == 'states': 
                    # print(error_list)
                    # print(len(error_list))
                    j2735_dict[key] = {}
                    for i in range(len(error_list)):
                        j2735_dict[key]['MovementState_'+str(i)] = error_list[i]
                elif key == 'state-time-speed':
                    j2735_dict[key] = {}
                    j2735_dict[key]['MovementEvent'] = error_list[0]    
                
                # MAP list data fix     
                elif key == 'laneSet': 
                    # print(error_list)
                    # print(len(error_list))
                    j2735_dict[key] = {}
                    for i in range(len(error_list)):
                        j2735_dict[key]['GenericLane_'+str(i)] = error_list[i]
                elif key == 'nodes':
                    j2735_dict[key] = {}
                    for i in range(len(error_list)):
                        j2735_dict[key]['NodeXY_'+str(i)] = error_list[i]
                elif key == 'connectsTo':
                    j2735_dict[key] = {}
                    for i in range(len(error_list)):
                        j2735_dict[key]['Connection_'+str(i)] = error_list[i]
        return j2735_dict

    def checkDict(self,python_dict,messageId):
        # print('INPUT',json,'\n')
        python_dict = self.fixJ2735dict(python_dict,messageId)
        # print('\n','OUTPUT',json,'\n')
        for key in python_dict:
            if type(python_dict[key]) is dict:
                python_dict[key] = self.checkDict(python_dict[key],messageId)
        return python_dict

    def dict2xml(self,j2735_dict, save=False):
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
