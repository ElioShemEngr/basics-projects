import 'dart:io';

main(){
  String response1;
  String response2;
  String response3;

  print("Marvel Movie Character Creator");
  print("");

  stdout.writeln("Your super power is the spider web? :");
  response1 = stdin.readLineSync()!;

  if (response1 == 'yes'){
    print("Yo are Spider Man");
  } else{
    print("Then you're not Spider Man");
    print("Ok next cuestion");
    print("");
  }

  stdout.writeln("You are a big man green?: ");
  response2 = stdin.readLineSync()!;

  if (response2 == 'yes'){
    print("Yo are Hulk");
  } else{
    print("Then you're not Hulk");
    print("Ok next cuestion");
    print("");
  }

  stdout.writeln("You are an enginner?: ");
  response3 = stdin.readLineSync()!;

  if (response3 == 'yes'){
    print("You are Iron Man");
  } else{
    print("Then you're not Iron Man");
    print("Ok I give up on you");
    print("");
  }

}