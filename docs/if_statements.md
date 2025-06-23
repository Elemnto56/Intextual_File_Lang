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

This is an If Node in RawAST.

***Let's break it down***

- We start off with the ``type`` Super Key define what concept is being used. In the case, it's an If Statement. To learn more about Super Keys, view the [RawText Chapter](rawtext.md).
- The `condition` key is the introduced with Sub-Keys. This helps ISEC know if it should execute the body. As of *v0.7* the condition only takes simple stuff with the operators  `<`,`>`,`<=`, etc.
  - The Sub-Key ``left`` provides what is the first arg. Which will most likely be a number. This arg will be compared using the ``operator`` with the ``right`` Sub-Key
  - The Sub-Key ``operator`` uses the operators of ``<``, ``>``, ``<=``, ``>=``, and ``==``. Using these ``left`` and ``right`` are compared to one another, with the possiblity of the ``condition`` being ``true``
  - The Sub-Key ``right`` is compared via the ``operator`` with ``left`` with the possiblity of the overall `condition` being ``true`` or ``false``
- The `body` key introduces a list of Sub-Nodes. Each being executed if the ``condition`` is ``true``. In the above example, the ``output`` of the "Hello World" literal will execute because 5 > 3 is ``true``. 

### Note

If statements aren't as likely to be as maintained as other functions or features due to their complexity and safety nets needing to be applied. Due to this, I rarely touch on fixing these, not even with a 10 foot pole. 