// Exercise 06

import 'dart:io';

main()
{
  String username;
  String password;

  print("MY LOGIN SYSTEM");
  print("");

  stdout.writeln("Username :");
  username = stdin.readLineSync()!;

  stdout.writeln("Password :");
  password = stdin.readLineSync()!;

  if (username == 'Elio' && password == 'Xai9kzcm'){
    print("Have a great day Elio");
  } else if (username == 'Elio' || password == 'Xai9kzcm'){
    print("User o Password incorrect");
  } else {
    print("this user not exist!");
  }

}