use std::io;

fn main() {
    println!("Welcome to the Unit Converter!");

    // Main loop for repeated conversions
    loop {
        // Get user input for source unit, target unit, and value
        let source_unit = get_user_input("Enter source unit:");
        let target_unit = get_user_input("Enter target unit:");
        let value = get_user_input_f32("Enter value:");

        // Perform conversion based on unit types
        match (source_unit.as_str(), target_unit.as_str()) {
            ("celsius", "fahrenheit") => convert_temp(value, "C", "F"),
            ("fahrenheit", "celsius") => convert_temp(value, "F", "C"),
            // ... other conversions ...
            _ => println!("Unsupported conversion."),
        }

        // Option to continue or exit
        println!("Do you want to perform another conversion? (y/n)");
        let mut answer = String::new();
        io::stdin().read_line(&mut answer).expect("Failed to read line");
        if answer.trim().to_lowercase() != "y" {
            break;
        }
    }
}

// Helper functions for input and conversions
fn get_user_input(prompt: &str) -> String {
    println!("{}", prompt);
    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read line");
    input.trim().to_string()
}

fn get_user_input_f32(prompt: &str) -> f32 {
    loop {
        println!("{}", prompt);
        let mut input = String::new();
        io::stdin()
            .read_line(&mut input)
            .expect("Failed to read line");
        match input.trim().parse() {
            Ok(value) => return value,
            Err(_) => println!("Invalid input. Please enter a number."),
        }
    }
}


fn convert_temp(value: f32, from: &str, to: &str) {
    match (from, to) {
        ("C", "F") => {
            let fahrenheit = value * 9.0 / 5.0 + 32.0;
            println!("{} Celsius = {} Fahrenheit", value, fahrenheit);
        }
        ("F", "C") => {
            let celsius = (value - 32.0) * 5.0 / 9.0;
            println!("{} Fahrenheit = {} Celsius", value, celsius);
        }
        _ => println!("Unsupported temperature conversion."),
    }
}

