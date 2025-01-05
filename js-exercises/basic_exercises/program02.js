// 2) Programa una función que te devuelva el texto recortado según el número de caracteres indicados, pe. miFuncion("Hola Mundo", 4) devolverá "Hola".

// let Text = "Hola mundo";

// function trimText (stringVar, num){
//     console.log(stringVar.slice(0,num));
// };

// trimText(Text, 4);

const cutString = (string, separator) => typeof(string) === "string"
? console.log(string.slice(0, separator))
:console.log(`El valor ingresado no es un string`);

let word = "Hola mundo";

cutString(word, 4);
