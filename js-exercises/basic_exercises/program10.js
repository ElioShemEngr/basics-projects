//10) Programa una función que reciba un número y evalúe si es capicúa o no (que se lee igual en un sentido que en otro), pe. miFuncion(2002) devolverá true.

const capicuaNumber = number => {
    const digitsArray = Array.from(String(number), Number);
    let newNumber = digitsArray.reverse().join('');
    newNumber = Number(newNumber);
    // console.log(newNumber);
    // console.log(typeof newNumber);
    if (number === newNumber) {
        return true;
    } else {
        return false;
    };
};  

console.log(capicuaNumber(2002));