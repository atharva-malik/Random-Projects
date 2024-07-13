use std::io;

fn main() {
    let x: i64 = 255;
    let y: i32 = 10;

    let z = x + (y as i64); // this works?!
    println!("z is {}", z);

    let u_input = input();
    let int_input: f64 = u_input.trim().parse().unwrap();
    print!("u is {}", int_input + 1.0f64);
}

fn input() -> String{
    let mut s = String::new();
    io::stdin().read_line(&mut s).expect("Failed to read line");
    return  s;
}
