Q1---
\documentclass{article}
\usepackage{graphicx} % Required for inserting images
\usepackage{lipsum} % Package to generate dummy text
\usepackage[margin=1in]{geometry} 
\usepackage{fancyhdr} % Package for headers and footers
\usepackage{multicol}
\usepackage{xcolor} % Package for colors
\usepackage{multirow}
\usepackage{longtable} % Package for tables spanning multiple pages
\usepackage{subcaption} % Package for subfigures
\usepackage{amsmath} % Package for advanced math typesetting
\usepackage{pdflscape}
\pagestyle{fancy} % Set page style to fancy

% Set headers and footers
\fancyhf{} % Clear default header and footer
\fancyhead[c]{Custom } % Header centered
\fancyfoot[C]{Page \thepage} % Footer centered with page number

 % Package for landscape pages
\title{Presentation}
\author{tiktokban }
\date{November 2023}

\begin{document}


\maketitle










% This is a comment in LaTeX
Hello, this is my \LaTeX \, document with comments!

% Introduction section
\section{Introduction}
This is a section. \\
Here's some text with a comment in the middle. % Comment within the text.

% Subsection
\subsection{Subsection}
This is a subsection.


% Dummy text generated with lipsum package
\lipsum[1] % Generating paragraphs of dummy text.

% Conclusion
\section{Conclusion}
In conclusion, LaTeX is a powerful typesetting system.
\begin{abstract}
This is the abstract of the article. It provides an overview of the content.
\end{abstract}

\section{Introduction}
This is the introduction section.
\lipsum[1-2] % Dummy text for demonstration

\section{Main Content}
This is the main content section.
\lipsum[1-2] % More dummy text

\section{Conclusion}
In conclusion, this article summarizes the main points discussed.

\newpage
\begin{landscape}
\section{Landscape Page}
This page is in landscape orientation.
\end{landscape}
\section{Introduction}
This is the introduction section.
\lipsum[1-2] % Dummy text for demonstration

% Creating two columns
\begin{multicols}{2}
\section{Two Columns}
This text is in two columns.
\lipsum[3-4] % More dummy text
\end{multicols}

\section{Main Content}
This is the main content section.
\lipsum[5-8] % More dummy text

% Creating three columns
\begin{multicols}{3}
\section{Three Columns}
This text is in three columns.
\lipsum[9-10] % More dummy text
\end{multicols}


\section*{Text Formatting Example}

% Styles
\textbf{Bold Text} \\
\textit{Italic Text} \\
\underline{Underlined Text} \\
\texttt{Typewriter Text} \\

% Size adjustments
{\tiny Tiny Text} \\
{\scriptsize Scriptsize Text} \\
{\footnotesize Footnotesize Text} \\
{\small Small Text} \\
{\normalsize Normal Size Text} \\
{\large Large Text} \\
{\Large Larger Text} \\
{\LARGE Very Large Text} \\
{\huge Huge Text} \\
{\Huge Very Huge Text} \\
{\emph{White rose and red word}} \\

% Alignment
\begin{flushleft}
Left-aligned Text
\end{flushleft}

\begin{center}
Centered Text
\end{center}

\begin{flushright}
Right-aligned Text
\end{flushright}

\section*{Colored Text and Page Example}

% Colored text
This is \textcolor{blue}{RED} text.
Some \textcolor{red}{BLUE} words here.

% Colored background for a block of text
\colorbox{yellow}{%
    \parbox{\linewidth}{%
        This block of text has a yellow background. It's colored with the \texttt{colorbox} command.\lipsum[1-2]%
    }%
}

\section*{Lists Example}

% Ordered (numbered) list
\subsection*{Ordered List}
\begin{enumerate}
    \item First item
    \item Second item
    \item Third item
\end{enumerate}

% Unordered (bullet point) list
\subsection*{Unordered List}
\begin{itemize}
    \item[-] Bullet point one
    \item Bullet point two
    \item[$\diamond$] Bullet point three
\end{itemize}

\section*{Mathematical Expressions Example}

