"""The calculator's application package.

``__init__.py`` identifies this directory as a regular Python package. Python
executes it on the first import of ``app`` in a process, including imports such
as ``from app.operations import add``. Keep package initialization lightweight:
importing arithmetic for a test must not start an interactive input loop.

The demo below is an introductory import exercise, not part of the calculator's
execution path. Try ``from app import demo`` followed by ``demo()`` in Python.

═══════════════════════════════════════════════════════════════════════════════
🤖 MENTOR COMMENTARY: Packages, Namespacing, and Why It Matters
═══════════════════════════════════════════════════════════════════════════════

Let's talk about one of the most fundamental concepts in professional
programming: NAMESPACING. You'll see this pattern in every language.

1. **WHAT __init__.py DOES (Python-Specific)**
   
   Without __init__.py:
   ```
   app/
   ├── operations.py
   └── cli.py
   ```
   This is just a folder with Python files. Python won't know it's a package.
   
   With __init__.py:
   ```
   app/
   ├── __init__.py     ← This file marks it as a package
   ├── operations.py
   └── cli.py
   ```
   Now you can do:
   ```python
   from app import operations
   from app.operations import add
   from app.cli import Calculator
   ```
   
   That's the ENTIRE purpose of __init__.py. It says: "This folder is a
   coherent unit of code, not random Python files."
   
   Side note: Python 3.3+ has "namespace packages" that work without __init__.py,
   but having it is clearer and works everywhere. Use it.

2. **NAMESPACING: THE UNIVERSAL PATTERN**
   
   This concept exists in every programming language:
   
   JavaScript:
   ```javascript
   // Namespace via objects
   const calculator = {
       add: (a, b) => a + b,
       subtract: (a, b) => a - b
   };
   calculator.add(5, 3); // Avoid global pollution
   ```
   
   Java:
   ```java
   // Namespace via packages
   package com.mycompany.calculator;
   public class Operations {
       public static int add(int a, int b) { return a + b; }
   }
   // Call as: com.mycompany.calculator.Operations.add(5, 3)
   ```
   
   C#:
   ```csharp
   // Namespace via namespaces (obviously)
   namespace MyCompany.Calculator {
       public class Operations {
           public static int Add(int a, int b) { return a + b; }
       }
   }
   // Call as: MyCompany.Calculator.Operations.Add(5, 3)
   ```
   
   C:
   ```c
   // Namespace via naming conventions
   int calculator_add(int a, int b) { return a + b; }
   int calculator_subtract(int a, int b) { return a - b; }
   // C has no namespaces, so use prefixes
   ```
   
   Python:
   ```python
   # Namespace via packages/modules
   from app.operations import add
   add(5, 3)
   ```
   
   **THE PATTERN:** Organize code into logical containers so:
   - Related functions live together
   - Name collisions are prevented
   - Code is easy to find and reuse
   - Team members understand the structure

3. **WHY NAMESPACING MATTERS (Real-World Consequences)**
   
   Imagine two engineers both create a `format_date()` function:
   
   BAD (no namespace):
   ```python
   # engineer1.py
   def format_date(d):
       return d.strftime("%Y-%m-%d")
   
   # engineer2.py
   def format_date(d):
       return d.strftime("%d/%m/%Y")
   
   # main.py
   from engineer1 import format_date  # Which one? Confusion!
   ```
   
   GOOD (with namespacing):
   ```python
   from engineer1.utils import format_date as format_iso
   from engineer2.utils import format_date as format_eu
   
   date1 = format_iso(today)  # Engineer1's version
   date2 = format_eu(today)   # Engineer2's version
   # Both work, no collision, intent is clear
   ```
   
   This scales: thousand-person companies have hundreds of packages.
   Without namespacing, it would be chaos.

4. **KEEP __init__.py LIGHTWEIGHT (Crucial Rule)**
   
   Notice our __init__.py doesn't do much. It just defines demo().
   
   If we did this:
   ```python
   # BAD - don't do this
   from app.operations import add, subtract, multiply, divide
   from app.cli import Calculator
   
   # Now these are all loaded when anyone imports app
   ```
   
   Problem: When running tests that import app.operations, Python would also
   load app.cli, which would start the REPL loop. Tests would hang. Classic
   mistake.
   
   Rule: __init__.py should do minimal work. It's an entry point, not a
   place to load everything.

5. **MODULE-LEVEL IMPORTS (What You See at the Top)**
   
   At the top of app/cli.py:
   ```python
   from app.operations import (
       add, subtract, multiply, divide, modulo, power, square_root
   )
   ```
   
   We explicitly list what we use. This is intentional:
   - Readers see exactly what dependencies exist
   - IDE tools can track usage
   - Linters can catch unused imports
   - Circular imports are obvious and caught early
   
   Contrast with:
   ```python
   # Implicit/bad
   from app.operations import *  # Import everything
   # Now where did 'add' come from? Unknown.
   ```
   
   The explicit approach scales to large teams. Nobody wastes time hunting
   for where something was defined.

═══════════════════════════════════════════════════════════════════════════════
🤖 MENTOR COMMENTARY: Dependency Management with pip freeze
═══════════════════════════════════════════════════════════════════════════════

Now let's talk about requirements.txt and `pip freeze`. This is where
many junior engineers get confused, but it's simple once you understand
the principle.

1. **THE PROBLEM: "It Works On My Machine"**
   
   You write code using pytest version 8.4.2. Your teammate runs it and gets
   pytest version 9.0.0, which has breaking changes. Their tests fail.
   
   Senior engineer: "What version of pytest are you using?"
   Junior: "I dunno, just pip installed it."
   
   This happens thousands of times a day in professional software.
   
   The fix: LOCK YOUR DEPENDENCIES.
   
2. **REQUIREMENTS.txt (The Lock File)**
   
   Our requirements.txt:
   ```
   exceptiongroup==1.3.1
   iniconfig==2.1.0
   packaging==26.3
   pluggy==1.6.0
   pytest==8.4.2
   ...
   ```
   
   Each line says: "This exact version, nothing newer, nothing older."
   
   When you clone this repo and run:
   ```bash
   pip install -r requirements.txt
   ```
   
   You get EXACTLY the same versions as the original author. No surprises.

3. **HOW IT'S CREATED: `pip freeze`**
   
   When we ran:
   ```bash
   pip freeze > requirements.txt
   ```
   
   pip listed every installed package and its version:
   
   ```
   exceptiongroup==1.3.1
   iniconfig==2.1.0
   packaging==26.3
   ...
   ```
   
   This is a "snapshot" of the environment at a specific moment.
   
   Real-world use:
   - Dev environment: pip freeze > requirements.txt
   - Commit to git with the code
   - CI/CD pipeline: pip install -r requirements.txt (reproducible build)
   - Production: pip install -r requirements.txt (same versions)
   - Teammate: pip install -r requirements.txt (same versions)
   
   Everyone gets the same environment. Bugs are reproducible.

4. **TRANSITIVE DEPENDENCIES (The Invisible Tree)**
   
   We only asked for pytest:
   ```python
   pip install pytest
   ```
   
   But pytest itself needs:
   - pluggy (for plugin system)
   - packaging (for version parsing)
   - iniconfig (for .ini file parsing)
   
   These are "transitive dependencies"—dependencies of our dependencies.
   
   When we `pip freeze`, it captures ALL of them:
   ```
   pytest==8.4.2
   pluggy==1.6.0       ← pytest needs this
   packaging==26.3     ← pytest needs this
   iniconfig==2.1.0    ← pytest needs this
   ```
   
   If we only specified pytest==8.4.2 and someone installed pytest==9.0.0
   later, they might get different plugin versions, causing bugs.
   
   By freezing the ENTIRE tree, we eliminate this source of variation.

5. **SEMANTIC VERSIONING (What The Numbers Mean)**
   
   pytest==8.4.2 means:
   - 8 = MAJOR version (breaking changes)
   - 4 = MINOR version (new features, backward compatible)
   - 2 = PATCH version (bug fixes)
   
   In professional dev:
   - 8.4.2 → 8.4.3: Safe, just bug fixes
   - 8.4.2 → 8.5.0: Probably safe (new features, backward compatible)
   - 8.4.2 → 9.0.0: DANGER (breaking changes)
   
   requirements.txt locks all three. Nobody accidentally upgrades.
   
   Contrast with loose specifications:
   ```
   # Loose - bad for production
   pytest>=8.0.0      # Could install 9.0.0 with breaking changes
   pytest~=8.4        # Could install 8.5.0 (usually safe)
   pytest==8.4.2      # EXACTLY 8.4.2 (locked)
   ```
   
   For production: use ==. For development: use >= and test thoroughly.

6. **THE REAL-WORLD SCENARIO**
   
   You deploy a banking app Friday at 5 PM.
   
   BAD (no lock file):
   ```
   pip install flask requests numpy
   # Six months later, new dev installs
   pip install flask requests numpy
   # Gets different versions
   # Subtle bugs appear that you can't reproduce
   ```
   
   GOOD (lock file):
   ```
   # requirements.txt specifies exact versions
   pip install -r requirements.txt
   # Six months later, new dev installs
   pip install -r requirements.txt
   # Gets EXACTLY the same versions
   # Can reproduce every bug from production
   ```
   
   This is why requirements.txt exists. It's not optional in professional work.

═══════════════════════════════════════════════════════════════════════════════
⚡ UNIVERSAL PROGRAMMING CONCEPTS

These ideas transcend Python:

**Namespacing:**
- Java: packages (com.company.module)
- C#: namespaces (MyCompany.Module)
- Go: packages (github.com/user/package)
- Rust: modules (mod mymodule)

Every language solves the same problem: organize code so millions of lines
don't collide.

**Dependency Locking:**
- npm (JavaScript): package-lock.json
- Cargo (Rust): Cargo.lock
- Maven (Java): versions in pom.xml + local .m2 cache
- Go: go.sum

Every language learned (often the hard way) that reproducible builds require
locked dependencies. Early languages didn't have this. They had nightmares.

**Explicit Imports:**
- Most languages: explicit imports/includes
- Python: "from X import Y"
- Java: "import com.company.package"
- C: #include "header.h"

The principle: Be explicit. Make dependencies visible. This is how large
teams coordinate without stepping on each other.

═══════════════════════════════════════════════════════════════════════════════
⚡ WHAT THIS MEANS FOR YOUR CAREER

Right now you're learning:
1. Organize code into packages (namespacing)
2. Manage dependencies explicitly (requirements.txt)
3. Make everything reproducible (pip freeze)
4. Write code other people can run (same versions)

These are TABLE STAKES for professional software engineers. Companies that
don't do this have chaos. Companies that do this ship reliable software.

In your first real job:
- Day 1: "Clone the repo and run pip install -r requirements.txt"
- You'll see requirements.txt in EVERY project
- The pattern is identical across every tech stack
- Your ability to understand this matters


═══════════════════════════════════════════════════════════════════════════════
"""


def demo():
    """Print a package-import demonstration; return None implicitly.

    Defining a function does not execute its body. Printing happens only when
    someone calls ``demo()``. Compare this with operations.add, which returns a
    value for its caller to use instead of printing it.
    """
    print("This is a demo function from the app package.")
