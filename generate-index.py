import os
from glob import glob

#files = [y for x in os.walk('.') for y in glob(os.path.join(x[0], '*.whl'))]
# TODO add links to subdirectories as well
files = sorted([x for x in glob('*.whl')], key=str.lower)


f = open('index.html', 'w')

# write the header
f.write('<!DOCTYPE html>\n')
f.write('<html>\n')
f.write('  <body>\n')
f.write('\n')


# Loop through the files
for filepath in files:
    f.write('    <a href="{0}">{0}</a></br>\n'.format(filepath))


# write the footer
f.write('\n')
f.write('  </body>\n')
f.write('</html>\n')
