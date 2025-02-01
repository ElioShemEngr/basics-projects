
// Tema: Búsqueda de perfiles.

var contactos = [
    {
        "nombre": "Nora",
        "apellido": "Nav",
        "numero": "0543236543",
        "gustos": ["Pizza", "Programación"]
    },
    {
        "nombre": "Harry",
        "apellido": "Potter",
        "numero": "0994372684",
        "gustos": ["Hogwarts", "Magia"]
    },
    {
        "nombre": "Sherlock",
        "apellido": "Holmes",
        "numero": "0487345643",
        "gustos": ["Casos interesantes", "Violín"]
    }
];


function buscarPerfil(array, nombre, propiedad) {
    for (let i = 0; i < array.length; i++) {
        if (array[i].nombre === nombre) {
            return contactos[i][propiedad] || "La propiedad no existe";
        }
    }
    return "El contacto no esta en la lista";
}

console.log(buscarPerfil(contactos, "Sherlock", "numero"));