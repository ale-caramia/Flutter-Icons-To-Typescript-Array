# Flutter Icon Converter 🚀

This program converts a flutter icon file into a typescript array that can be used in an angular project. This is useful if you want to check the icons to set on a flutter app directly from an angular management site. You can save the hexadecimal codes of the icons you want to set in a database, and then use them in flutter like this: 
```IconData(iconCode, fontFamily: 'MaterialIcons')```

## How to use it 💻

To use this program, you need to have python3 installed on your machine. You also need to have a flutter icon file that contains the names and codes of the icons you want to convert. The file should look something like this:

```static const IconData phone_iphone_outlined = IconData(0xf28d, fontFamily: 'MaterialIcons');
/// comments or other code will be ignored
static const IconData phone_locked = IconData(0xe4ab, fontFamily: 'MaterialIcons');

static const IconData phone_locked_sharp = IconData(0xeba1, fontFamily: 'MaterialIcons');

...
```

To run the program, open a terminal and type:

```python3 main.py <input_file>```

where <input_file> is the name of your flutter icon file. The program will create a typescript array in the same directory as the input file, with the name **array.ts**. The array will look something like this:

```export const icons: FlutterIcon[] = [
  { name: 'ten_k', code: 0xe000, style: 'material-icons' },
  { name: 'ten_k', code: 0xe700, style: 'material-icons-sharp' },
  { name: 'ten_k', code: 0xf4df, style: 'material-icons-round' },
  ...
]
```

You can then use this array in your angular project to access the icons by their names and styles.

## License 📄

This program is free and open source. You can use it for any purpose, as long as you give credit to the author and respect the license terms.

## Author ✒️

This program was created by Ale, your dev. If you have any questions or suggestions, feel free to contact me at info@aleyour.dev.