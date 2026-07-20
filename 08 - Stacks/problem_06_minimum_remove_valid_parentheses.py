"""
============================================================
Problem: Minimum Remove to Make Valid Parentheses
Pattern: Stacks
Difficulty: Medium
Link: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
============================================================

UNDERSTANDING THE PROBLEM (Explain Like I'm 5):
-------------------------------------------------
You have a sentence that has some parentheses in it, like `a)b(c)d`.
But oh no! The parentheses are messed up. There is a closing parenthesis `)` 
right after `a` that never had an opening parenthesis before it.
We want to fix the sentence by erasing the MINIMUM number of parentheses 
possible. We never erase the letters.
If we use our Stack trick, it's really easy to find the bad parentheses!
Every time we see an opening `(`, we put its **index** (its location in the word) 
onto our Stack.
When we see a closing `)`, we try to pop from the Stack. 
If the Stack is empty, it means this `)` is an extra, invalid parenthesis! We 
write down its index on our "erase list".
If we finish reading the whole sentence, and there are still numbers left in 
our Stack, that means we had some `(` that we never closed! Those are invalid 
too, so we add them to our "erase list".
Finally, we just rewrite the sentence, skipping any index that is on our erase list!

APPROACH:
---------
1. Initialize a `stack` to store indices of `(`.
2. Initialize an `invalid_indices` set.
3. Loop through the string with `enumerate(s)` to get both index `i` and `char`:
   - If `char == '('`: Push `i` to `stack`.
   - If `char == ')'`:
     - If stack is empty: This is invalid. Add `i` to `invalid_indices`.
     - Else: Pop from stack (we successfully matched it).
4. After the loop, anything left in the `stack` is an unmatched `(`.
   - Add all remaining items in `stack` to `invalid_indices`.
5. Build the result string:
   - Loop through `s` again.
   - If `i` is NOT in `invalid_indices`, append `char` to our result list.
6. Return the joined result list.

COMPLEXITY:
-----------
Time:  O(N) — One pass to find invalid indices, one pass to build the string.
Space: O(N) — Stack, set, and result list can all store up to N elements.

EDGE CASES:
-----------
- Edge case 1: String has no parentheses. Returns string unchanged.
- Edge case 2: String is completely invalid `)))(((`. Returns empty string (if no letters) or just the letters.
============================================================
"""

def min_remove_to_make_valid(s: str) -> str:
    """
    Removes the minimum number of invalid parentheses to make a string valid.
    """
    stack: list[int] = []
    invalid_indices: set[int] = set()

    # 1. Identify all invalid parentheses
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                invalid_indices.add(i)

    # 2. Any unmatched opening parentheses left in the stack are also invalid
    for index in stack:
        invalid_indices.add(index)

    # 3. Build the final string without the invalid characters
    result: list[str] = []
    for i, char in enumerate(s):
        if i not in invalid_indices:
            result.append(char)

    return "".join(result)

# ─────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────
if __name__ == "__main__":
    # ✅ Normal cases
    assert min_remove_to_make_valid("lee(t(c)o)de)") == "lee(t(c)o)de", "Test 1 failed"
    assert min_remove_to_make_valid("a)b(c)d") == "ab(c)d", "Test 2 failed"
    assert min_remove_to_make_valid("))((") == "", "Test 3 failed"

    # 🔲 Edge cases
    assert min_remove_to_make_valid("hello") == "hello", "Edge 1: No parentheses"
    assert min_remove_to_make_valid("(a(b)c)d)") == "(a(b)c)d", "Edge 2: Nested valid with extra closing"

    print("All tests passed!")
