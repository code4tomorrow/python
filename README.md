# Python
Source code from Code For Tomorrow's Python course

## Difficulty Level
Source code is organized under 3 difficulty levels:
1. `1_beginner`
2. `2_intermediate`
3. `3_advanced`

## Chapters
Under each of the 3 packages, source code is further divided by chapter.
### Beginner
1. `chapter1` Intro to Python
2. `chapter2` Data
3. `chapter3` Operators
4. `chapter4` Conditionals
5. `chapter5` Loops
6. `chapter6` Lists
7. `chapter7` String Manipulation

### Intermediate
8. `chapter8` Libraries
9. `chapter9` Dictionaries
10. `chapter10` 2D Lists
11. `chapter11` Functions
12. `chapter12` Classes

### Advanced
13. `chapter13` Special Methods
14. `chapter14` Selection Sort
15. `chapter15` Tuples & Sets
16. `chapter16` Pythonness
17. `chapter17` Exception Handling
18. `chapter18` Recursion
19. `chapter19` Asymptotic Analysis
20. `chapter20` File I/O

## Category
Under each chapter, source code is further divided by category:
1. `examples` - example code to demo certain programming concepts
2. `practice` - practice exercise templates for students to write code
3. `solutions` - solutions to practice exercises

The practice template file has the same name as the corresponding solution file.

# Practice Problem Guidelines
Please follow the following guidelines when creating or finding practice problems. We expect all problems submitted by teachers to maintain the highest quality! (You can also read these guidelines on every repository’s README.md.)

If you have questions, send a message to #questions on the teachers Discord.

## Follow good programming style.
### Install Linters
This will save you time because when you submit a pull request (PR) on GitHub, we check for good programming style. Your PR will not be approved unless it passes those style checks. Also, linters basically enforce all of the style rules that we discuss below, so you basically can just skip to the next section (Follow the C4T practice and solution problem format).

* Java: Install checkstyle (SonarLint recommended as well)
* Python: Install flake8 (pylint recommended as well)
* HTML/CSS: Install SonarLint (recommended)

This should go without saying, but actually use the linters! If you see errors/problems/warnings, address them, don’t ignore them and keep going!

**Note:** We highly recommend that you use [Visual Studio Code](https://code.visualstudio.com/download), because it has a lot of useful extensions you can install with a few clicks (including the linters mentioned above). It also has great Version Control System (VCS) integration and extensions.

### Whitespace
* Indent properly.
* Make sure there are spaces between binary operators, parentheses, curly braces, etc. when applicable. (For method/function calls, there should not be a space between the method/function name and the parentheses.)
  * For HTML, attributes should not have spaces between the attribute name, equal sign, and attribute value
* Leave empty lines where appropriate to increase readability

### Naming
* Name files so that they are representative of what the program is about. File names are also the name of the practice problem.
  * Avoid naming files after concepts, like “Arrays.java”
  * Java: Use class naming conventions to name files. For example, HelloWorld.java rather than helloWorld.java or hello_world.java or something else
  * Python: Use snake case to name files. For example, hello_world.py rather than HelloWorld.py or helloWorld.py or something else
* Name variables/methods/functions descriptively, and follow your language’s conventions.
 * Java: camelCase for regular variables, snake case (and uppercase) for constants
 * Python: Snake case for regular variables, snake case (and uppercase) for constants

### Reduce complexity
* If a line of code is very long, separate it into 2+ lines (e.g. for long lists/arrays, long print statements, etc.)
* Add comments to explain parts of your code
* Break up the program into methods/functions if applicable and if the students have learned about methods/functions at that point in time.

## Follow the C4T practice and solution problem format.
* Make sure you put the file(s) in the right directories.
  * All code filed under “practice” should be templates.
    * Templates may include things like an empty class and main method.
    * They must include a multi-line comment with the title of the practice problem AND the full instructions for the problem.
  * All code filed under “solutions” should be solutions.
    * Solutions should include the practice problem title AND full instructions at the top of the file (exact same comment as in the practice template file) and then a (possible) solution to the problem.
* The practice template and solution should have the same file name.
* Java: Make sure that you have the correct package statement as the first line of your code.

## Testing
* Thoroughly test your solution. Make sure it works as intended.
  * Try to break your program! Don’t just give input you know will work.
* Hundreds of students and ~50 teachers could potentially see and use your work. Please make sure that it works!

## Check the content.
* Make sure that the problem is doable for the skill level of your students.
* Check Thinkific to see if the concepts that you need to solve the problem have been covered already.
* Be aware of how long your own class takes on other practice problems.
* Practice problems shouldn’t take several hours/days.

## Cite your sources.
* If you are using data or practice problems from somewhere other than yourself, you MUST cite your sources. 
* Providing a link to the original is usually sufficient if you found the problem online. 
* If you found it in a book, cite the full title and author.

## Submit practice problem(s).

### Option 1: Use GitHub
***Note 1:** If you choose option 1, we assume you know basic Git, e.g. committing, pushing, pulling, branching, merging, etc. If you want to learn the basic Git you need to contribute, we recommend watching [this entire playlist.](https://www.youtube.com/watch?v=3RjQznt-8kE&list=PL4cUxeGkcC9goXbgTDQ0n_4TBzOO0ocPR&index=1)*

***Note 2:** If you want an overview of the Pull Request (PR) workflow we are using, read these articles.*

1. Send your GitHub username to a Curriculum Development member and ask them to add you as an outside collaborator on the repository or repositories that you want to contribute to.
2. Clone or fork the official C4T repository.
  * All repositories can be found here: https://github.com/code-for-tomorrow 
  * [How to Clone](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
  * [How to Fork](https://help.github.com/en/github/getting-started-with-github/fork-a-repo)
3. Work on the practice problems locally.
  * If you cloned the repo, make sure you create and checkout a new branch. **DO NOT MAKE EDITS ON THE MASTER BRANCH.**
  * If you forked the repo, you’re free to work on the master branch or make your own branches (though that is kinda unnecessary).
  * [Git Branches Tutorial](https://www.atlassian.com/git/tutorials/using-branches)
4. Push your local branch to remote.
  * [How to Push](https://help.github.com/en/github/using-git/pushing-commits-to-a-remote-repository)
5. Make a pull request to merge your branch with the master branch of the official C4T repo.
  * Make sure that the title of your pull request is descriptive but concise.
  * In the description part of your pull request, you should specify the following:
    * Your full name (if it’s not clear from your GitHub profile)
    * Chapter # and section name that this problem should go under (for example, Ch. 1 Intro to Python, Section: Comments)
  * [How to Create a Pull Request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)
6. Mention @Curriculum Development on the Teachers Discord that you’ve submitted a PR.
7. Monitor the status of your Pull Request on GitHub. 
  * It’s possible that the Curriculum Development team will Request Changes, in which case you will need to commit those changes before your PR will be approved and merged into the official master branch.

### Option 2: Use the Google Form
Submit a problem [here](https://forms.gle/hDWrPRG3HuAgUdCJ9) if you don’t have a GitHub account.


**Thank you teachers for following these guidelines and helping us build a problem base!**
