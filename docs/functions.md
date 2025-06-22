# Functions

## crunch()
Crunch stands for "crunch da numbas", or for a more formal and easy to understand way: "crunch the numbers". Crunch solves four-function math equations. The functions being addition, subtraction, division, and multiplication. Along with that, ``crunch()`` can be forced to be a string, and not to be a int like usual.

If the string type is not forced in ``crunch()``, then it will return a int. Crunch must be assigned to a variable using ``declare``, with its respected type specifier. For more information about ``declare``, check out the chapter for Declare Syntax in the wiki.

Here are some examples:

**Addition**
``` intext
int declare x = crunch(5, 5, +);
``` 

**Subtraction**
``` intext
int declare x = crunch(5, 5, -);
``` 

Note: The first number gets subtracted by the second. Had to point that out, as some mathematicians do it the other way around.

**Division**
``` intext
int declare x = crunch(5, 5, /);
``` 

**Multiplication**
``` intext
int declare x = crunch(5, 5, *);
``` 

**Example when string is forced:**

``` intext
string declare x = crunch(5, 5, +, string);
```
Notice how a fourth argument was added? That's what converts the returned value into a string. Also, notice how the type specifier for declare is ``string``? This is in place, so a type mismatch does not occur. Let it be noted: crunch can only force return a ``string``.

***

## read()

``read()`` is used to read the file contents of a file. There is only one argument, with that being the path. ``read()`` must be assigned to a ``string`` variable using ``declare``. In order to see the file contents, output the variable.

``` intext
string declare x = read("file.txt");
```

It doesn't matter if the path is put in double-quotes, or just by itself. However, double-quotes look neater. 

For the ``path`` argument of ``read()``, you need to make sure it is either in your directory, a previous directory, or a deeper directory. To refer to file in your directly, just simply type the full file name; no need to include the ``./`` path. To refer to a previous directory, use ``../file.txt``. For example:

> **Main**

> file.txt
>> **Current**

>> og_parser.py

>> main.itx

(Sorry if that was a bad example)

For a file in a deeper directory, just use the name of the directory, and add the file ``my_dir/file.txt``. Example:

> **Main**

> og_parser.py

> main.itx
>> **my_dir**

>> file.txt

### Limitation(s) of ``read()``
Try not to make paths for ``read()`` be too complex. As trying to read the file, could cause an error. At the time of writing this, I do plan to patch these errors. Also, by complex, I mean a path like:

``/home/user/my_dir/folder/name.txt``

or

``~/texts/file.txt`` 

Doing so, has the possibly of undefined behavior

***

## write()

``write()`` is used to write to a file. Similar to all programming lanaguges, it creates the file, and writes what you wanted to be written. Along with that, if you ``write()`` to an existing file, it'll overwrite all of it's contents.

#### Syntax 
```intext
write(<file>, <text>)
```

- Example:
```intext
write("shopping_list.txt", "1. Eggs\n2. Milk")
```

Since write doesn't return a value, it's considered a <b>Standalone Function</b>. Meaning, you can just write it in the void, rather than assign it to a variable like ``read()``. 