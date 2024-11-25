// Exercise 10

import 'dart:io';

main(){
  print("--------------");
  print("Tip Calculator");
  print("--------------");
  print("");

  stdout.write("How much did you spend? > ");
  num spend = num.parse(stdin.readLineSync()!);

  stdout.write("what Percentage do you want to tip? > ");
  num tipPercent = num.parse(stdin.readLineSync()!);

  stdout.write("How many people in your group? > ");
  int numberPeople = int.parse(stdin.readLineSync()!);

  num total = (spend + (tipPercent * spend / 100)) / numberPeople;

  print("You each owe $total");

}
