# Control Flow

**If Statements** are a somewhat basic programming concept that is heavy on logic. Intext uses **If Statements** similarly to other languages to keep it simple.

## RawAST
```JSON
{
 "type": "if",
 "condition": {
    "left": 5,
    "operator": ">",
    "right": 3
  },
  "body": [
    {
     "type": "output",
     "value": "Hello World"
    }
  ]
}
```

This is an If Node in RawAST. *Let's break it down*

- We start off with the ``type`` Super Key define what concept is being used. In the case, it's an If Statement. To learn more about Super Keys, view the [RawText Chapter](rawtext.md).
- The "condition" key is the introduced with Sub-Keys.

# WIP 