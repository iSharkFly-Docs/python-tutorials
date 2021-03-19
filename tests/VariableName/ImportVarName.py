# -*- coding: utf-8 -*-

# Python __name__ module ImportVarName
# Author - HoneyMoose(huyuchengus@gmail.com)
# Link Article - https://www.ossez.com/t/python-name/13393


print("ImportVarName __name__ = %s" % __name__)

if __name__ == "__main__":
    print("ImportVarName is being run directly")
else:
    print("ImportVarName is being imported")
