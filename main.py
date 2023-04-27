import sys

if len(sys.argv) < 2:
  print('Usage: python main.py <input_file>')
  quit()

input_file = sys.argv[1]

with open(input_file, 'r') as file:
  rows = file.readlines()

with open('array.js', 'w') as output_file:
  output_file.write("export interface Customer {\n")
  output_file.write("  name: string;\n")
  output_file.write("  code: number;\n")
  output_file.write("}\n\n")

  output_file.write("const icons: FlutterIcon = [\n")
  for row in rows:
    if 'static const IconData ' in row:
      iconName = row.split('tatic const IconData ')[1].split(' = IconData(')[0]
      iconCode = row.split(' = IconData(')[1].split(', fontFamily: \'MaterialIcons\');')[0]

      output_file.write('  { name: \'' + iconName + '\', code:\'' + iconCode + '\' },\n')

  output_file.write("];\n")
