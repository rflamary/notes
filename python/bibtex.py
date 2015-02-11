# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 13:41:48 2012
@author: rflamary
"""
import datetime
import codecs


def to_list(string):
    """
    convert a str separated by ',' to a list
    """
    return string.split(',')


latex_fr=[[u'\\v{',u''],
          [u'\\_',u'_'],
          [u'\\c{c}',u'ç'],
          [u'\\{',u'\\ocb'],# tweak pour pouvoir toujour avoir des curls
          [u'\\}',u'\\ccb'],          
          [u'{',u''],
          [u'}',u''],
          [u'\\ocb',u'{'],
          [u'\\ccb',u'}'], 
          [u'\\\'e',u'é'],
          [u'\\`e',u'è'],
          [u'\\\'o','o'],
          [u'\\"u',u'ü'], 
          [u'\\"o',u'ö'],
          [u'\\"a',u'ä'],
          [u'\\`a',u'à'],
          [u'\\~n','n'],
          [u'\\&','&'],
          [u'\\\'a','a'],
          [u'"',''],  ]

bibsep=[["{","}"]]

field_list=['author',
            'title',
            'year',
            'journal',
            'booktitle',
            'howpublished',
            'institution',
            'school',
            'number',
            'pages',
            'volume',
            'publisher',
            'organization',
            'url',
            'school',
            'abstract',
            'key',
            'file',
            'pdf',            
            'code',
            'demo',
            'doi',
            'pres',
            'pubtype',
	    'submited']   
            

def unlatexit(chaine):
    # remove the most obvious latex commands..
    chaine=unicode(chaine)
    if not chaine =='':
        for key in latex_fr:
            chaine=unicode(chaine.replace(key[0],key[1])) 
    return (chaine)
    
def tryget(item,field):
    try:         
        res=item[field]
    except (KeyError):
        res=""
    return res
        
def prep_ref(ref):
    for field in field_list:
        ref[field]=unlatexit(tryget(ref,field))

def load_bibfile2(fname):
    
    #f = open(fname, "r")
    f = codecs.open(fname, "r", "utf-8")
    
    lines=f.readlines()
    
    lines=[l.replace('\t',' ') for l in lines]
    
    return get_biblist(lines)


def clean_spaces(txt):
    if len(txt):
        while len(txt) and txt[0]==' ':
            txt=txt[1:]
        while len(txt) and txt[-1]==' ':
            txt=txt[:-1]            
    return txt

def short_name(txt):
    def get_double(name):
        return u''.join([nm[0]+'.' for nm in name.split('-')])
    if '-' in txt:
        res=u' '.join([get_double(nm) for nm in txt.split(' ') if len(nm)>0])
    else:
        res=u' '.join([nm[0]+'.' for nm in txt.split(' ') if len(nm)>0])
    return res

def get_author(txt):

    ls2=list()
    for aut in txt.split(' and '):
        if ',' in aut:
            lst=clean_spaces(aut).split(',')
            ls2.append(lst[0]+', '+short_name(clean_spaces(u' '.join(lst[1:]))))
        else:
            lst=clean_spaces(aut).split(' ')
            ls2.append(lst[-1]+', '+short_name(clean_spaces(u' '.join(lst[:-1]))))
    #print ls2
    return u', '.join(ls2),[aut.split(', ')[1]+' '+aut.split(', ')[0] for aut in ls2]
    
    

def get_biblist(lines):
    bib=list()
    
    temp=dict()
    
    inref=False
    inkey=False
    
    #f= codecs.open('index2.html', "w", "utf-8")
    
    for l in lines:
        
        if l:        
            # if not in a current ref we search for a new entry
            if not inref:
                if l[0]=='@':#entry found
                    lst=l[1:].split('{')
                    t=lst[0] # get the pub type
                    ktemp=lst[1].split(',') # get rid of after the ,
                    #f.write(ktemp[0]+ '\n')
                    inref=True
                    temp=dict() # dictionnary 
                    temp['type']=t.lower()
                    temp['key']=ktemp[0]
                    #print temp['key']
            else:
                if l[0]=='}': # closing ref (necessary t)
                    prep_ref(temp)
                    bib.append(temp)
                    inref=False    
                else:
    
                    if not inkey:    # not locked in an opened key      
                        lst=l.split('=') # separate key and value
                        
                        key=lst[0].replace(' ','').lower()
                        val=u''.join(lst[1:])
                        #print '\t',key,val
                        if len(val)>0:
                            while val[-1]=='\n' or val[-1]==',' or val[-1]==' ' or val[-1]=='\r':
                                val=val[:-1]
                            temp[key]=val
                            
                        #f.write('\t'+ key + ' : ' + unlatexit(val)+'\n')
                        if not l.count('{')==l.count('}'):
                            opendif=l.count('{')-l.count('}')
                            val+=' '
                            inkey=True
                    else:
                        val+=l
                        temp[key]=val
                        if l.count('{')+opendif==l.count('}'):
                            inkey=False
                            while val[-1]=='\n' or val[-1]==',' or val[-1]==' ' or val[-1]=='\r':
                                val=val[:-1]
                            temp[key]=val
                        else:
                            opendif+=l.count('{')-l.count('}')
                
    return bib
    
def format_bib(bib):
    for temp in bib:
            #print temp['type']
            temp['author_tex']=temp['author']
            temp['author'],temp['author_list']=get_author(temp['author'])
            prep_ref(temp)
            temp['journalproc']=temp['journal']+temp['booktitle']+temp['howpublished']+temp['school']
            temp2=''
            if not temp['volume']=='':
                temp2+=' Vol. '+temp['volume']+','
            if not temp['number']=='':
                temp2+=' N. '+temp['number']+','             
            if not temp['pages']=='':
                temp2+=' pp '+temp['pages']+','
            temp['volnumpage']=temp2[:-1];
            #print temp
            if temp['title'][0]==' ':
                temp['title']=temp['title'][1:]
            temp['year']=temp['year'].replace(' ','')
            temp['submited']=clean_spaces(temp['submited'])	
            

def load_bibfile(fname,recentyears=3):
    bib=list()

    bib=load_bibfile2(fname)
    #print bib
    format_bib(bib)
    
    year=datetime.date.today().year
    reentyears=list()
    for i in range(recentyears):
        reentyears.append(str(year-i))

    for temp in bib:
        temp['recentyears']=reentyears
        #print temp['key'],temp['type'],temp['year']
        
    bib.sort(key=lambda k: k['year'],reverse=True)

    #for temp in bib:
    #    print temp['key'],temp['type'],temp['year']
    
    return bib



        
