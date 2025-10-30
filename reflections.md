1. Which issues were the easiest to fix, and which were the hardest? Why?
The easy ones were mostly formatting issues like fixing long lines and removing extra spaces — those just needed small edits. The harder part was dealing with the global variable warning. That required changing how some parts of the code worked to avoid using globals, which took a bit more thought and testing to make sure nothing broke.

2. Did the static analysis tools report any false positives? If so, describe one example.
There weren’t any serious false positives, but Pylint did flag some indentation and style issues even though the code ran fine. These didn’t affect functionality, but I still fixed them to keep the style consistent and get a perfect score.

3. How would you integrate static analysis tools into your actual software development workflow?
I’d set up tools like Pylint, Flake8, and Bandit to run automatically in a CI pipeline — for example, every time I push code to GitHub. I’d also add pre-commit hooks so that code gets checked before it’s even committed. This way, the code stays clean and secure without needing manual checks every time.

4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
After cleaning up the code, everything looks much neater and easier to follow. The indentation and line lengths are consistent, so it’s more readable. Removing global variables made the code feel more modular and less error-prone. Overall, it just feels more professional and reliable — plus, Bandit confirming zero security issues was a good sign.