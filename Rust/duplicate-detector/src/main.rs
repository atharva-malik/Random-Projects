use std::{collections::HashMap, fs::File, io::{BufRead, BufReader, Write}};
use colored::*;

fn main() -> std::io::Result<()> {
    let args: Vec<String> = std::env::args().collect();
    if args.len() != 2 {
        eprintln!("Usage: {} <input_file>", args[0]);
        std::process::exit(1);
    }

    let input_file = &args[1];
    let output_file = "output.txt";
    let duplicates_file = "duplicates.txt";

    let file = File::open(input_file)?;
    let reader = BufReader::new(file);

    let mut word_counts: HashMap<String, usize> = HashMap::new();
    let mut text_without_duplicates: String = String::new();

    for line in reader.lines() {
        let line = line?;
        let words: Vec<&str> = line.split_whitespace().collect();

        for word in words {
            let word = word.to_lowercase();
            let count = word_counts.entry(word.clone()).or_insert(0);
            *count += 1;

            if *count == 1 {
                text_without_duplicates.push_str(&word);
                text_without_duplicates.push(' ');
            } else {
                text_without_duplicates.push_str(&format!("{}", word.red()));
                text_without_duplicates.push(' ');
            }
        }

        text_without_duplicates.push('\n');
    }

    println!("{}", text_without_duplicates);

    let mut output_file = File::create(output_file)?;
    output_file.write_all(text_without_duplicates.as_bytes())?;

    let mut duplicates: Vec<(usize, String)> = word_counts
        .iter()
        .filter(|(_, count)| *count > 1)
        .map(|(word, count)| (*count, word.clone()))
        .collect();

    duplicates.sort_by(|a, b| b.0.cmp(&a.0));

    let mut duplicates_file = File::create(duplicates_file)?;
    for (count, word) in duplicates {
        let line = format!("{}: {}\n", count, word);
        duplicates_file.write_all(line.as_bytes())?;
    }

    Ok(())
}
