# RawText
RawText, is short for "Rawness of Intext", or "raw is a ``R``eally `A`wful ``W``ay to write in In``Text``". What it stands for is up to what you want it to be. RawText will in the future will have multiple things implemented into it, and each with a version number, will be tracked. 

### RawAST
**🛈 v0.6.1-pre and above only**

RawAST is a directive of RawText. RawAST allows you to program an Abstract Syntax Tree (AST). For comparison, standard ISEC takes Intext code, then makes tokens -> parses the tokens into an AST -> the interpreter shows output. Even though this process short, it takes longer than just simply making an AST, and interpreting it. I'd recommend those who like code that runs fast, and/or likes working low-level to use RawAST.

**How to change standard Intext to RawAST**
At the very first line, add the directive: 
``` plaintext
@RawAST
```

***

## RawAST Syntax
Be warned: RawAST is very verbose and strict. Expect to type a lot. Here are some things to know about ASTs:
### Components of an AST
Here is an example AST for Intext:
``` JSON
[
  {
    "type": "declare",
    "var_type": "int",
    "var_name": "x",
    "var_value": "5"
  },
  {
    "semicolon": ";"
  },
  {
    "type": "output",
    "value": "x"
  },
  {
    "semicolon": ";"
  }
]
```
This can be fed right into the interpreter to see your output. Though, what do certain things mean? Well, for starters, let's discuss why it looks like that. It's in a structured manner, because ASTs are put in JSON files. Due to this, they have to follow JSON rules as well. The interpreter reads the JSON, and outputs.

***Let's break down the code**
## Nodes
A statement in RawAST, is considered a node. How to identify a node, is by viewing the code surrounded in curly braces ({}). For example, the code below is a node.
```JSON
{
 "type": "output",
 "value": "Hello World!"
}
```
Without these, the interpreter wouldn't know what to do!

### Sub-Nodes
Sub-Nodes are regular Nodes, except contained in a Standard Key. Here is an example below, from a snippet of an If Statement. To learn more about If Statements, please view the [If Statements Chapter](if_statements.md).
```JSON
 body: [
  {
   "type": "output",
   "value": "Intext Rocks!1"
  }
 ]
```
In most cases, Sub-Nodes will be contained in brackets. Similar to how a usual Node would be.

### Special Nodes
Special Nodes are nodes with a small amount of keys and values, and usually appear either a lot or not a lot in an AST. Think of special nodes as Super-Key's long lost cousin. 

#### Semicolon Nodes
_As of version 0.6.2 and above, this lesson won't apply to you. For those who are on 0.6.1, please pay attention._ 
```JSON
{
 "semicolon": ";"
}
```
Semicolon Nodes are Special Nodes with one single key, and one value. They serve the purpose to be semicolons in what would be a line of Standard Intext. Semicolon Nodes must be places after each node. Failing to do so, will lead to an error. For an example on how to use them, look at the RawAST example. 

However, these rules do not apply to bodies in If Statements, and RawAST in versions 0.6.2. Reason being, ISEC now automatically inserts Semicolon Nodes after regular nodes. In other words, it expects the nodes to run, but does it automatically, so you don't have to type all that boilerplate.

## Keys
There are multiple types of keys in RawAST. Let's discuss them in detail.

### Standard Key
A Standard Key is a data type inside of a node. In the example above, ``value`` shown in the output node, is a Standard Key. Do know, that I'll refer to "Standard Keys" as "keys" out of simplicity. As for the data past the semicolon, that is a ``value``. Now, you may be confused that a key has the same name as a keyword, but don't think about it too much. Usually, nodes require a certain amount of keys and certain names of keys in order for the statement to run, but depending on your version, an error will likely get thrown to notify you.
 
### Super-Key
A Super-Key, is a key that is usually found across a lot of nodes. Not every node, but most. Due to that, they hold special importance to all nodes that contain them. For example, ``type`` is a Super Key that defines what concept a node will use. For instance, I want to make an ``output`` statement, I use the Super Key ``type``, and give it the value ``"output"``.

### Sub-Keys
A Sub-Key is a subset of a key. Similar to Standard Keys, it must have a certain amount and certain names for the key it's attached too. The code snippet below, it from an If Statement ``condition`` key. To learn more about If Statements, please view the [If Statements Chapter](if_statements.md)
```JSON
"condition": {
   "left": 5,
   "operator": "==",
   "right": 5
}
```
In this case, the ``left``, ``right``, and ``operator`` keys are the Sub-Keys to the ``condition`` key.

## Common Errors & Things not fully addressed
I'll try to keep this section sort, as ISEC should point out the errors well enough for you to know what went wrong. 

- **Error: No double-quotes**

This is a non-negotiable. Double-quotes are required for JSON, and must be used for the value of any key, even if Super Key. Failing to do so, could cause code to not become outputted correctly.

#### **Requirement: Each node must be seperated with a comma**

Each node must end their right-sided curly brace with a comma, like ``},`` unless it's the last node. Failing to do so, goes against JSON's rules, and will mess up output