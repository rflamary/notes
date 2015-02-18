## Latex tricks


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
