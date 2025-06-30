# Intextual File Lang

Intext is a lightweight, Python-powered scripting language built for embedding structured text and reading external files. It's meant to be simple, flexible, and readable, yet closer to natural English than traditional programming languages (Some may argue). You write what you mean, and it just works (in theory).

## Current Features

- `output` statements for printing anything (int, string, bool, whatever)
- Variable declarations for `int`, `string`, `bool`, and `char`
- Basic error handling
- Comment support using `//`

<b>And more, make sure to check the docs</b>

#### RawText
RawText is an umbrella term to describe programming closer to the compenents of ISEC. In other words, you work more low-level.
- RawAST: The parser outputs an Abstract Syntax Tree, which the user (you) can make one to feed into the interpreter yourself. This makes running code much faster, but be warned: programming in RawAST is very verbose due to JSON's rules an the interpreter's rules. As the ASTs are made in a JSON file.

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
- <b>Also, check the docs for more info!</b>

## [Intext Playground](https://playground.devhatch.site)
For simplicity, for those who want to program in Intext, without dealing with the hassle of installing, running, and etc... I made a website that you can visit to code on! It parses to the latest release.
## <a href="https://elemnto56.github.io/Intextual_File_Lang/" target="_blank">Intext Documentation</a>
Here is the offical docs of Intext, where you can find all the ways to explore the beauty of Intext.

## Moving to Nim
The more I develop Intext in Python, the more I realize how slower running scripts gets. Due to this, I decided to venture out and see other faster languages. I first came across Rust which I though would be overkill for Intext, but then I found Nim. A good alternative to Python and with great speed. Stay tooned for the switch.

##  [Changelog](CHANGELOG.md)
View the latest and oldest changes!