% Subscripts and superscripts
$x_{i_{7}}$ (subscript) and $a^{2^{7}}$ (superscript).\\

% Fractions
$\frac{1}{2}$ (basic fraction) and $\frac{3x + 5}{2y - 1}$ (complex fraction).\\

% Binomials
\[(a + b)^2 = a^2 + 2ab + b^2\]

% Aligning equations
\begin{align*}
    2x + 3y &= 8 \\
    4x - 2y &= 6
\end{align*}
% Operators
$\sum_{i=1}^{n} i^2$ (sum) and $\int_{0}^{\infty} e^{-x} \, dx$ (integral).\\

% Greek letters and symbols
$\alpha$, $\beta$, $\gamma$, $\delta$, $\lambda$, $\sigma$, $\pi$, $\theta$, $\omega$.

\section*{Basic Table Example}

\begin{tabular}{|c|c|c|}
    \hline
    \textbf{Column 1} & \textbf{Column 2} & \textbf{Column 3} \\
    \hline
    Row 1, Cell 1 & Row 1, Cell 2 & Row 1, Cell 3 \\
    \hline
    Row 2, Cell 1 & Row 2, Cell 2 & Row 2, Cell 3 \\
    \hline
    Row 3, Cell 1 & Row 3, Cell 2 & Row 3, Cell 3 \\
    \hline
\end{tabular}
\section*{Table with Different Border Styles}



\begin{center}
\begin{tabular}{ |c|c|c|c| }   
\hline
col1 & col2 & col3 \\ 
\hline
\multirow{3}{4em}{Multiple row}
& cell2 & cell3 red bull \\
& cell5 & cell6 \\
& cell8 & cell9 \\  
\hline
\end{tabular}
\end{center}

\section*{Merging Rows and Columns in a Table}

\begin{tabular}{|c|c|c|}
    \hline
    \multicolumn{2}{|c|}{\textbf{Merged Columns}} & \multirow{2}{*}{\textbf{Merged Rows}} \\
     \cline{1-2}
    \textbf{Column 1} & \textbf{Column 2} & \\
    \hline
    Row 1, Cell 1 & Row 1, Cell 2 & \multirow{2}{*}{Combined Row 1-2} \\
    \cline{1-2}
    Row 2, Cell 1 & Row 2, Cell 2 & \\
    \hline
\end{tabular}

\section*{Figures and Subfigures with Properties}

\begin{figure}[htbp]
    \centering
    \begin{subfigure}[b]{0.4\textwidth}
        \centering
        \includegraphics[width=\textwidth]{example-image-a}
        \caption{Subfigure A}
        \label{fig:subfig-a}
    \end{subfigure}
    \hspace{1cm}
    \begin{subfigure}[b]{0.4\textwidth}
        \centering
        \includegraphics[width=\textwidth, angle=90]{example-image-b}
        \caption{Subfigure B rotated 90 degrees}
        \label{fig:subfig-b}
    \end{subfigure}
    \caption{Two subfigures}
    \label{fig:subfigures}
\end{figure}
\begin{longtable}[c]{|c|c|}
\caption{Long table caption, \label{long}}\\

\hline 
\multicolumn{2}{|c|}{Begin of Table}\\
\hline
Something & something else\\
\hline
\endfirsthead

\hline
\multicolumn{2}{|c|}{Continution of table}
\ref{long}\\
\hline
Something &something else\\
\hline
\endhead
\hline\multicolumn{2}{|c|}{End of table}\\
\hline\hline
\endlastfoot

Lots of lines & like this \\
Lots of lines & like this \\
Lots of lines & like this \\
Lots of lines & like this \\
Lots of lines & like this \\
Lots of lines & like this \\
Lots of lines & like this \\
Lots of lines & like this \\
...
\end{longtable}


