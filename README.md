<h1 align="center"> V2X Communication Message Decoder </h1>

Python library to decode SAE J2735 encoded UPER hex (Currently supporting BSM, MAP, SPaT).

## Dependencies

* Python3

### Python Libraries
* Pycrate
```sh
pip install pycrate 
```
* binascii
* xml.etree.ElementTree
* xmltodict
```sh
pip install xmltodict 
```
* json
* json2xml
```sh
pip install json2xml 
```


## Usage 
Import J2735_decode function from CAVmessage.py library into your python. 

j2735_decode function
    
* Function to decode J2735 UPER hex to XML or JSON.
* Supported messages - BSM, MAP, SPaT.
* Input - 
    1. Payload - UPER hex payload.
    2. FileSave [Default = False] - If "True" the function will save both XML and JSON decoded files into running directory. (Filenames - j2735decode.xml and j2735decode.json)
* Output - XML and JSON decoded J2735 message.

### Example

decode = J2735_decode(payload)

Generated output class file contains both XML and JSON formated output.

To get XML file use "decode.xml" and to get JSON file use "decode.json".

### Test

To get started try running "main_test.py" with different payload values that print out both XML and JSON files to terminal to test out installation.  

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## Contact
CAV support services - [CAVSupportServices@dot.gov](CAVSupportServices@dot.gov)


