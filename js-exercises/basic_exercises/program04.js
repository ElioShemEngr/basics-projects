// let word = "Hola ";

// function miFunc (stringVar, num) {
//     console.log(stringVar.repeat(num));
// };

// miFunc(word, 4);

let word = "Hola ";

const repeatWord = (string, times) => typeof(string) === "string"
? console.log(string.repeat(times))
: console.log(`El valor ingresado no es un string`);

repeatWord(word, 3);