#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = """Remi Flamary """
try:
    import matplotlib.pyplot as plt
except:
    raise


import networkx as nx
import bibtex




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
          [u'\\\'a','a'], ]
          

    
def authors_to_txt(txt):
    authors=txt.split('and')        
    res=""
    for author in authors:
        author.strip()
        lst=author.split(',')
        if len(lst)>=2:
            res+= lst[-1].strip()+ ' ' + ''.join(lst[:-1]).strip()+ ', '
        else:
            res+= lst[0].strip()+ ', '
    res.replace('  ',' ')
    return res[:-2]
    #output==''
    
def unlatexit(chaine):
    # remove the most obvious latex commands..
    chaine=unicode(chaine)
    for key in latex_fr:
        chaine=unicode(chaine.replace(key[0],key[1])) 
    return (chaine)    
    
       
       
bibfile='biblio.bib'
bib=bibtex.load_bibfile(bibfile)

lst=bib

  
G=nx.Graph()

# weight added for each publication
w0=10

for paper in lst:
    print paper['key']
    for temp in unlatexit(authors_to_txt(paper["author_tex"])).split(', '):
        for temp2 in unlatexit(authors_to_txt(paper["author_tex"])).split(', '):
            if temp and temp2:
                if temp == temp2:
                    G.add_edge(temp,temp2,weight=0)
                else:
                    G.add_edge(temp,temp2,weight=w0)
#                
for paper in lst:
    for temp in unlatexit(authors_to_txt(paper["author"])).split(', '):
        for temp2 in unlatexit(authors_to_txt(paper["author"])).split(', '):
            if temp and temp2 and not temp==temp2:
                G[temp][temp2]['weight'] = G[temp][temp2]['weight']+1

pos=nx.graphviz_layout(G,prog='fdp')

k=10
col=[]
for edge in G.edges():
    col.append(G[edge[0]][edge[1]]['weight'])


plt.clf()
nx.draw(G,pos,node_size=0,node_color='#A0CBE2',width=1,edge_color=col,edge_cmap=plt.cm.Blues,with_labels=True,alpha=.2)
#,edge_cmap=plt.cm.Blues

#plt.savefig("edge_colormap.png") # save as png
#plt.savefig("edge_colormap.svg") # save as png
plt.show() # display
