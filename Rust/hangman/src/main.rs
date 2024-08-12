use rand::Rng;

fn main() {
    let words = ["apple", "banana", "orange", "grape", "kiwi"];
    let random_word = words[rand::thread_rng().gen_range(0..words.len())];

    let mut guessed_letters: Vec<char> = Vec::new();
    let mut lives = 6;

    loop {
        // Display the current game state
        println!("Lives remaining: {}", lives);
        print!("Word: ");
        for letter in random_word.chars() {
            if guessed_letters.contains(&letter) {
                print!("{}", letter);
            } else {
                print!("_");
            }
        }
        println!();

        // Get user input
        let mut guess = String::new();
        std::io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line");
        let guess: char = guess.trim().chars().next().unwrap_or_default();

        // Update game state
        if random_word.contains(guess) {
            println!("Correct!");
        } else {
            println!("Incorrect!");
            lives -= 1;
        }
        guessed_letters.push(guess);

        // Check for win or loss
        if random_word.chars().all(|c| guessed_letters.contains(&c)) {
            println!("You win!");
            break;
        } else if lives == 0 {
            println!("You lose! The word was: {}", random_word);
            break;
        }
    }
}
