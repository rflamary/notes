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

For those who don't like the beamer math foont.

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


