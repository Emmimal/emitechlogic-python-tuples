# emitechlogic-python-tuples
Hands-on code examples and demonstrations for Python tuples – companion to the full tutorial at https://emitechlogic.com/python-tuples/

# Python Tuples Examples

This repository contains practical, runnable code examples demonstrating key concepts from the excellent tutorial:

**[Python Tuples: Immutability as a Design Contract](https://emitechlogic.com/python-tuples/)**  
by Emmimal Alexander | Updated February 2026

The full article explains *why* tuples matter (not just how to use them). It covers immutability as a promise, performance benefits, real-world patterns, and common pitfalls.

This repo provides the code snippets from the article (and a few extras) organized into separate files for easy experimentation.

## Why Use This Repo?
- Run and modify examples locally.
- See differences between lists and tuples in action.
- Learn best practices with namedtuples, dictionary keys, and more.

## Quick Start
Clone the repo and run any `.py` file:
```bash
git clone https://github.com/yourusername/python-tuples-examples.git
cd python-tuples-examples
python examples/memory_comparison.py

## Examples Included

 ## 1. Memory and Performance Benefits
See how tuples use less memory than lists.
File: examples/memory_comparison.py

 ## 2. Tuples as Dictionary Keys
Why lists fail as dict keys but tuples work perfectly.
File: examples/dict_keys.py

 ## 3. The "Immutable Container Trap"
Tuples are immutable... but contents might not be!
File: examples/mutable_content.py

 ## 4. Tuples as Data Records
Using position to represent fixed meaning (coordinates, colors, etc.).
File: examples/data_records.py

 ## 5. Named Tuples for Clarity
Make tuples self-documenting.
File: examples/namedtuples.py

 ## 6. Functions and Intent
Using tuples in parameters and return values to signal stability.
File: examples/function_patterns.py

 ## 7. Common Mistakes
See inefficient patterns and better alternatives.
File: examples/common_mistakes.py

Run All Examples at Once
Use the script run_all_examples.py to execute everything.

Read the complete tutorial here: https://emitechlogic.com/python-tuples/

