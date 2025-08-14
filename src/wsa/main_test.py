#! /usr/bin/env python3
from wsa_decode import WSA_decode

def main():
    wsa_input = input("Enter your WSA Hex Message:\n")
    frame = WSA_decode(wsa_input)
    decoded_data = frame.decode(xml=False)
    print(decoded_data)

if __name__ == "__main__":
    main()
