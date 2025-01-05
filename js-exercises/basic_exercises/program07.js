// 7) Programa una función que valide si una palabra o frase dada, es un palíndromo (que se lee igual en un sentido que en otro), pe. mifuncion("Salas") devolverá true.

const isPalindrome = (textIn) => {
    textIn = textIn.toLowerCase();
    if (textIn.split('').reverse().join('') === textIn) {
        return true;
    } else { 
        return false;
    };
};

console.log(isPalindrome("Salas")); // true