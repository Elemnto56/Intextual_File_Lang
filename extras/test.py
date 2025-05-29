string = """
[
{
  "type": "declare",
  "var_type": "int",
  "var_name": "x",
  "var_value": 5
},
{
  "type": "declare",
  "var_type": "bool",
  "var_name": "flag",
  "var_value": "true"
},
{
  "type": "if",
  "condition": {
    "left": "x",
    "operator": "==",
    "right": 5
  },
  "body": [
    {
      "type": "output",
      "value": "x is five"
    },
    {
      "semicolon": ";"
    }
  ]
},
{
  "type": "if",
  "condition": {
    "left": 5,
    "operator": "!=",
    "right": 3
  },
  "body": [
    {
      "type": "output",
      "value": "5 is not 3"
    },
    {
      "semicolon": ";"
    }
  ]
},
{
  "type": "if",
  "condition": {
    "left": "flag",
    "operator": "==",
    "right": "true"
  },
  "body": [
    {
      "type": "output",
      "value": "Flag is on"
    },
    {
      "semicolon": ";"
    }
  ]
},
{
  "type": "if",
  "condition": {
    "left": 10,
    "operator": ">",
    "right": 2
  },
  "body": [
    {
      "type": "output",
      "value": "10 is greater than 2"
    },
    {
      "type": "output",
      "value": "Math checks out"
    },
    {
      "semicolon": ";"
    }
  ]
},
{
  "type": "if",
  "condition": {
    "left": 1,
    "operator": "<",
    "right": 2
  },
  "body": [
    {
      "type": "if",
      "condition": {
        "left": 100,
        "operator": "==",
        "right": 100
      },
      "body": [
        {
          "type": "output",
          "value": "Nested success"
        },
        {
          "semicolon": ";"
        }
      ]
    },
    {
      "semicolon": ";"
    }
  ]
}
]
"""

print(string[len(string)-2:len(string)].strip())