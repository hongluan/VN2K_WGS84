# VN2K_WGS84
A small script supporting GIS and RS technicians in converting between Vietnamese national coordinate system (VN2000) and WGS84 back and forth. I adopted the codes in Python GDAL/OGR Cookbook and inherited codes by Br. Elias Max König. Links to these sources are listed in reference.
The transformation applies Molodensky Badekas method with 7 transformation parameters. These parameters were adopted from the report by Luyen et al. (2014).

INSTRUCTION

STEP 1: DOWNLOAD AND INSTALL ANACONDA

Link: https://www.anaconda.com/download/

STEP 2: INSTALL OSGEO LIBRARIES

Open Anaconda terminal (Prompt) and paste:

conda install -c conda-forge gdal 

conda install -c conda-forge/label/broken gdal

STEP 3: OPEN PYTHON FILE (.py) ON SPYDER OF ANACONDA

STEP 4: RUN THE SCRIPT

Hit Run File (F5)

STEP 5: 


Reference

Khac Luyen, B., Trung Dung, P., Dinh Toan, V., Thi Thu Trang, T., & Phuc Hong, N. (2014). Coordinates transformation between world geodetic system 1984 and vietnam geodetic system 2000 for maritime surveying and mapping.

http://geoinformaticstutorial.blogspot.com/2012/10/reprojecting-shapefile-with-gdalogr-and.html

https://pcjericks.github.io/py-gdalogr-cookbook/projection.html
