// 13) Programa una función que determine si un número es par o impar, pe. miFuncion(29) devolverá Impar.

const primeNumber = (num) => {
    if (num % 2 === 0) {
        console.log(`El numero ${num} es Par`);
    } else {
        console.log(`El numero ${num} es Impar`);
    };
};

primeNumber(6);