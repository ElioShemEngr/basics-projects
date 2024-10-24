// Exercise 04
// Create a basic calculator that receives the user's numbers and can perform operations such as: addition, subtraction, multiplication and division

import 'dart:io';

main() {
  print('Basic Calculator');
  print('');

  // Input Numbers and type operation
  stdout.writeln('Enter first number : ');
  num firstNumber = num.parse(stdin.readLineSync()!);

  stdout.writeln('Enter second number : ');
  num secondNumber = num.parse(stdin.readLineSync()!);

  print('Enter Operation');
  stdout.writeln('Addition(a)/Subtraction(s)/Multiplication(m)/Division(d): ');
  String operation = stdin.readLineSync()!;

  // Display Result
  if (operation == 'a'){
    print('The Result of Addition is : ${firstNumber + secondNumber}');
  } else if (operation == 's'){
    print('The Result of Subtraction is : ${firstNumber - secondNumber}');
  } else if (operation == 'm'){
    print('The Result of Multiplication is : ${firstNumber * secondNumber}');
  } else if (operation == 'd'){
    print('The Result of Division is : ${firstNumber / secondNumber}');
  } else {
    print('Error! Enter a valid option...');
  }

}