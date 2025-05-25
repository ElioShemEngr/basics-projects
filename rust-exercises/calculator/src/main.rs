use crossterm::{
    cursor::MoveTo,
    execute,
    style::Print,
    terminal::{Clear, ClearType},
};
use std::io;

fn calculator(operation: &str, number_one: i32, number_two: i32) {
    match operation {
        "s" => {
            let result: i32 = number_one + number_two;
            println!("El resultado de la suma es: {}", result);
        }
        "r" => {
            let result: i32 = number_one - number_two;
            println!("El resultado de la resta es: {}", result);
        }
        "m" => {
            let result: i32 = number_one * number_two;
            println!("El resultado de la multiplicacion es: {}", result);
        }
        "d" => {
            let result: i32 = number_one / number_two;
            println!("El resultado de la division es: {}", result);
        }
        _ => println!("The type of operation is not recognize"),
    }
}

fn clear_screen() {
    let mut stdout = io::stdout();
    execute!(
        stdout,
        Clear(ClearType::All), // Limpia toda la pantalla
        MoveTo(0, 0),          // Mueve el cursor a la esquina superior izquierda
        Print("")              // Opcionalmente forzamos un "flush" inmediato
    )
    .unwrap();
}

fn main() {
    let mut exit = String::new();

    while exit.trim() != "yes" {
        clear_screen();

        let mut value_one = String::new();
        let mut value_two = String::new();
        let mut operation = String::new();

        println!("Enter First Value: ");
        io::stdin()
            .read_line(&mut value_one)
            .expect("Error! Enter valid value");

        let number_one: i32 = value_one
            .trim()
            .parse()
            .expect("Please enter a valid number");

        println!("Enter Second Value: ");
        io::stdin()
            .read_line(&mut value_two)
            .expect("Error! Enter valid value");

        let number_two: i32 = value_two
            .trim()
            .parse()
            .expect("Please enter a valid number");

        println!("Enter the type Operation(s/r/m/d):");
        io::stdin()
            .read_line(&mut operation)
            .expect("Enter valid value");

        let operation = operation.trim();

        println!("");

        calculator(operation, number_one, number_two);

        println!("Exit? (yes to exit): ");
        exit.clear();
        io::stdin()
            .read_line(&mut exit)
            .expect("Enter a valid value");
    }
}
