import os
from lxml import etree
import datetime
import time
violations={'tSoliddLine':'/report/targetinfo/tSolidLine/text()','nRedLight':'/report/targetinfo/nRedLight/text()','nWrongDirection':'/report/targetinfo/nWrongDirection/text()','tRoadSide':'/report/targetinfo/tRoadSide/text()','tStopLine':'/report/targetinfo/tStopLine/text()','tOneDirection':'/report/targetinfo/tOneDirection/text()','nOverSpeed':'/report/targetinfo/nOverSpeed/text()'}
forsage={'F401':'[F401]','F402':'[F402]','F403':'[F403]','F404':'[F404]','F405':'[F405]','F406':'[F406]','F407':'[F407]','F408':'[F408]','F409':'[F409]','F410':'[F410]'}

forsage100={'F401':{'tSolidLine':0,'nRedLight':0,'nWrongDirection':0,'tRoadSide':0,'tStopLine':0,'tOneDirection':0,'nOverSpeed':0},
'F402':{'tSolidLine':0,'nRedLight':0,'nWrongDirection':0,'tRoadSide':0,'tStopLine':0,'tOneDirection':0,'nOverSpeed':0},
'F403': {'tSolidLine': 0, 'nRedLight': 0, 'nWrongDirection': 0, 'tRoadSide': 0, 'tStopLine': 0,'tOneDirection': 0, 'nOverSpeed': 0},
'F404': {'tSolidLine': 0, 'nRedLight': 0, 'nWrongDirection': 0, 'tRoadSide': 0, 'tStopLine': 0,'tOneDirection': 0, 'nOverSpeed': 0},
'F405': {'tSolidLine': 0, 'nRedLight': 0, 'nWrongDirection': 0, 'tRoadSide': 0, 'tStopLine': 0,'tOneDirection': 0, 'nOverSpeed': 0},
'F406': {'tSolidLine': 0, 'nRedLight': 0, 'nWrongDirection': 0, 'tRoadSide': 0, 'tStopLine': 0,'tOneDirection': 0, 'nOverSpeed': 0},
'F407': {'tSolidLine': 0, 'nRedLight': 0, 'nWrongDirection': 0, 'tRoadSide': 0, 'tStopLine': 0,'tOneDirection': 0, 'nOverSpeed': 0},
'F408': {'tSolidLine': 0, 'nRedLight': 0, 'nWrongDirection': 0, 'tRoadSide': 0, 'tStopLine': 0,'tOneDirection': 0, 'nOverSpeed': 0},
'F409': {'tSolidLine': 0, 'nRedLight': 0, 'nWrongDirection': 0, 'tRoadSide': 0, 'tStopLine': 0,'tOneDirection': 0, 'nOverSpeed': 0},
'F413': {'tSolidLine': 0, 'nRedLight': 0, 'nWrongDirection': 0, 'tRoadSide': 0, 'tStopLine': 0,'tOneDirection': 0, 'nOverSpeed': 0}}
list_in=[]
#print ('Dictionares',violations)
#tSolidLine='' #12.16
#nRedLight=''  #12.12.1
#nWrongDirection=''
#tRoadSide=''
#tStopLine='./targetinfo/tStopLine'  #12.12.2
#tOneDirection='./targetinfo/tOneDirection'
#nOverSpeed='./targetinfo/nOverSpeed'    #12.9
path='C:\\Python27/'
def unixtime (timestamp): #из 28.10.2018 10:20:30 в юникс время
     timestamp =int(timestamp)
     value= datetime.datetime.fromtimestamp(timestamp)
     exct_time = value.strftime('%d %B %Y %H:%M:%S')
     print (exct_time)
     return (exct_time)
def timeunix (d,m,y,hh,mm,ss): #из юникс времени в формат time
    time_tuple = (y, m, d, hh, mm, ss, 0, 0, 0)
    timestamp = time.mktime(time_tuple)
    print(repr(int(timestamp)))
    return (timestamp)
def s_viol (treexml):
    for lang,lang1 in violations.items():
        if (treexml.xpath(lang1))==['1']:
            print((treexml.xpath('/report/targetinfo/tDeviceSerial/text()')))
            print(lang)
            list_in.append((treexml.xpath('/report/targetinfo/tDeviceSerial/text()')))
            list_in.append(lang)
         #   list_in.append(treexml.xpath('/report/targetinfo/tDeviceSerial/text()'))
        #if (treexml.xpath(lang.keys())) == ['1']:
            #print (lang1)
    return (list_in)
print ('Начало поиска дата месяц год часы минуты секунды')
start_d=28
start_m=11
start_y=2018
start_hh=9
start_mm=20
start_ss=00
print(start_d,' ',start_m,' ',start_y,' ',start_hh,' ',start_mm,' ',start_ss)
print('Конец поиска дата месяц год часы минуты секунды')
end_d=28
end_m=11
end_y=2018
end_hh=9
end_mm=25
end_ss=00
print(end_d,' ',end_m,' ',end_y,' ',end_hh,' ',end_mm,' ',end_ss)
starttime=int(timeunix(start_d,start_m,start_y,start_hh,start_mm,start_ss))
endtime=int(timeunix(end_d,end_m,end_y,end_hh,end_mm,end_ss))
solid = 0
cars_out = 0
cars_un = 0
for rootdir, dirs, files in os.walk(path): #парсинг пути
    for file in files:
        if((file.split('.')[-1])=='xml'): #поиск XML файлов
            xmlpath = os.path.join(rootdir,file)    #путь к XML файлу
            #print (os.path.join(rootdir,file))
            tree = etree.parse(os.path.join(rootdir,file)) #создаем дерево параметров XML
            for node in tree.iterfind('./targetinfo/nDatetime'):  # поиск элементов
                data =int(node.text)
                if (data>= starttime and data<= endtime):
                    s_viol(tree)
                   # print (node.text)
                    #for vio in tree.xpath(violations.keys()):
                     #   print (vio)
                    #solid =tree.iterfind('./targetinfo/tSolidLine')
                    #if (tree.xpath('/report/targetinfo/tSolidLine/text()')) == ['1']:
                     #   solid = solid+1
                      #  print ('test',solid)
# print(tree.xpath('/report/targetinfo/tSolidLine/text()'))
for i in list_in:
    for n in forsage.values():
            if i==n:
                print('TEST',i)
#print (forsage['F401']['tSolidLine'])