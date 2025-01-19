const coleccionDeDiscos = {
    7853 : {
        tituloDelAlbum: "Bee Gees greatest",
        artista: "Bee Gees",
        canciones: ["Stayin Alive"]
    },
    5439: {
        tituloDelAlbum: "ABBA Gold",
    }
}

function actualizarDiscos (discos, id, propiedad, valor) {
    if (valor === ""){
        delete discos[id][propiedad];
    } else if (propiedad === "canciones") {
        discos[id][propiedad] = discos[id][propiedad] || [];
        discos[id][propiedad].push(valor);
    } else {
        discos[id][propiedad] = valor;
    }
}



actualizarDiscos(coleccionDeDiscos, 5439, "artista", "ABBA");
console.log(coleccionDeDiscos[5439].artista);

actualizarDiscos(coleccionDeDiscos, 5439, "canciones", "Dancing Queen");
console.log(coleccionDeDiscos[5439].canciones);

