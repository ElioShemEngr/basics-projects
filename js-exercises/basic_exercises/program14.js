// 14) Programa una función para convertir grados Celsius a Fahrenheit y viceversa, pe. miFuncion(0,"C") devolverá 32°F.

const convertTemperature = (temperature, unit) => {
    if (unit === 'C') {
        return `${temperature}°C son ${temperature * 9 / 5 + 32}°F`;
    } else if (unit === 'F') {
        return `${temperature}°F son ${(temperature - 32) * 5 / 9}°C`;
    } else {
        return 'Unidad no válida';
    }
};

console.log(convertTemperature(0, 'C'));