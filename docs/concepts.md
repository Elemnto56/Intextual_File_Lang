# Intext Concepts

## The Bound System
The Bound System is a classification model that separates Intext functions into two categories:

### In-Bound

These functions operate strictly within the script’s logic and follow Intext’s syntax rules. Example:

```
declare x = crunch(5, 5, +);
```
`crunch()` solves mathematical operations, and has no need to interact outside the file, therefore it is ``In-Bound``. Along with that, it must follow Intext's synaxt rules.

### Out-of-Bound

These functions interact with the outside world (files, user input, etc.), and may relax certain syntax rules. For example:
```
write("hello.txt", "I'm a file lol")
```
`write()` is ``Out-of-Bound`` because it interacts outside of the script. It doesn't need a semicolon because it's not following Intext's rules. Imagine it as someone leaving a city, and moving into a deserted lawless land. This system helps define what a function is allowed to do, how it's parsed, and whether it's sandbox-safe.

#### Note
The Bound System is still new at the time of writing and may expand in future versions. Expect additional classifications or behavior modifiers as Intext evolves.


## Text Blocs
