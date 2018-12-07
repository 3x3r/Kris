import os
from lxml import etree
import datetime
import time
import openpyxl
wb = openpyxl.load_workbook(filename='C:\\Python27/upload.xlsx')
sheet = wb['Лист1']
violations={'tSolidLine':'/report/targetinfo/tSolidLine/text()','nRedLight':'/report/targetinfo/nRedLight/text()','nWrongDirection':'/report/targetinfo/nWrongDirection/text()','tRoadSide':'/report/targetinfo/tRoadSide/text()','tStopLine':'/report/targetinfo/tStopLine/text()','tOneDirection':'/report/targetinfo/tOneDirection/text()','nOverSpeed':'/report/targetinfo/nOverSpeed/text()'}
forsage={'F401':['F401'],'F402':['F402'],'F403':['F403'],'F404':['F404'],'F405':['F405'],'F406':['F406'],'F407':['F407'],'F408':['F408'],'F409':['F409'],'F410':['F410'],'F413':['F413']}
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
     d= value.strftime('%d')
     b= value.strftime('%B')
     y= value.strftime('%Y')
     time = value.strftime('%H:%M:%S')
     return (d,b,y,time)
def timeunix (d,m,y,hh,mm,ss): #из юникс времени в формат time
    time_tuple = (y, m, d, hh, mm, ss, 0, 0, 0)
    timestamp = time.mktime(time_tuple)
    print(repr(int(timestamp)))
    return (timestamp)
def s_viol (treexml):
    for lang,lang1 in violations.items():  #проход по дереву XML и посик нарушений
        if (treexml.xpath(lang1))==['1']:   # если найден путь в дереве берем его значение и сравниеваем
            for lang2,lang3 in forsage.items(): # поиск номера форсажа
                if (treexml.xpath('/report/targetinfo/tDeviceSerial/text()'))==lang3: #если наден номер форсажа сравниеваем его со списком
                    k=forsage100[lang2][lang]       #присваиваем текущее значение ключ:значение forsage[401][tSolidLine] буферной переменной
                    forsage100[lang2][lang]=k+1     #добавляем к текущему значению +1
    return ()
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
end_mm=40
end_ss=00
print(end_d,' ',end_m,' ',end_y,' ',end_hh,' ',end_mm,' ',end_ss)
starttime=int(timeunix(start_d,start_m,start_y,start_hh,start_mm,start_ss))
endtime=int(timeunix(end_d,end_m,end_y,end_hh,end_mm,end_ss))
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
#sheet['B2'] = 'test'
for x in forsage100.keys():
    #print (forsage100[x])
    #for z in forsage100[x].keys():
#    print ('Test2222',x,forsage100[x]['nRedLight'])
    sheet.append([str(start_d)+'-'+str(start_m)+'-'+str(start_y), str(start_hh)+':'+str(start_mm)+':'+str(start_ss),str(end_d)+'-'+str(end_m)+'-'+str(end_y),str(end_hh)+':'+str(end_mm)+':'+str(end_ss),x,forsage100[x]['tSolidLine'],forsage100[x]['nRedLight'],forsage100[x]['nWrongDirection'],forsage100[x]['tRoadSide'],forsage100[x]['tStopLine'],forsage100[x]['tOneDirection'],forsage100[x]['nOverSpeed']])
#print ('TEST11',forsage100.keys())#(['F401', 'F402', 'F403', 'F404', 'F405', 'F406', 'F407', 'F408', 'F409', 'F413'])
#print('Test3',forsage100['F401'].values()) #([3, 0, 0, 0, 0, 0, 0])
#print('Test4',forsage100['F401'].keys()) #(['tSolidLine', 'nRedLight', 'nWrongDirection', 'tRoadSide', 'tStopLine', 'tOneDirection', 'nOverSpeed'])
#print('TEST',forsage100['F401']['tSolidLine'])
#print(forsage100)
wb.save('C:\\Python27/upload.xlsx')