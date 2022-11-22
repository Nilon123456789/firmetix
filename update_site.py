from firmetix import firmetix
import pdoc

print("Updating documentation...")

# Generate HTML documentation
html = open('docs/firmetix.html', 'w')
html.write(pdoc.html(firmetix))
html.close()
print("Generated HTML documentation")

# Copy the readme file to the documentation folder
original_readme = open('README.md', 'r')
readme = open('docs/README.md', 'w')

line_found = False
for line in original_readme:
    if line.startswith('<!-- HTML Begin -->'):
        line_found = True
    if line_found:
        readme.write(line)    

readme.close()
original_readme.close()
print("Copied README.md")