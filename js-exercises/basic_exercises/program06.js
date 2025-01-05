// 6) Programa una función para contar el número de veces que se repite una palabra en un texto largo, pe. miFuncion("hola mundo adios mundo", "mundo") devolverá 2.

let text = 'hola mundo adios mundo';

const repeatWord = (textIn, wordIn) => {
    let text = textIn.toLowerCase();
    let word = wordIn.toLowerCase();
    let count = 0;
    let words = text.split(' ');
    words.forEach((element) => {
        if (element === word) {
            count++;
        }
    });
   console.log(count);

};

repeatWord(text, 'mundo'); // 2