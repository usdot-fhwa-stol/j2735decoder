#! /usr/bin/env python3
import ieee1609Dot3_wsa
from binascii import unhexlify
from json2xml import json2xml
from json2xml.utils import readfromstring

# Monkey-patch imports to control JSON encoding behavior used by to_jer()
import pycrate_asn1rt.asnobj
import pycrate_core.elt as _core_elt
import pycrate_asn1rt.codecs as _asn_codecs

FRAME = ieee1609Dot3_wsa.Ieee1609Dot3Wsa.SrvAdvMsg

class WSA_decode:
    def __init__(self, frame):
        # Ensure JER JSON preserves insertion order (disable alphabetical sorting)
        # i.e., pycrate defaults to JSONEncoder(sort_keys=True). Override it here.
        try:
            # Recreate the encoder with sort_keys disabled
            _core_elt.JsonEnc = _core_elt.JSONEncoder(sort_keys=False, indent=1)
            # Propagate to modules that cached the encoder
            _asn_codecs.JsonEnc = _core_elt.JsonEnc
            pycrate_asn1rt.asnobj.JsonEnc = _core_elt.JsonEnc
        except Exception:
            pass

        self.frame = frame

    def decode(self, xml: bool = False) -> str:
        """
        Decode the WSA frame.
        """
        decode = FRAME
        decode.from_uper(unhexlify(self.frame))
        jer = decode.to_jer()
        if xml:
            return self.dict2xml(jer)
        return jer
    
    def dict2xml(self, jer: str, save=False) -> str:
        '''
        Convert J2735 JER to XML.

        Parameters
        ----------
        jer (str): The J2735 JER string to convert.
        save (bool): Whether to save the XML to a file.

        Returns
        -------
        str: The converted XML string.
        '''
        jer_dict = readfromstring(jer)
        xml_str = json2xml.Json2xml(jer_dict, attr_type=False, wrapper="SrvAdvMsg").to_xml()

        if save:
            with open("j2735decode.xml","w") as f:
                f.write(str(xml_str))
        return str(xml_str)
