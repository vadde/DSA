"""
============================================================
Problem: Simplify Path
Pattern: Stacks
Difficulty: Medium
Link: https://leetcode.com/problems/simplify-path/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
Imagine you are exploring folders on a computer. 
You start at the very beginning (the root `/`).
The path you are given is like a map with some weird, messy instructions:
- `/a/` means "go into folder 'a'".
- `.` means "stay in the current folder".
- `..` means "go BACK out of this folder to the previous one".
- `//` means nothing special, it's just a typo, treat it like a single `/`.
You want to read this messy map and draw a clean, simple map that gets you to 
the exact same final folder without any backtracking or typos.
Since `..` means "undo my last move", this is the perfect job for a Stack!
Every time you go into a folder, you push it onto the stack.
Every time you see `..`, you pop the top folder off the stack (undoing your last move).
If you see `.` or empty spaces from typos, you just ignore them!

APPROACH:
---------
1. Initialize an empty stack `stack = []`.
2. Split the input path by `/`. This breaks it into parts. 
   (e.g. `"/a//b/./../c/"` becomes `['', 'a', '', 'b', '.', '..', 'c', '']`).
3. Loop through each `part` in the parts:
   - If `part == '..'`: We need to go back! `pop()` from the stack IF the stack is not empty.
   - If `part == '.'` or `part == ''`: Just ignore it.
   - Else: It's a real folder name! Push it to the stack.
4. After the loop, the stack contains the exact folders you need to enter.
5. Join them with `/` and add a leading `/`.
   Return `'/' + '/'.join(stack)`.

COMPLEXITY:
-----------
Time:  O(N) — We split the string once and iterate through the parts.
Space: O(N) — The stack can store up to N parts if the path is very deep.

EDGE CASES:
-----------
- Edge case 1: `"/../"` trying to go up from root. Stack is empty, so we safely ignore it. Result is `"/"`.
- Edge case 2: Multiple slashes `"/a//b"`. The split makes empty strings, which we ignore.
============================================================
"""

def simplify_path(path: str) -> str:
    """
    Simplifies an absolute Unix-style file path.
    """
    stack: list[str] = []
    
    # 1. Split the path by the directory separator
    parts = path.split('/')

    for part in parts:
        if part == '..':
            # Go back one directory if possible
            if stack:
                stack.pop()
        elif part == '.' or part == '':
            # Stay in current directory / ignore multiple slashes
            continue
        else:
            # Go into the directory
            stack.append(part)

    # Reconstruct the absolute path
    return '/' + '/'.join(stack)

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert simplify_path("/a/./b/../../c/") == "/c", "Test 1 failed"
    assert simplify_path("/home/") == "/home", "Test 2 failed"
    assert simplify_path("/a//b/c") == "/a/b/c", "Test 3 failed"

    # 🔲 Edge cases
    assert simplify_path("/../") == "/", "Edge 1: Trying to go above root"
    assert simplify_path("/...") == "/...", "Edge 2: '...' is a valid directory name, not '..'"

    print("All tests passed!")
