import re
import os

# Items to remove from Pages dropdown
items_to_remove = [
    # 404 Error
    r'<li>\s*<a href="404\.html">404 Error</a>\s*</li>',
    # Coming Soon Page
    r'<li>\s*<a href="coming-soon\.html">Coming Soon Page</a>\s*</li>',
    # Case Study Grid View
    r'<li>\s*<a href="case-1\.html">Case Study \(Grid View\)</a>\s*</li>',
    # Case Study List View
    r'<li>\s*<a href="case-2\.html">Case Study \(List View\)</a>\s*</li>',
    # Case Details
    r'<li>\s*<a href="case-details\.html">Case Details</a>\s*</li>',
]

# Get list of HTML files
html_files = [f for f in os.listdir('.') if f.endswith('.html')]
print("Removing navigation items from {} HTML files...\n".format(len(html_files)))

updated_count = 0
failed_count = 0

for filename in sorted(html_files):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Remove each item
        for pattern in items_to_remove:
            content = re.sub(pattern, '', content, flags=re.DOTALL)
        
        # Clean up any double newlines left behind
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        
        if content != original_content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            updated_count += 1
            print("✓ {}".format(filename))
        else:
            print("- {} (no changes)".format(filename))
    except Exception as e:
        failed_count += 1
        print("✗ {} (error: {})".format(filename, e))

print("\n--- Summary ---")
print("Updated: {}".format(updated_count))
print("Failed: {}".format(failed_count))
