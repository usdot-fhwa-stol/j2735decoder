
<h1 align="center"> V2X Communication Message Decoder </h1>

A Python library crafted to decode SAE J2735 encoded UPER HEX messages.

### Built With

- [pycrate](https://github.com/pycrate-org/pycrate)
- [J2735: Dedicated Short Range Communications Message Set](https://www.sae.org/standards/content/j2735_202409/)

## Getting Started

> **Note**: The library has been tested on Ubuntu 22.04 and Windows 10.

### Prerequisites

- **Python 3**

### Install

You can install dependencies and the SAE J2735 ASN.1 Python package bundled in this repo as a wheel.

- Create and activate a virtual environment (recommended)
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

- Install required packages
   ```bash
   pip install -r requirements.txt
   ```

- Install the J2735 definitions package from the local wheel. You may install either or both wheels available. Example:
   ```bash
   pip install wheels/j2735_202409-*.whl
   ```

#### Required Python Libraries

- **Pycrate**
```sh
pip install pycrate==0.7.11
```

- **json2xml**
```sh
pip install json2xml==5.2.1
```
[The following libraries are essential and should already be part of a standard Python3 installation:]
- **json**
- **binascii**

## Usage: `J2735_decode` Function

### 1. **Importing the Function**:
   To get started, first import the `J2735_decode` function from the `CAVmessage.py` module.
   ```python
   from CAVmessage import J2735_decode
   ```

   **Note:** You may also set the desired J2735 V2X version in CAVmessage.py. Simply change the import name at the top of this file. It is currently defaulted to j2735_202409. You may change this to j2735_201603_combined.

### 2. **Understanding the Function**:
   The function is designed to decode J2735 UPER hex payloads into XML or JSON.

   - **Primary Objective**: Convert J2735 UPER hex into XML or JSON format.
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
