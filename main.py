# This program converts a flutter icon file into a typescript array
# Author: Ale, your dev
# Date: 27/04/2023
# Version: 1.0.1
# Description: The program reads the flutter icon file and extracts the names, codes and styles of the icons.
#     Then it creates a typescript array with the icon names as keys and objects as values. Each object contains
#     the code and the style of the icon. The style corresponds to the material icons class that is used to
#     create the icon in a typescript project. The array can be used to access the icons by their names and styles.
import sys

if len(sys.argv) < 2:
  print('Usage: python3 main.py <input_file>')
  quit()

input_file = sys.argv[1]

with open(input_file, 'r') as file:
  rows = file.readlines()

with open('array.ts', 'w') as output_file:
  output_file.write("export interface FlutterIcon {\n")
  output_file.write("  name: string;\n")
  output_file.write("  code: number;\n")
  output_file.write("  style: string;\n")
  output_file.write("}\n\n")

  output_file.write("export const icons: FlutterIcon[] = [\n")
  for row in rows:
    if 'static const IconData ' in row:
      iconName = row.split('tatic const IconData ')[1].split(' = IconData(')[0]
      iconCode = row.split(' = IconData(')[1].split(', fontFamily: \'MaterialIcons\'')[0]

      iconStyle = 'material-icons'
      # check the icon style
      if '_rounded' in iconName:
        iconStyle += '-round'
        iconName = iconName.replace('_rounded', '', 1)
      elif '_outlined' in iconName:
        iconStyle += '-outlined'
        iconName = iconName.replace('_outlined', '', 1)
      elif '_sharp' in iconName:
        iconStyle += '-sharp'
        iconName = iconName.replace('_sharp', '', 1)

      output_file.write('  { name: \'' + iconName + '\', code: ' + iconCode + ', style: \'' + iconStyle + '\' },\n')

  output_file.write("];\n")

print("Done! Output: array.ts")
