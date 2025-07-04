**Intextual File Lang Pre-Release v0.3.0**

**Release Date:** May 10, 2025
**Status:** The Beginning; The Original

**Highlights:**

- **Variable Declarations:**
    Introduced the ``declare`` keyword for defining typed variables.
    Example:
    ``` 
    int declare x = 5;
    string declare name = "Jaydog";
    ```

- **Print Statements:**
    Added the ``output`` keyword for console printing of literals and variables.
    Example:
    ```
    output "Hello, world!";
    output x;
    ```

**Purpose:**
    This version marks the first step toward building a minimal scripting experience focused on text output and type-safe variable assignment.
    **Notes:**

- Only supports basic types: int, float, char, bool, string. 
- Semicolons required at the end of each statement. 
- No expressions, no logic, no input — this release is deliberately basic to test core parsing and interpretation.

***

**Intextual File Lang – Version 0.5.0 Pre-Release**

**Title:** The 0.5 Release of Intext
**Status:** Alpha Milestone
**Release Date:** May 15, 2025

**Features Introduced:**

- ``crunch()`` Function (Math Operations):
    - A built-in utility to perform arithmetic between two values using a defined operator
    - Supports: ``+``, ``-``, ``*``, ``/``
    Example:
    ```
    int declare sum = crunch(5, 3, +);
    ```

- **Spaghetti Output Support:**
    - ``output`` can now accept multiple mixed-type values using concatenation with ``+``
    - Enables combining strings, numbers, booleans, and characters into a single output line
Example:
    ```
    output "Count: " + 5 + ", status: " + true;
    ```

- **read() Function (File Reading):**
    - Allows reading external file content as a string
Example:
    ```
    string declare content = read("file.txt");
    output content;
    ```

Notes:

- This version is the final release built under the single-file architecture where all logic (lexing, parsing, execution) was handled in one script
    
- Future versions transition into modular architecture under the ISEC system

- ``crunch()`` does not support nested or chained operations. It is strictly binary

- Spaghetti Output is limited to concatenation only. No interpolation or formatting is supported

- ``read()`` will return a raw string. Errors during file access are returned as error strings (not raised exceptions)

***

**Intextual File Lang – Version 0.6.0 Pre-Release**

**Title:** ISEC-lite for Intext
**Status:** Early Preview
**Release Date:** May 20, 2025

**Overview:**

This is the first public preview of ISEC-lite, the modular rewrite of Intext's core execution system (ISEC). It replaces the single-file interpreter model with a structured system that separates the boot, lexing, parsing, and execution stages.

**Limitations (Compared to Previous Builds):**

ISEC-lite does not support the following (yet):
- ``crunch()`` math function
- ``read()`` file-reading function
- Outputting mixed types (i.e., Spaghetti Output)

**Current Feature Set:**

- Basic variable declarations via declare

    - Supports all core types: ``int``, ``float``, ``bool``, ``char``, ``string``

    - Output of literals and simple variables using output

    - Primitive AST generation and token stream handled through the new modular architecture

    - Includes main.py to initialize ISEC-lite from a user-supplied Intext file

Notes:

- This release introduces the ISEC/ directory structure, preparing the system for scalability.

- RawAST is in early planning, not yet implemented at this stage.

- Example files and instructions are bundled with the release for demonstration purposes.

***

**Intextual File Lang – Version 0.6.1 Pre-Release**

**Title:** RawText Introduction: RawAST
**Status:** Pre-Release *to ISEC*
**Release Date:** May 26, 2025

**Overview:**

This release marks the introduction of RawAST, a new way to write Intext programs directly in raw Abstract Syntax Tree (AST) format. RawAST bypasses traditional parsing entirely, using the ``@RawAST`` directive in ``.itx`` files to interpret JSON-based code. It provides an early glimpse into what execution in a lower-level, high-precision format looks like for the language.

**What’s Included:**

- **Support for RawAST Mode**
    You can now write your Intext programs directly as JSON AST blocks, enabling faster execution by skipping lexing and parsing.

- **@RawAST Directive Support**
    Use ``@RawAST`` at the top of your ``.itx`` file to trigger RawAST evaluation.

- **Error Reporting**
    RawAST errors show a visual of where a semicolon node was forgot to be placed.

**Note:**
- This version serves as a lightweight fallback while the full ISEC system undergoes improvements. Users who want performance and don’t mind verbosity will find RawAST to be the first step toward a more robust execution layer.

***

**Intextual File Lang – Version 0.6.2 Pre-Release**

**Title:** Improving RawAST with Major Changes 
**Status:** Pre-Release *to ISEC*
**Release Date:** May 28, 2025

**Overview:**

This release improves RawAST by adding more programming concepts. Along with that, Standard Intext gets an improvement as well. Consider this release to be start of logic-building across all of Intext.

**What's Included:**

- **If Statements**
    You can now make If-Statements in RawAST. Not in Standard Intext though. However, it's very basic in logic.

- **Lists**
    Lists are now introduced in both Standard Intext and RawAST! However, they are called "orders", so lists are called "orders" in Intext.

- **Error-solving**
    More in-depth errors are now shown whenever you make a mistake. While they may be more exclusive to RawAST, Standard Intext users can benefit from this improvement as well.

***

**Intextual File Lang - Version 0.6.2.5 Pre-Release**

**Title:** Small Additions to a Big Picture
**Status:** Pre-Release *to ISEC*
**Release Date:** June 2, 2025

**Overview:**

This release just simple smashes some bugs, and fixes the most infamous one being indexing orders. Because, it'd be odd to have lists, but not be able to index them. 

**What's Included:**

- **Indexing Orders**
    This is the highlight of this release. You can now output or store these indexes into variables

***

**Intextual File Lang - Version 0.6.3 Pre-Release**

**Title:** Spaghetti & Crunch
**Status:** Pre-Release *to ISEC*
**Release:** June 16, 2025

**Overview:**

This release sharpens Intext's expressive power with the introduction of `crunch()`, allowing direct inline math and optional type casting. Output is now more dynamic than ever thanks to Spaghetti Output, enabling clean multi-type prints in a single call. File reading enters the picture with `read()`, and overall error-handling has been refined to make debugging smoother and more intuitive.

**What's Included:**

- **Spaghetti Output**
  Output now supports multiple mixed-type values in one line using `+` chaining.

- **crunch() Function**
  Perform math inside scripts. Supports `+`, `-`, `*`, and `/`. Also supports forced type casting to `string`, `bool`, or `char`.

- **read() Function**
  Lazily read the contents of a file. Can be stored in variables or used in simple output calls.

- **Improved Error Handling**
  More readable and consistent error messages, including cases like invalid crunch casts or missing files.

***