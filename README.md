# pyLS
>"ls" implementation in python **3.6.7**

## Usage
>This project runs with **python3**
```
usage: pyLS.py [-h] [-a] [-R] [-l] [-c] [-d] [-r] [paths [paths ...]]

positional arguments:
  paths            Directory path, can be a list of path

optional arguments:
  -h, --help       show this help message and exit
  -a, --all        Display additional hidden files or directories
  -R, --Recursive  Recursive display
  -l, --long       Display the size of files or directories
  -c, --count      Display the number of lines in files
  -d, --directory  Display only directories, and the number of file in each
  -r, --reverse    Reverse the display order
```

## Tests

Run the following command: 
```
python3 -m unittest discover test/unit
```

## Disclaimer
To compare the order of the output, please make sure you run "ls" with the following locale:
```
LANG=C ls
```
