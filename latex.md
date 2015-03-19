## Latex tricks

### Beamer
#### Beamer subsection toc

```latex
\AtBeginSubsection[]
{
  \mode<beamer>{
  \addtocounter{framenumber}{-1}
  \begin{frame}
    \frametitle{Section}
    \tableofcontents[currentsection,currentsubsection,subsubsectionstyle=show/show/shaded/shaded]
  \end{frame}  }
}
```

#### Beamer use classic math font

```latex
\renewcommand\mathfamilydefault{\rmdefault} 
```

For those who don't like the beamer math font.

#### Beamer references
To change from icons to text:

```latex
\setbeamertemplate{bibliography item}[text]
```

To change the color of the references:
```latex
\setbeamercolor{bibliography item}{fg=black,bg=blanc}
\setbeamercolor{bibliography entry title}{fg=black,bg=blanc}
\setbeamercolor{bibliography entry author}{fg=black,bg=blanc}
```

#### Beamer 4x4 slides

```bash
$ pdfnup --nup 2x2 --frame false --noautoscale false --landscape --delta "0.2cm 0.3cm" --scale 1 SOURCE.pdf --outfile TARGET.pdf
```



### Graphics
#### Graphics Path
To tell LaTeX where to find image:
```latex
\graphicspath{ {images_folder/}{/path/to/other/folder/}{/path/to/other/folder2/} }
```


### Misc

#### Context sensitive quotation
Idea: automatically get quotation according to the language.

First import the package:
```latex
\usepackage[babel=true]{csquotes}
```

Then, instead of standard quotation use:
```latex
A  superb quote:  \enquote{This  superb  quote subquotes:  \enquote{nice
isn't it ?}}
```


#### Emacs and flyspell

Force latex mode and flyspell:
```latex
%%% Local Variables: 
%%% mode: latex
%%% TeX-master: t
%%% flyspell-mode: 't'
%%% End: 
```



Force flyspell language:
```latex
%%% Local Variables: 
%%% ispell-local-dictionary: "french"
%%% End: 
```


#### Margins for the itemize/enumerate

To set the margin:
```latex
\addtolength{\leftmargini}{2.5em} 
```


