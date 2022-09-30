import pandas as pd
import pygtk, gtk
import csv

PATH_1 = './Geenbezpow1.csv'
PATH_2 = './Illuminabezpow1.csv'
PATH_3 = './GeenIluminabezpow1.csv'
PATH_4 = './Geenbezpow2.csv'
PATH_5 = './Illuminabezpow2.csv'
PATH_6 = './GeenIluminabezpow2.csv'
PATH_7 = './GeenIluminabezpowost.csv'

def BezPow(data):
	RS = data['rs'].drop_duplicates()
	positions = data['positions'].drop_duplicates() 
	dx = pd.DataFrame(data.drop_duplicates(), columns=['chip_name','rs','allele_f','allele_t','chromosome','positions','snp_name'])	
	return dx

def openCSV(path):
	with open(path) as csvfile:
		readCSV = csv.reader(csvfile,delimiter=',')
		data = []
		for row in readCSV:
			data.append(row)
	dy = pd.DataFrame(data, columns=['chip_name','rs','allele_f','allele_t','chromosome','positions','snp_name'])
	return dy
	
def CompareTotal(data1,data2):
	for b in data1:
		if b in data1['rs'] and not data1['chromosome'] and not data1['positions'] and not data1['snp_name']:
			data1.remove(b)
	for c in data2:
		if c in data2['rs'] and not data2['chromosome'] and not data2['positions'] and not data2['snp_name']:
			data2.remove(c)
	return data1+data2
	
def SaveFile(data,path):
	data.to_csv(path)	

dialog = gtk.FileChooserDialog("Open...", None,
		 gtk.FILE_CHOOSER_ACTION_OPEN, 
		 (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
		 gtk.STOCK_OPEN, gtk.RESPONSE_OK))
        
dialog.set_default_response(gtk.RESPONSE_OK)   
dialog.set_select_multiple(True)

filter = gtk.FileFilter()
filter.set_name("All_files")   
filter.add_pattern("*.csv")
dialog.add_filter(filter)

response = dialog.run()

if response == gtk.RESPONSE_OK:
    flista = [];
    flista = dialog.get_filenames();
    BTNGeen = openCSV(flista[0])    
    #print BTNGeen
    BTNGeenBezPow = BezPow(BTNGeen)
    #print BTNGeenBezPow
    SaveFile(BTNGeenBezPow,PATH_1)
    BTNIllumina = openCSV(flista[1])
    #print BTNIllumina
    BTNIllumniaBezPow = BezPow(BTNIllumina)
    SaveFile(BTNIllumniaBezPow,PATH_2)
    BTNGeenIluminaCT = CompareTotal(BTNGeenBezPow,BTNIllumniaBezPow)
    SaveFile(BTNGeenIluminaCT,PATH_3)
    UMDGeen = openCSV(flista[2])
    #print UMDGeen
    UMDGeenBezPow = BezPow(UMDGeen)
    SaveFile(UMDGeenBezPow,PATH_4)
    UMDIllumina = openCSV(flista[3])
    #print UMDIllumina
    UMDIllumniaBezPow = BezPow(UMDIllumina)
    SaveFile(UMDIllumniaBezPow,PATH_5)
    UMDGeenIluminaCT = CompareTotal(UMDGeenBezPow,UMDIllumniaBezPow)
    SaveFile(UMDGeenIluminaCT,PATH_6)
    BTNUMDGeenIluminaCT = CompareTotal(BTNGeenIluminaCT,UMDGeenIluminaCT)
    SaveFile(BTNUMDGeenIluminaCT,PATH_7)
    
