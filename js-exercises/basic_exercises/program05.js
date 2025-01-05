// 5) Programa una función que invierta las palabras de una cadena de texto, pe. miFuncion("Hola Mundo") devolverá "odnuM aloH".

const reverseWords = str => typeof str === 'string' 
? console.log(str.split('').reverse().join('')) 
: console.warn('No se ingresó un string');

reverseWords('Hola Mundo'); // "odnuM aloH"