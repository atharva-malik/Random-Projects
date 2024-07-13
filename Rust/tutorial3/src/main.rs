fn main() {
    const PI: f32 = 3.14;
    println!("{}", PI);
    {
        const PI: f32 = 10.0;
        println!("PI is: {}", PI);
    }
    let x: i32 = 4;
    println!("x is: {}", x);
    {
        let x: i32 = x - 2;
        println!("x is: {}", x);
    }
    let x: i32 = x + 1;
    println!("x is: {}", x);
}
