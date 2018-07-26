#!/usr/bin/env python
#FILE:          main.py
#SOURCE:        viper/system/core/
__author__      = "Danny Dowshenko"
__copyright__   = "http://creativecommons.org/licenses/by/3.0/legalcode"
#DESCRIPTION: 
"""
MAIN MENU that threads
    -each 'core' element is a thread
    -main listens to 'core'
"""

def CENTRAL():
    print("CENTRAL: OK")


# For making modules"
if __name__ == '__main__':
    CENTRAL()
    # print('main.py is being run directly')
else:
    # print("main.py is being imported")
    pass

