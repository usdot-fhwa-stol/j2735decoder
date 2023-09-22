
<h1 align="center"> V2X Communication Message Decoder </h1>

A Python library crafted to decode SAE J2735 encoded UPER hex messages. At present, it supports BSM, MAP, and SPaT message types.

### Built With

- [pycrate](https://github.com/P1sec/pycrate)
- [J2735: Dedicated Short Range Communications Message Set](https://www.sae.org/standards/content/j2735_201603/)

## Getting Started

> **Note**: The library has been tested on Ubuntu20.

### Prerequisites

- **Python 3**

#### Required Python Libraries

- **Pycrate**
```sh
pip install pycrate 
```
- **binascii**
- **xml.etree.ElementTree**
- **xmltodict**
```sh
pip install xmltodict 
```
- **json**
- **json2xml**
```sh
pip install json2xml 
```

## Usage: `J2735_decode` Function

### 1. **Importing the Function**:
   To get started, first import the `J2735_decode` function from the `CAVmessage.py` module.
   ```python
   from CAVmessage import J2735_decode
   ```

### 2. **Understanding the Function**:
   The function is designed to decode J2735 UPER hex payloads into XML or JSON.

   - **Primary Objective**: Convert J2735 UPER hex into XML or JSON format.
   - **Supported Messages**: BSM, MAP, SPaT.
   - **Inputs**:
     - `Payload`: Represents the UPER hex payload intended for decoding.
     - `FileSave` (default value is `False`): When set to `True`, the decoded XML and JSON outputs are saved in the directory from which the script is executed.
   - **Outputs**: The function provides a decoded J2735 message in both XML and JSON formats.

### 3. **Utilizing the Function**:

   Basic usage:
   ```python
   decode = J2735_decode(payload)
   ```

   To save outputs as files:
   ```python
   decode = J2735_decode(payload, True)
   ```

### 4. **Extracting the Outputs**:
   
   - To retrieve the XML format:
     ```python
     print(decode.xml)
     ```
   - To retrieve the JSON format:
     ```python
     print(decode.json)
     ```

### 5. **Test Your Setup**:

   For an initial test, execute the `main_test.py` script. You can modify the payload values in this script as needed, and then inspect the XML and JSON outputs directly in the terminal.

## Sample Data Insights

Within the `Sample Data` directory, you'll find "SampleHexPayloads.txt". This file contains several J2735 encoded UPER hex payloads. Corresponding decoded XML and JSON messages for these payloads are also available in the same directory.

## Contributing to the Project

Your contributions enrich the open-source community, making it a vibrant place for learning, inspiration, and creativity. Every contribution, however small, is invaluable.

1. Fork the Project.
2. Spawn your Feature Branch (`git checkout -b feature/YourFeatureName`).
3. Commit the changes (`git commit -m 'Introduce YourFeatureName'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Initiate a Pull Request.

## Get in Touch

For any queries or support, reach out to: [CAVSupportServices@dot.gov](mailto:CAVSupportServices@dot.gov).


