# Description
A command line Reverse Polish Notation (postfix) calculator program.

# Usage 
Installing this package also installs the `pyrpncalc` command. Executing it will enter the program's interactive mode.

Example expressions:
```
    "1 1+" = (1+1)
        => 2
    "1 2 + 3 4 + /" = (1+2)/(3+4)
        => 0.428571428571
    "pi sin" = sin(pi)
        => 0.000000000000
    "2 sqrt 2 sqrt *" = sqrt(2)*sqrt(2)
        => 2.000000000000
    "2 2 inv ^ 2 ^" = (2^(1/2))^2
        => 2.000000000000
    "10 cos 2 ^ 10 sin 2 ^ +" = cos(10)^2 + sin(10)^2
        => 1.000000000000
    "2 dup +" = (2+2)
        => 4.000000000000
    "e pi n ^" = e^(-pi)
        => 0.043213918264
```
