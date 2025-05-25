const menu = [
    {name: "Margherita", price: 8},
    {name: "Pepperoni", price: 10},
    {name: "Hawaiian", price: 9},
    {name: "Veggie", price: 11},
]

const cashInRegister = 100;
const orderQueue = [];

function addNewPizza (pizzaObj) {
    menu.push(pizzaObj);
}

function placeOrder(namePizza) {
    for (let item of menu) {
        if (item.name === namePizza) {
            console.log("The pizza is ready in the menu list");
            return;
        }
    }
    console.log("Add pizza to the menu");
}

placeOrder("Veggie");