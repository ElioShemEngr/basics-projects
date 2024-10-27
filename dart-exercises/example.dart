main(){
  // Null Variable
  var num;
  print(num);
  
  // Number Type in Strings
  var age = 32;
  var str = 'My age is: $age';
  print(str);
  print('');

  // Multiline text
  var s1 = '''
This is a text
multi-line strings
like this one
''';

  var s2 = """This is also a
multi-line string""";

  print(s1);
  print(s2);
  print('');

  // Convert data types
  //str -> int
  var one = int.parse('1');
  assert(one == 1);
  print(one.runtimeType);

  //str -> double
  var onePointOne = double.parse('1.1');
  assert(onePointOne == 1.1);
  print(onePointOne.runtimeType);

  //int -> str
  String oneAsString = 1.toString();
  assert(oneAsString == '1');
  print(oneAsString.runtimeType);

  //double -> str
  String piAsString = 3.14159.toStringAsFixed(2);
  assert(piAsString == '1.14');
  print(piAsString.runtimeType);

  print('');

  // Constans
  const aConstNum = 3; // int Constant
  const aConstBool = true; // bool constant
  const aConstString = 'a constant String'; // String Constant

  print(aConstNum);
  print(aConstBool);
  print(aConstString);

  print('');

  print(aConstNum.runtimeType);
  print(aConstBool.runtimeType);
  print(aConstString.runtimeType);

}