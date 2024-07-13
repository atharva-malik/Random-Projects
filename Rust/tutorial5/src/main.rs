use std::io;

fn main() {
    println!("Hello, world!");
    let mut input: String = String::new();

    io::stdin().read_line(&mut input).expect("failed to read line"); //TODO: Create a simpler way to do this for future projects.
    println!("You said: {}", input);
}
