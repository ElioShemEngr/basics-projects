// 1) Programa una función que cuente el número de caracteres de una cadena de texto, pe. miFuncion("Hola Mundo") devolverá 10.

// let words = "Hola Mundo";

// function countChart(stringVar) {
//     console.log(stringVar.length);
// };

// countChart(words);

let words = "Hola Mundo";

const countString = string => typeof(string) === "string"
? console.log(string.length) 
: console.log(`El valor ingresado no es un string`);

countString(words);

