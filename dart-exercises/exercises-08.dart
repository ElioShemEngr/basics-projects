// Exercise 08

import 'dart:io';

main(){
  print ('wholesome Positivity Machine');
  print ('');

  String nameUser;
  String response;
  String scale;

  stdout.write("Who are you?: ");
  nameUser = stdin.readLineSync()!;

  stdout.write("What do you want to achieve today?: ");
  response = stdin.readLineSync()!;

  stdout.write("On Scale of 1 - 10 how do you feel today? (1: 😢,10:🥳): ");
  scale = stdin.readLineSync()!;

  if (scale == "1" || scale == "2" || scale == "3"){
    print ("Hey $nameUser, keep your chin up! Today you're going to $response in the most amazing way, simply by being you - YOU ROCK!");
  } else if (scale == "4" || scale == "5" || scale == "6"){
    print ("Hey $nameUser You're going on!");
  } else {
    print ("Hey $nameUser Perfect, thank you for that 🥳");
  }

}
