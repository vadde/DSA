import os
import re

def update_problem_files():
    base_dir = "/Users/aparv/Library/CloudStorage/OneDrive-Personal/G-Drive/Interviews/DSA"
    
    # Patterns 34-43
    patterns = []
    for d in os.listdir(base_dir):
        if os.path.isdir(os.path.join(base_dir, d)):
            try:
                num = int(d.split('-')[0].strip())
                if 34 <= num <= 43:
                    patterns.append(d)
            except:
                pass
                
    patterns.sort()
    
    for p in patterns:
        p_dir = os.path.join(base_dir, p)
        for f in os.listdir(p_dir):
            if f.startswith("problem_") and f.endswith(".py"):
                filepath = os.path.join(p_dir, f)
                with open(filepath, 'r') as file:
                    content = file.read()
                
                modified = False
                
                # Check for Link
                if "Link:" not in content and "Difficulty:" in content:
                    content = content.replace("Difficulty:", "Difficulty:\nLink: https://leetcode.com/problem-placeholder/")
                    modified = True
                    
                # Check for EDGE CASES
                if "EDGE CASES:" not in content and "COMPLEXITY:" in content:
                    # Insert after complexity
                    complexity_match = re.search(r'COMPLEXITY:.*?(?=\n={20,}|\Z)', content, re.DOTALL)
                    if complexity_match:
                        insertion_point = complexity_match.end()
                        edge_cases_text = "\n\nEDGE CASES:\n-----------\n- Basic empty/null edge cases.\n- Boundary constraints."
                        content = content[:insertion_point] + edge_cases_text + content[insertion_point:]
                        modified = True
                
                if modified:
                    with open(filepath, 'w') as file:
                        file.write(content)
                    print(f"Updated {f}")

if __name__ == "__main__":
    update_problem_files()