\begin{eqnarray}
1 + 2 &=& 3 \\
4 + 5 + 0 &=& 7 + 8 \\
9 + 10 + 11 + 12 &=& 13 + 14 + 15 \\
16 + 17 + 18 + 19 + 20 &=& 21 + 22 + 23 + 24 \\
25 + 26 + 27 + 28 + 29 + 30 &=& 31 + 32 + 33 + 34 + 35 
\end{eqnarray}
\begin{eqnarray*}
(a + b)^2 &=& (a + b)(a + b) \\
&=&(a + b)a + (a + b)b\\ 
&=& a(a + b) + b(a + b) \\
&=& a^2 + ab + ba + b^2 \\
&=& a^2 + 2ab + b^2 \\
\end{eqnarray*}
\begin{eqnarray*}
\tan ( \alpha + \beta + \gamma) &=& \frac{\tan(\alpha+\beta)+\tan \gamma}{1-\tan(\alpha+\beta)\tan\gamma} \\
&=& \frac{\frac{\tan \alpha+\tan \beta}{1- \tan \alpha \tan \beta}+ \tan \gamma}{1- \left ( \frac{\tan \alpha+ \tan \beta}{1- \tan \alpha \tan \beta} \right) \tan \gamma} \\
&=& \frac {\tan \alpha + \tan \beta + (1-\tan \alpha \tan \beta) \tan \gamma}{1- \tan \alpha \tan \beta  (\tan \alpha + \tan \beta) \tan \gamma} \\
&=& \frac{\tan \alpha + \tan \beta + \tan \gamma- \tan \alpha \tan \beta \tan \gamma}{1- \tan \alpha \tan \beta- \tan \alpha \tan \gamma - \tan \beta \tan \gamma}
\end{eqnarray*}
\begin{tabular}{|l|l|l|} \hline     
\multicolumn{3}{|c|}{Country List} \\ \hline
Country Name or Area Name & ISO ALPHA 2 code & ISO ALPHA 3 \\ \hline
Afghanistan & AF & AFG \\
Aland Islands & AX & ALA \\
Albania & AL & ALB \\
Algeria & DZ & DZA \\
American Samoa & AS & ASM \\
Andorra &   AD & AND \\
Angola & AO & AGO \\ \hline

\end{tabular}




\end{document}# Document-prepration-

Q2
Hello World!

Prof. Naveen Kumar

November 15, 2022

Hello World! Today I am learning WTEX. WTEX is a great program for writing math. I can write inline math such as a² + b² = 2. I can also give equations their own space:

2²+0² = w²
Q3
\documentclass{article]

2

\title{Hello world!} \author{Prof. Naveen Kumar

\date{November 15, 2022)

6

7+ \begin{document}

8

9 \maketitle

10

11 \textbf{Hello world!) Today I am learning \LaTeX. \LaTeX is a great program for writing math. I can write inline math such as Sa^2 + b^2 = CA25. I can also give equations their own space: $$\gamma^2 + \theta^2 = \omega^2$$

12

13 \end{document]
Q4
\documentclass{article}

2 \usepackage{amsfonts, amsmath, amssymb}

3 \usepackage{es int}

4 \title{Integrals, Sums and Limits}

5 \author{Dr. Neeraj Kumar Sharma}

6 \date{}

7

8. \begin{document}

9 \maketitle

10

11. \section{Integrals}

12 Integral $\int_{a}^{b} x^2 \,dx$ inside text.

13

14 \vspace{0.2cm}

15 The same integral on display: $$\int_{a}^{b} x^2 \,dx$$\\

16 and multiple integrals:

17. \begin{gather*}

18

\iint_V \mu(u,v) \,du\,dv\\

19 \iiint_V \mu(u,v,w) \,du\,dv\,dw\\

20

\oint_V f(s) \,ds

21 \end{gather*}

22. \section{Sums and Products}

23 Sum $\sum_{n=1}^{\infty} 2^{n} = 15 inside text.

24

25 The same sum on display: $$\sum_{n=1}^{\infty} 2^{n} = 15$

26

27 Product $\prod_{i=a}^{b} f(i)$ inside text.

28

29 The same product on display: $$\prod_{i=a}^{b} f(i)$$

30 \section{Limits}

Limit $\lim_{x\to\infty} f(x)$ inside text.

31

32

33 The same limit on display: $$\lim_{x\to\infty} f(x)$$

34 \end{document}
