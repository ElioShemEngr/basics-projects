// Exercise 08

import 'dart:io';

main(){
  print("Generation Identifier");
  print("---------------------");
  print("");

  stdout.write("What's your name? >  ");
  String nameUser = stdin.readLineSync()!;

  stdout.write("What's your name? >  ");
  int yearBirth = int.parse(stdin.readLineSync()!);

  if (yearBirth >= 1883 && yearBirth <= 1900){
    print("Hah! $nameUser, You are the Lost Generation");
  } else if (yearBirth >=1901 && yearBirth <=1927){
    print("Hah! $nameUser, You are the Greatest Generation");
  } else if (yearBirth >=1928 && yearBirth <=1945){
    print("Hah! $nameUser, You are Silent Generation");
  } else if (yearBirth >=1946 && yearBirth <=1964){
    print("Hah! $nameUser, You are Baby Boomers");
  } else if (yearBirth >=1965 && yearBirth <=1980){
    print("Hah! $nameUser, You are the Generation X");
  } else if (yearBirth >=1981 && yearBirth <=1996){
    print("Hah! $nameUser, You are the Millenials");
  } else if (yearBirth >=1997 && yearBirth <=2012){
    print("Hah! $nameUser, You are Generation Z");
  } else if (yearBirth >=2013 && yearBirth <=2023){
    print("Hah! $nameUser, You are Generation Alpha");
  } else{
    print("In outer year please");
  }

}

