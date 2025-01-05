// 3) Programa una función que dada una String te devuelva un Array de textos separados por cierto caracter, pe. miFuncion('hola que tal', ' ') devolverá ['hola', 'que', 'tal'].

// let word = "hola que tal";

// function miFunc (stringVar) {
//     return stringVar.split(' ');
// };

// console.log(miFunc(word));

let word = "hola que tal";

const splitString = (string) => typeof(string) === "string"
? console.log(string.split(' '))
: console.log(`El valor ingresado no es un string`);

splitString(word);