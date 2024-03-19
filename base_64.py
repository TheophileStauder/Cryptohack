#!/bin/python
import base64


if __name__ == "__main__" :

        input = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
        input_byte = bytes.fromhex(input)
        flag = base64.b64encode(input_byte)
        print(flag.decode())

        
