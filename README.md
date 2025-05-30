# Intextual File Lang

Intext is a lightweight, Python-powered scripting language built for embedding structured text and reading external files. It's meant to be simple, flexible, and readable, yet closer to natural English than traditional programming languages (Some may argue). You write what you mean, and it just works (in theory).

## Current Features

- `output` statements for printing anything (int, string, bool, whatever)
- Variable declarations for `int`, `string`, `bool`, and `char`
- Basic error handling
- Comment support using `//`

#### RawText
RawText is an umbrella term to describe programming closer to the compenents of ISEC. In other words, you work more low-level.
- RawAST: The parser outputs an Abstract Syntax Tree, which the user (you) can make one to feed into the interpreter yourself. This makes running code much faster, but be warned: programming in RawAST is very verbose due to JSON's rules an the interpreter's rules. As the ASTs are made in a JSON file.

### Ones only for v0.5-pre
- `crunch()` function for basic math (`+`, `-`, `*`, `/`) with optional string conversion
- `read()` function to pull in content from text files
- Loosely typed output: mix anything together (ex: a bool and int can output together)
- Comment support using `//`
- Basic error handling

## How to Run
### For v0.3 and v0.5
```bash
python3 og_parser.py <filename>.itx
```
### For v0.6 and above
```bash
python3 main.py
```
- Make sure your file ends in .itx so it'll work!

### **🛈 More info can be seen in the Wiki tab of this repo**

## [Intext Playground](https://www.devhatch.site)
For simplicity, for those who want to program in Intext, without dealing with the hassle of installing, running, and etc... I made a website that you can visit to code on! It parses to the latest release.

## - BIG CHANGE; ISEC INFO -
The way Intext runs, will be soon changed starting v0.7-pre. By change, I mean that Intext will run on a system called "ISEC", rather than a single file. ISEC stands for "Intext Script Execution Core", which will turn code into tokens, then into AST, then into execution. Developing this will be difficult, so expect a long wait. An expriemental version of ISEC has been released on v0.6-pre. Check the releases and stay tuned!

##  [Changelog](CHANGELOG.md)
