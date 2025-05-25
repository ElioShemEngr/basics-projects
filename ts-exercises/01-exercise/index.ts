const menu = [
    {name: "Margherita", price: 8},
    {name: "Pepperoni", price: 10},
    {name: "Hawaiian", price: 9},
    {name: "Veggie", price: 11},
]

const cashInRegister = 100;
const orderQueue = [];

// Challenge
interface Pizza {
    name: string;
    price: number;  
}

const newPizza = {
    name: "",
    price: 0,
};

newPizza.name = "American";
newPizza.price = 8;

function addNewPizza (object: object, menus: Array<object>) {
    menus.push(object);
}

addNewPizza(newPizza, menu);

console.log(menu);


