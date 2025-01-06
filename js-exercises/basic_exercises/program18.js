// 18) Programa una función que dada una cadena de texto cuente el número de vocales y consonantes, pe. miFuncion("Hola Mundo") devuelva Vocales: 4, Consonantes: 5.

const countVowelsAndConsonants = (str = "") => {
  if (!str) return console.warn("No ingresaste una cadena de texto");

  if (typeof str !== "string")
    return console.error("El valor ingresado no es una cadena de texto");

  let vowels = 0,
    consonants = 0;

  str = str.toLowerCase();

  for (let i of str) {
    if (/[aeiouáéíóúü]/.test(i)) vowels++;
    if (/[bcdfghjklmnñpqrstvwxyz]/.test(i)) consonants++;
  }

  return console.info({
    str,
    vowels,
    consonants,
  });
};


countVowelsAndConsonants("Hola Mundo"); // {str: "hola mundo", vowels: 4, consonants: 5}