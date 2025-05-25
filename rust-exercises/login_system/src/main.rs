use std::io;

// Function to handle user login logic
fn login_system() {
    let mut name = String::new();
    let mut password = String::new();

    println!("My System Login");
    println!("---------------");

    // Prompt for username
    println!("Enter username:");
    io::stdin()
        .read_line(&mut name)
        .expect("Failed to read input");

    let user_name = name.trim(); // Trim input to remove extra spaces or newlines

    // Check username
    if user_name == "ElioshemDev" {
        println!("Enter your password:");
        io::stdin()
            .read_line(&mut password)
            .expect("Failed to read input");

        let user_password = password.trim(); // Trim input to remove extra spaces or newlines

        // Check password
        if user_password == "Xai9kzcm" {
            println!("Hi, Welcome {}", user_name);
        } else {
            println!("Your Password is incorrect!!");
        }
    } else {
        println!("Your username is incorrect!!");
    }
}

fn main() {
    // Refactored to separate the login logic into its own function for better modularity
    login_system();
}
