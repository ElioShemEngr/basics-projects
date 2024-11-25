// Exercise 07

import 'dart:io';

main()
{
  
  print ('Fake Fan Finder');
  print ('---------------');
  print ('');

  stdout.write("What is your favorite anime? > ");
  String anime = stdin.readLineSync()!.toLowerCase();

  if (anime == 'dragon ball'){
    print("Oh, it's really cool!");
    stdout.write("Name me any of the characters? > ");
    String favCharacter = stdin.readLineSync()!;

    if (favCharacter == 'goku'){
      print("You got by pure chance");
      stdout.write("Okey then, What is the name her power? > ");
      String powerName = stdin.readLineSync()!;

        if (powerName == "kamehame ha"){
          print("You are true fan!");
        } else if (powerName == "henki dama") {
          print("You are true fan!, but hamehame ha is the best");
        } else {
          print("Nah, You are Fake Fan");
        }
    } else if (favCharacter == 'vegeta') {
      print("Aww, he is the best character");
    } else {
      print("Nah, goku's the greatest");
    }
  } else if (anime == 'naruto'){
    print("Aww, sad times");
  } else {
    print("Yeah, that's cool and all…");
  }

}