# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 12:14:22 2018

@author: PHẠM ĐẶNG MẠNH HỒNG LUÂN
"""

from osgeo import gdal,ogr

def readvect():
    inshpdir = input('INPUT VECTOR FILE: ')
    driver = ogr.GetDriverByName('ESRI Shapefile')
    dataset = driver.Open(inshpdir)
    layer = dataset.GetLayer()
    return layer
def readgeoref():
    
    return




#MAIN MENU FUNCTION
def main_menu():
    os.system('clear')
    print('WELCOME TO lANDUSE CLASSIFICATION PROGRAM! \n')
    print('PLEASE CHOOSE OPERATION YOU WANT: \n')
    print('1. VISUALIZING INPUT DATA')
    print('2. DRAWING HISTOGRAM OF TRAINING DATA')
    print('3. COMPOSITE IMAGES')
    print('4. UNSUPERVISED CLASSIFICATION')
    print('5. SUPERVISED CLASSIFICATION')
    print('6. POST CLASSIFICATION')
    print('7. PCA')
    print('8. EXPORT DATA')
    print('9. COME BACK TO MAIN MENU')
    print('0. TERMINATE THE PROGRAM')    
    choice = input('>> ')
    exec_menu(choice)    
###################



#FUNCTION
menu_actions = {}
#FUNCTION EXECUTE MENU
def exec_menu(choice):
    #os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            if ch in ['9','0']:
                menu_actions[ch]()
            elif ch == '1':
                menu_actions[ch](imgarr,imgarrcldrmove,optname,subset,dtmbol,dsmbol,vegibol,trainarr,pcaimgarr,pcaimgarrcldrm)
                choice = input('>> ')
                exec_menu(choice)
            elif ch == '2':
                menu_actions[ch](imgarr,trainarr,optname,dsmbol,dtmbol,vegibol,pcaarr)
                choice = input('>> ')
                exec_menu(choice)
            elif ch == '3':
                menu_actions[ch](imgarr,optname)
                choice = input('>> ')
                exec_menu(choice)
            elif ch == '4':
                menu_actions[ch](imgarr)
                choice = input('>> ')
                exec_menu(choice)
            elif ch == '5':
                menu_actions[ch](imgarrcldrmove,trainarrcldfree,trainarr,subdir,pcabol,pcaimgarrcldrm)
                choice = input('>> ')
                exec_menu(choice)
            elif ch == '7':
                menu_actions[ch](imgarr)
                choice = input('>> ')
                exec_menu(choice)
            elif ch == '8':
                menu_actions[ch](imgarr,imgarrcldrmove,indir,subdir)
                choice = input('>> ')
                exec_menu(choice)               
        except KeyError:
            print('INVALID SECTION, PLEASE TRY AGAIN. \n')
            menu_actions['main_menu']()
######################
#FUNCTION BACK TO MAIN MENU PROGRAM
def back():
    menu_actions['main_menu']()    
###################################

#FUNCTION EXIT PROGRAM
def exit():    
    sys.exit()
######################
    
#MENU DEFINITION
menu_actions = {
        'main_menu': main_menu,
        '1': visualinput,
        '2': plottrainpair,
        '3': plotcomposite,
        '4': unsupervise,
        '5': luclassify,
        '7': pcatrans,
        '8': export2imray,
        '9': back,
        '0': exit}
###############
#MAIN PROGRAM
if __name__ == '__main__':
    main_menu()    
#############
