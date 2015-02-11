#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 16:26:33 2013

@author: flam
"""



import argparse,sys,subprocess,os,string,re,codecs,shutil

# simple command
simple_command="\{(.*?)\}"

graphics_list=['png','jpg','jpeg','gif','eps','PNG','JPG','GIF','EPS','pdf','PDF']

class_style_list=[['documentclass','cls'],
                  ['usepackage','sty'],
                  ['bibliographystyle','bst'],]
                  
                  
encoding_corr={'ascii':'ascii','utf8':'utf8','latin1':'latin1','macce':'maccentraleurope','applemac':'maccentraleurope','ansinew':'cp1252'}

def run_command(cmd,wait=True):
    proc=subprocess.Popen(cmd,shell=True)
    if wait:
        proc.wait()
        
def load_file(fname,encode="utf8"):
    try:
        f=codecs.open(fname, mode="r", encoding=encode)
        txt=f.read()
        f.close()
    except IOError:
        txt=None  
        print "Error opening file:",fname
    return txt
    
def load_file0(fname):
    try:
        f=open(fname)
        txt=f.read()
        f.close()
    except IOError:
        txt=None  
        print "Error opening file:",fname
    return txt    
            
def save_file(fname,txt,encode="utf8"):
    try:
        f=codecs.open(fname, mode="w", encoding=encode)
        txt=f.write(txt)
        f.close()
    except IOError:
        print "Error writing file"   

    
def get_list_command(command,txt):
    #print '\\'+command+"\{(.*?)\}"
    return re.findall('\\\\'+command+"\{(.*?)\}", txt) 
    
def clean_comments(txt):
    txt=re.sub('(?<!\\\\)%(.*)\n','',txt)
    return txt
    
def copy_insert_images(path,txt,args):
    lst=re.findall(r'\\includegraphics\[(.*)\]\{(.*?)\}', txt) 
    
    gpath=path
    if not args.graphicpath:
        gp=get_list_command('graphicspath',txt)
        if gp:
            args.graphicpath=gp[0]
            gp[0]=gp[0].replace('{','')
            gpath=path+gp[0]
            if args.verbose:
                print 'Graphic path:',gpath
    
    
    for opt,fname in lst:
        basename=os.path.basename(fname)
        fname0=fname
        fname, ext = os.path.splitext(fname)
        if args.verbose:
            print 'Copying image:',basename
        #print ext
        if len(ext)>0:
            if os.path.exists(gpath+fname+ext):
                shutil.copyfile(gpath+fname+ext,args.outputfolder+'/'+basename)    
        else:         
            for ext in graphics_list:
                #print path+fname+'.'+ext
                if os.path.exists(gpath+fname+'.'+ext):
                    shutil.copyfile(gpath+fname+'.'+ext,args.outputfolder+'/'+basename+'.'+ext)
        txt=txt.replace('{'+fname0+'}','{'+basename+'}')
    
    return txt
    
    
def insert_input_files(path,txt,main,args):
    
   # extract input files
    lst_input=get_list_command('input',txt)
    
    if args.verbose:
        if main:
            print 'Input files:'
            print lst_input
    
    # handle input
    txt_input=list()
    for inpt in lst_input:
        if inpt[-4:]=='.tex':
            inpt=inpt[:-4]
        txt_input.append(parse_file(path+inpt+'.tex',args,False))
    txt=replace_list_command('input',txt,lst_input,txt_input)


   # Extract include files
    lst_input=get_list_command('include',txt)
    
    if args.verbose:
        if main:
            print 'Include files:'
            print lst_input
    
    # handle input
    txt_input=list()
    for inpt in lst_input:
        if inpt[-4:]=='.tex':
            inpt=inpt[:-4]
        txt_input.append(parse_file(path+inpt+'.tex',args,False))
    txt=replace_list_command('include',txt,lst_input,txt_input)

    
    return txt
    
def replace_biblio(path,basename,txt,args):
    
    lst=get_list_command('bibliography',txt)
    
    if lst:
        bib=lst[0]
        if os.path.exists(path+basename[:-4]+'.bbl'):
            if args.verbose:
                print 'Inserting bibliography:',bib
            bb=load_file(path+basename[:-4]+'.bbl',args.encoding)
            txt=txt.replace('\\bibliography{'+bib+'}',bb)
        else:
            print "Warning: no *.bbl file, compile with bibtex for a bibliograpy"
    return txt
    
def copy_class_style(path,txt,args):
    # case without options
    for command,ext in class_style_list:
        ls=get_list_command(command,txt)
        for cls in ls:
            if os.path.exists(path+cls+'.'+ext):
                shutil.copyfile(path+cls+'.'+ext,args.outputfolder+'/'+cls+'.'+ ext)
                if args.verbose:
                    print 'Copying file:',cls+'.'+ext
        # case with options
        ls=re.findall(r'\\documentclass\[(.*)\]\{(.*?)\}', txt)
        for cls in ls:
            if os.path.exists(path+cls[1]+'.'+ext):
                shutil.copyfile(path+cls[1]+'.'+ ext,args.outputfolder+'/'+cls[1]+'.'+ ext)  
                if args.verbose:
                    print 'Copying file:',cls[1]+'.'+ ext

def replace_list_command(command,txt,lst,lstreplace):
    for i in range(len(lst)):
        txt=txt.replace('\\'+command+'{'+lst[i]+'}',lstreplace[i])
       # print txt
    return txt
    
def set_encoding(txt,args):
    if not args.encoding:
        args.encoding='utf8'
        ls=re.findall(r'\\usepackage\[(.*)\]\{inputenc\}', txt)
        if ls:
            if ls[0] in encoding_corr:
                args.encoding=encoding_corr[ls[0]]
            else:
                args.encoding=ls[0]
    print args.encoding
            

    
def parse_file(fname,args,main=True):
    
    if os.path.dirname(fname):
        path= os.path.dirname(fname)+'/'
    else:
        path=''


    if main:
        txt=load_file0(fname)
        txt=clean_comments(txt)
        set_encoding(txt,args)
    else:
        if args.verbose:
            print 'Sub file:',fname       
        
    #print args.encoding
    
    txt=load_file(fname,args.encoding)
    
    # cleaning comments
    txt=clean_comments(txt)        
	
    
    # copy and insert image file
    txt=copy_insert_images(path,txt,args)
    

    #print txt
    copy_class_style(path,txt,args)

    # inserting input files
    txt=insert_input_files(path,txt,main,args)
    
    if main:

        basename=os.path.basename(fname)

        txt=replace_biblio(path,basename,txt,args) 
        
        save_file(args.outputfolder+'/'+basename,txt,args.encoding)
    else:
        pass
    
        
    return txt
        
    
    



def main(argv):  

    parser = argparse.ArgumentParser(prog='clean_latex',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
        description='''utility for cleaning complex latex files''',
    epilog='''''')   
    
    parser.add_argument('-o','--outputfolder',help='force the use of oarsub',default="clean_latex") 
    parser.add_argument('-g','--graphicpath',help='path for graphic files',default="")
    parser.add_argument('-v','--verbose',action='store_true',help='use verbose printing mode')
    parser.add_argument('latexfile',help='use verbose printing mode',default="cleanlatex")
    
    parser.add_argument('-e','--encoding',help='force encoding for the files',default='')
    
    args= parser.parse_args()   
    
    if args.latexfile:
        if not os.path.exists(args.outputfolder):
            os.mkdir(args.outputfolder)
        txt=parse_file(args.latexfile,args)
        #print txt
    else:
        print("Not a valide file name")

            


if __name__ == "__main__":
   #import doctest
   #doctest.testmod(verbose=True)   
   main(sys.argv[1:])
   #print get_dependence('./launch_octave.sh {module} {script} {param}')
