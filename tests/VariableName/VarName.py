# -*- coding: utf-8 -*-

# Python __name__ module Test
# Author - HoneyMoose(huyuchengus@gmail.com)
# Link Article - https://www.ossez.com/t/python-name/13393

import ImportVarName

print("Main VarName __name__ = %s" % __name__)

if __name__ == "__main__":
    print("VarName is being run directly")
else:
    print("VarName is being imported")
