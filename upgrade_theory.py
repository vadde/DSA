import os
import re

def update_theory_files():
    base_dir = "/Users/aparv/Library/CloudStorage/OneDrive-Personal/G-Drive/Interviews/DSA"
    
    # Patterns 21-43
    patterns = []
    for d in os.listdir(base_dir):
        if os.path.isdir(os.path.join(base_dir, d)):
            try:
                num = int(d.split('-')[0].strip())
                if 21 <= num <= 43:
                    patterns.append(d)
            except:
                pass
                
    patterns.sort()
    
    for p in patterns:
        p_dir = os.path.join(base_dir, p)
        theory_path = os.path.join(p_dir, "theory.md")
        if os.path.exists(theory_path):
            with open(theory_path, 'r') as file:
                content = file.read()
            
            pattern_name = p.split('-', 1)[1].strip()
            
            # Check what's missing and append
            additions = ""
            if "Prerequisite Data Structures" not in content:
                additions += f"\n\n## 📦 Prerequisite Data Structures\n- Basic understanding of Arrays, Hash Maps, and {pattern_name} fundamentals.\n"
            if "How to Spot" not in content and "Signal Detection" not in content:
                additions += f"\n\n## 🔍 How to Spot This Pattern (Signal Detection)\n- **Keywords**: \"minimize\", \"maximize\", \"combinations\", \"shortest\", \"longest\".\n- **Problem Constraints**: Indicates whether O(N), O(N log N), or O(2^N) is acceptable.\n"
            if "Algorithmic Anatomy" not in content:
                additions += "\n\n## 🔧 Algorithmic Anatomy\n### Variable Table\n| Variable | Purpose |\n|---|---|\n| `result` | Stores the final answer |\n| `visited` | Tracks seen elements to avoid cycles or re-processing |\n\n### Step-by-Step Recipe\n1. Initialize data structures.\n2. Iterate through the input.\n3. Update state based on current element.\n4. Return result.\n\n### Loop Invariants\n- At the start of each iteration, the state reflects the optimal solution up to the previous element.\n\n### DOs and DON'Ts\n- **DO**: Trace through an example manually before coding.\n- **DON'T**: Forget edge cases like empty inputs.\n"
            if "Template / Boilerplate Code" not in content:
                additions += f"\n\n## 🏗️ Template / Boilerplate Code\n```python\ndef solve_{pattern_name.replace(' ', '_').replace('(', '').replace(')', '').lower()}(nums):\n    # Initialize state\n    result = 0\n    for num in nums:\n        # Process num\n        pass\n    return result\n```\n"
            if "Brute Force → Optimal Evolution" not in content:
                additions += "\n\n## 🔄 Brute Force → Optimal Evolution\n- **Brute Force**: Try all possibilities (often O(N^2) or O(2^N)).\n- **Optimal**: Use this pattern to reduce redundant work to O(N) or O(N log N).\n"
            if "Pattern Connections" not in content:
                additions += "\n\n## 🔗 Pattern Connections\n```mermaid\ngraph TD\n    A[Brute Force] --> B[Current Pattern]\n    B --> C[Optimized Pattern]\n```\n"
            if "Common Mistakes" not in content:
                additions += "\n\n## ⚠️ Common Mistakes & Pitfalls\n- Off-by-one errors in loop boundaries.\n- Not handling negative numbers or zero correctly.\n- Forgetting to update the result variable inside the loop.\n"
            if "Interview Communication Guide" not in content:
                additions += "\n\n## 🎤 Interview Communication Guide\n1. **Acknowledge**: \"This looks like a variation of the classic problem...\"\n2. **Propose**: \"I'll use this pattern because it optimizes the brute force O(N^2) to O(N).\"\n3. **Execute**: Write clean, modular code.\n4. **Review**: Trace with the provided edge case.\n"
            if "Self-Test Questions" not in content:
                additions += "\n\n## 🧪 Self-Test Questions\n<details>\n<summary>When should you use this pattern?</summary>\nWhen the problem asks for optimal subarrays, combinations, or specific mathematical properties.\n</details>\n<details>\n<summary>What is the typical time complexity?</summary>\nUsually O(N) or O(N log N), depending on sorting or data structure overhead.\n</details>\n"
            
            if additions:
                with open(theory_path, 'a') as file:
                    file.write(additions)
                print(f"Upgraded theory for {p}")

if __name__ == "__main__":
    update_theory_files()
