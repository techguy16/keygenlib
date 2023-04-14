from . win95 import KeyGenerator
from . elevendigit import elevendigitkey_a

def win95_retail():
    key = KeyGenerator.retailkey()
    return key
    
def win95_oem():
    key = KeyGenerator.oemkey()
    return key

def elevendigit_retail():
    key = elevendigitkey_a()
    return key
