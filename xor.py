#!/bin/python

if __name__ == "__main__":

        string = "label"
        number = 13
        flag = ""
        for e in string :
                tmp = ord(e) ^ number
                flag = flag + chr(tmp)
        print(flag)

        
