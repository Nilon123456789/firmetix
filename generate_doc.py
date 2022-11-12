from firmetix import firmetix
import pdoc

# Generate HTML documentation
html = open('html/firmetix/index.html', 'w')
html.write(pdoc.html(firmetix))
html.close()

