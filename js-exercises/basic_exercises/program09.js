// 9) Programa una función que obtenga un numero aleatorio entre 501 y 600.

const randomNumber = () => {
    console.log(Math.floor(Math.random()*(600 - 500) + 500))
}; 

randomNumber();