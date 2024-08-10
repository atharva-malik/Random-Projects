use std::fmt;

#[derive(Debug)]
struct NumberComponents {
    trillions: u32,
    billions: u32,
    millions: u32,
    thousands: u32,
    hundreds: u32,
    tens: u32,
    units: u32,
}

impl NumberComponents {
    fn new(num: u64) -> Self {
        let mut num = num;
        let trillions = (num / 1_000_000_000_000) as u32;
        num %= 1_000_000_000_000;
        let billions = (num / 1_000_000_000) as u32;
        num %= 1_000_000_000;
        let millions = (num / 1_000_000) as u32;
        num %= 1_000_000;
        let thousands = (num / 1000) as u32;
        num %= 1000;
        let hundreds = (num / 100) as u32;
        num %= 100;
        let tens = (num / 10) as u32;
        let units = num % 10;
        Self {
            trillions,
            billions,
            millions,
            thousands,
            hundreds,
            tens,
            units,
        }
    }
}

fn number_to_words(num: u64) -> String {
    let components = NumberComponents::new(num);

    let mut words = String::new();

    if components.trillions != 0 {
        words += &format!("{} trillion ", number_to_words(components.trillions as u64));
    }
    if components.billions != 0 {
        words += &format!("{} billion ", number_to_words(components.billions as u64));
    }
    if components.millions != 0 {
        words += &format!("{} million ", number_to_words(components.millions as u64));
    }
    if components.thousands != 0 {
        words += &format!("{} thousand ", number_to_words(components.thousands as u64));
    }

    let hundreds_str = match components.hundreds {
        0 => String::new(),
        1 => "one hundred ".to_string(),
        _ => format!("{} hundred ", number_to_words(components.hundreds as u64)),
    };

    let tens_str = match components.tens {
        0 => String::new(),
        1 => match components.units {
            0 => "ten".to_string(),
            1 => "eleven".to_string(),
            2 => "twelve".to_string(),
            3 => "thirteen".to_string(),
            4 => "fourteen".to_string(),
            5 => "fifteen".to_string(),
            6 => "sixteen".to_string(),
            7 => "seventeen".to_string(),
            8 => "eighteen".to_string(),
            9 => "nineteen".to_string(),
            _ => unreachable!(),
        },
        _ => {
            let tens_word = match components.tens {
                2 => "twenty",
                3 => "thirty",
                4 => "forty",
                5 => "fifty",
                6 => "sixty",
                7 => "seventy",
                8 => "eighty",
                9 => "ninety",
                _ => unreachable!(),
            };
            format!("{} {}", tens_word, match components.units {
                0 => String::new(),
                _ => format!("{}", number_to_words(components.units as u64)),
            })
        },
    };

    words += &hundreds_str;
    words += &tens_str;
    words += &match components.units {
        0 if hundreds_str.is_empty() && tens_str.is_empty() => String::new(),
        _ => format!("{}", number_to_words(components.units as u64)),
    };

    words.trim().to_string()
}

fn main() {
    let num = 1234567890;
    let words = number_to_words(num);
    println!("{}", words);
}
