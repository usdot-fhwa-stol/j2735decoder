#!/usr/bin/env python3
from CAVmessages import J2735_decode

def main():
    while True:
        payload = input("Enter your J2735 Hex Message:\n")
        decode = J2735_decode(payload, True)
        print(decode.xml)
        print(decode.json)

if __name__=="__main__":
    main()
