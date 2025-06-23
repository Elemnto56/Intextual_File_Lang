# Declare

## Use and Origin
- Origin

I developed the name from how variables are ***declare***d. I believed using "declare" as a keyword, would let users easily identify what the statement is doing. 

- Use

If the name wasn't obvious enough, "declare" is used to give variables a value. For example, you want to give variable "x" the integer value of 5. Declare would be used for that. Along with that, declare can be used with built-in functions to give variables a special value.

***

## Note 

As of *v0.7*, type-specifiers are **deprecated** and not recommended for use anymore. Instead, disregarding the type of your variable's type, use simply ``declare`` and let ISEC infer the type.
```intext
declare x = 5
```

***

##  Types
There are 5 types that declare can assign a variable to. Each must have a type specifier of either: `` int ``, `` float ``, `` string ``,  `` bool ``, or `` char ``.

Do know: some types can have a built-in function assigned to them, which would be considered valid. A built-in function example, being read(). More about functions can be found out in their respected [chapter](functions.md).

***

### Integers (int)
`` int declare x = 5; ``

`` int declare big_num = 100000000; ``

Only whole numbers can be used with ints. Using a float such as 2.22, would throw an error.

***

### Floats/Decimals (float)
`` float declare y = 5.24; ``

`` float declare z = 8.23; ``

Similar to int, except with a rule change, only floats can be declared here. Something like 5 or even a string would throw an error.

***

### Strings/Text (string)
`` string declare name = "John Doe"; ``

`` string declare day = "Sunday"; ``

Only strings can be declared with the type specifier `` string ``. If a string is not used, an error will be thrown.

***

### Booleans (bool)
`` bool declare x = true; ``

`` bool declare y = false; ``

Booleans are strict. If want to assign a variable to a Truthy value, then use the word "true". However, if you want it to assign it to a Falsy value, used the word "false". As Intext develops, these will be more important for logic-handling.

***

### Characters (char)
`` char declare y = 'C'; ``
`` char declare z = 'H'; ``

Chars have a strict rule. You cannot use double-quotes to declare a char. Doing so, will throw an error. In v0.5-pre and before, errors may have been thrown regardless. These may have already been patched in later versions however.

***

## RawAST Declare Syntax

```JSON
{
 "type": "declare",
 "var_type": "void",
 "var_name": "x",
 "var_value": 5
}
```

Above, is a ``void declare`` node. It does not have a type specifier, because using it, will have ISEC automatically assume what type you need. Also, with the state of Intext as I am writing this, the type system was redundant. I won't go into to much detail about the node design due to how obvious it is, but the ``var_type`` key's value will change depending on what type you want specified. Whether it be ``char``, ``bool``, or ``string`` also make sure that the ``var_value``'s value is respective to the type. In other words, use common sense.

## Common Errors and Questions
- **What if I don't use a type specifier?**

In *v0.5* an error will be thrown if a type specifier is not used. In *v0.7* it's fine, in fact, expected.

- ***delcare***, **Common misspelling of "declare"**

I have suffered this typo way to many times to admit. Unfortunately, being a fast typer makes this error more common. The best thing you can do, is just read over your Intext file, and make sure the grammar is correct.


