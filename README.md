# EPAi-Modules

Modules

*Python has a way to put definitions in a file and use them in a script or in an interactive instance of the interpreter. Such a file is called a module; definitions from a module can be imported into other modules or into the main module.*

*A module is a file containing python definitions and statements. The file name is the module name with the suffix .py appended. Within a module, the module’s name (as a string) is available as the value of the global variable __name__.*

*Each module has its own **private symbol table**, which is used as the global symbol table by all functions defined in the module
*Modules can import other modules. The imported module names are placed in the importing module’s global symbol table.

### Import and ImportLib

#### Variations of Import

  * import <Module Name> as <Alias Name>
  * from <Module Name> import <function Name>
  * from <Module Name> import *
  * from <Module Name> import *
  
**Each module is only imported once per interpreter session. If we have done some change in our modules, we must use importlib.reload()**
e.g. import importlib; 
importlib.reload(modulename)

### Creating ZIP application

By including the file `__main__.py` and Zipping up the required Python files into a zip file say `app.zip` by typing:



The file `app` is now have a zipped Python application that is ready to deploy as a single file.
python app

ZipApp commands also can be used to create python application:
https://docs.python.org/3/library/zipapp.html#creating-standalone-applications-with-zipapp

### ArgParse
*The argparse module makes it easy to write user-friendly command-line interfaces. The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv. The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments.*

```
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))
```
