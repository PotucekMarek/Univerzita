echo Operating system is ; uname -o
true && echo This will not be printed ; echo This text was printed
true && echo this will be printed ; uname -o ; ; uname -o && true && echo this will  be printed