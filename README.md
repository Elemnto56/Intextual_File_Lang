# Intextual File Lang

Intext is a lightweight, Python-powered scripting language built for embedding structured text and reading external files. It's meant to be simple, flexible, and readable, yet closer to natural English than traditional programming languages (Some may argue). You write what you mean, and it just works (in theory).

## Current Features

- `output` statements for printing anything (int, string, bool, whatever)
- Variable declarations for `int`, `string`, `bool`, and `char`
- `crunch()` function for basic math (`+`, `-`, `*`, `/`) with optional string conversion
- `read()` function to pull in content from text files
- Loosely typed output: mix anything together (ex: a bool and int can output together)
- Comment support using `//`
- Basic error handling

## How to Run

```bash
python3 parser.py <filename>
```
- Make sure your file ends in .itx so it'll work!
