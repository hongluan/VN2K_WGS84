# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 12:14:22 2018

@author: PHẠM ĐẶNG MẠNH HỒNG LUÂN
"""

from osgeo import gdal,ogr,osr
import os,sys

inshpdir = input('INPUT VECTOR FILE: ')
driver = ogr.GetDriverByName('ESRI Shapefile')
dataset = driver.Open(inshpdir)
layer = dataset.GetLayer()
def exportgeomwtk(layer):
    featlst = []
    for feat in layer:
        wkt = feat.GetGeometryRef().ExportToWkt()
        featlst.append(wkt)
    return featlst
def spatrefdef(layer):    
    spatref = layer.GetSpatialRef()
    print('Spatial reference of your input vector is: {}'.format(spatref))
    return spatref
def importfield(layer,outLayer):
    inLayerDefn = layer.GetLayerDefn()
    for i in range(0,inLayerDefn.GetFieldCount()):
        fieldDefn = inLayerDefn.GetFieldDefn(i)
        outLayer.CreateField(fieldDefn)
        print(i)
    outLayerDefn = outLayer.GetLayerDefn()
    return outLayerDefn
def newvect(layer):    
    newfulname = inshpdir.split('.')[-2] + '_Trans.shp'
    newname = inshpdir.split('.')[-2].split('\\')[-1]
    
    outdataset = driver.CreateDataSource(newfulname)
    outlayer = outdataset.CreateLayer(newname+'_Trans',geom_type = ogr.wkbPolygon)    
    return outlayer
def VN2K2WGS84(layer):
        
    prj = open('D:\\Tai_Lieu\\Tai_Lieu_Hoc\\GIS\\VN2K\\3405 (2).prj').read()
    vnspatref = osr.SpatialReference()
    vnspatref.ImportFromWkt(prj)
    wgsspatref = osr.SpatialReference()
    wgsspatref.ImportFromEPSG(4326)
    transform = osr.CoordinateTransformation(vnspatref,wgsspatref)
    
    newfulname = inshpdir.split('.')[-2] + '_Trans.shp'
    
    newname = inshpdir.split('.')[-2].split('\\')[-1]
    
    driver = ogr.GetDriverByName('ESRI Shapefile')
    outdataset = driver.CreateDataSource(newfulname)
    outLayer = outdataset.CreateLayer(newname+'_Trans',geom_type = ogr.wkbPolygon)    
    inLayerDefn = layer.GetLayerDefn()    
    for i in range(0, inLayerDefn.GetFieldCount()):
        fieldDefn = inLayerDefn.GetFieldDefn(i)
        outLayer.CreateField(fieldDefn)
    outLayerDefn = outLayer.GetLayerDefn()    
    for feature in layer:    
        geom = feature.GetGeometryRef()        
        geom.Transform(transform)    
        outFeature = ogr.Feature(outLayerDefn)    
        outFeature.SetGeometry(geom)        
        for i in range(0,outLayerDefn.GetFieldCount()):            
            outFeature.SetField(outLayerDefn.GetFieldDefn(i).GetNameRef(), feature.GetField(i))    
        outLayer.CreateFeature(outFeature)    
        outFeature = None          
    wgsspatref.MorphToESRI()
    file = open(newname+'_Trans.prj', 'w') 
    file.write(wgsspatref.ExportToWkt())
    file.close()
#MAIN MENU FUNCTION
def main_menu():
    os.system('clear')
    print('WELCOME TO COORDINATE TRANSFORMATION PROGRAM! \n')
    print('PLEASE CHOOSE OPERATION YOU WANT: \n')
    print('1. TRANSFORM VN2000 TO GEOGRAPHIC WGS84')
        
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
                menu_actions[ch](layer)                
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
        '1': VN2K2WGS84,
        
        '9': back,
        '0': exit}
###############
#MAIN PROGRAM
if __name__ == '__main__':
    main_menu()    
#############
