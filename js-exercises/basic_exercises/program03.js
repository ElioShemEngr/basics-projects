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