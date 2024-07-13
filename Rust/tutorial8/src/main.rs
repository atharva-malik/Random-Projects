fn main() {
    println!("Hello, world!");
    let result = add_numbers(20, 30);
    println!("{}", result);
}

fn add_numbers(x: i32, y: i32) -> i32 {
    println!("Adding {} and {}", x, y);
    println!("Their sum is {}", x + y);
    x + y
}
