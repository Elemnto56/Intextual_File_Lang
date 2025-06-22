# Output

## Origin of Name and Use
Output is a print statement in Intext. Rather than follow the standard "print" word, I chose to make it as obvious as possible by using the keyword "output". Reason being, it wouldn't be hard to know which line is printing what's in output.

## Simple Output
``` intext
output "Hello World";
output 5;
```
The good ol` standard way to make a print statement. Except, the keyword being used is "output". 
- **Note:** Regarding what is being said in output, do not forget to use a semicolon at the end of each statement

## Spaghetti Output 
**🛈 Only for version v0.5-pre**

``` intext
output "Population: " + 8.1 + "B";
output "Living equals " + true;
```
Theses lines are legal. Even tough it's multiple types in one output statement, as long as they are separated by '+' symbols, it's valid.

#### Spaghetti with variables
``` intext
int declare x = 5;
string declare y = "Number: ";
output y + x;
```
Once again, this is valid. While it may not be outputting literals, variables work as well.

## (Current) Limitations
``` intext
output 2 + 2; // Will output 22, because output makes them into strings
output crunch(5, 5, +); // Crunch cannot be used in output
```
These limitations will either be fixed in the future, or be implemented and maintained as a feature.

***

## RawAST Output Syntax
***🛈 I recommend you check [RawAST Syntax](rawtext.md) to better understand how these systems work!***
```JSON
{
 "type": "output",
 "value": "Hello, World!"
}
```
Making an Output Statement in RawAST is very simple, despite it's verbosity. First, use the Super-Key ``type``, and give it the value of ``"output"``. Next, add comma at the end to follow JSON's rules, and make the ``value`` key next. Then, whatever you want to print, give that value to the ``value`` key. Make sure if you're outputting a ``string`` (text), that it is wrapped in quotes. However, if you are printing the ``bool`` of ``true`` or ``false``, quotes are unneeded, along when outputting ``ints`` such as 5.


## Common Errors
- **You misspell output**

It happens to the best of us. The only way to defeat this error, is by checking through your code for typos. If enough people suggest, error-handling to catch these typos will be implemented.

- **You type something illegal**

I assume you have not read the entirety of this page if that is the issue. While Spaghetti Output may seem complex, it's best to not overthink it, because if you do, depending on the version, it will return a silent output.

- **You forgot the semicolon**

This is very surprising. You likely tripped up. No worries, just make sure to not to forget next time.

