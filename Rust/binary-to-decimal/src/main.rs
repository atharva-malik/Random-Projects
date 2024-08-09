use std::io;

fn main() {
    println!("Welcome to the Binary-Decimal Converter!");

    loop {
        println!("Choose an option:");
        println!("1. Decimal to Binary");
        println!("2. Binary to Decimal");
        println!("3. Exit");

        let mut choice = String::new();
        io::stdin()
            .read_line(&mut choice)
            .expect("Failed to read line");

        let choice: u32 = match choice.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        match choice {
            1 => decimal_to_binary(),
            2 => binary_to_decimal(),
            3 => break,
            _ => println!("Invalid choice. Please try again."),
        }
    }
}

fn decimal_to_binary() {
    println!("Enter a decimal number:");
    let mut decimal = String::new();
    io::stdin()
        .read_line(&mut decimal)
        .expect("Failed to read line");

    let decimal: u32 = match decimal.trim().parse() {
        Ok(num) => num,
        Err(_) => {
            println!("Invalid input. Please enter a valid decimal number.");
            return;
        }
    };

    let binary = format!("{:b}", decimal);
    println!("Binary equivalent: {}", binary);
}

fn binary_to_decimal() {
    println!("Enter a binary number:");
    let mut binary = String::new();
    io::stdin()
        .read_line(&mut binary)
        .expect("Failed to read line");

    let binary: u32 = match u32::from_str_radix(&binary.trim(), 2) {
        Ok(num) => num,
        Err(_) => {
            println!("Invalid input. Please enter a valid binary number.");
            return;
        }
    };

    println!("Decimal equivalent: {}", binary);
}
