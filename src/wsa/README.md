# Install

You can install dependencies and the SAE J2735 ASN.1 Python package bundled in this repo as a wheel.

- Create and activate a virtual environment (recommended)
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```

- Install the IEEE 1609.3 package from the local wheel
   ```sh
   pip install wheels/ieee*.whl
   ```

# Usage

## 1. **Importing the Function**:
   To get started, first import the `WSA_decode` function from the `wsa_decode.py` module.
   ```python
   from wsa_decode import WSA_decode
   ```

## 2. **Understanding the Function**:
   The function is designed to decode IEEE 1609.3 WSA UPER hex payloads into XML or JSON.

   - **Primary Objective**: Convert WSA UPER hex into XML or JSON format.
   - **Inputs**:
     - `frame`: Represents the UPER hex payload intended for decoding.
   - **Outputs**: The function provides a decoded WSA message as either an XML or JSON.

## 3. **Utilizing the Function**:

   Basic usage:
   ```python
   frame = WSA_decode(wsa_input)
   ```

## 4. **Extracting the Outputs**:
   
   - To retrieve the XML format:
     ```python
     decoded_data = frame.decode(xml=True)
     print(decoded_data)
     ```
   - To retrieve the JSON format:
     ```python
     decoded_data = frame.decode(xml=False)
     print(decoded_data)
     ```

## 5. **Test Your Setup**:

   For an initial test, execute the `main_test.py` script. You can modify the payload values in this script as needed, and then inspect the XML and JSON outputs directly in the terminal.