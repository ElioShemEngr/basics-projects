// 8) Programa una función que elimine cierto patrón de caracteres de un texto dado, pe. miFuncion("xyz1, xyz2, xyz3, xyz4 y xyz5", "xyz") devolverá  "1, 2, 3, 4 y 5.

let text = "xyz1, xyz2, xyz3, xyz4 y xyz5";
let pattern = "xyz";

const deletePattern = (textIn, patternIn) => {
    let textOut = textIn.replace(new RegExp(patternIn, 'g'), '');
    return textOut;
};

console.log(deletePattern(text, pattern)); // 1, 2, 3, 4 y 5