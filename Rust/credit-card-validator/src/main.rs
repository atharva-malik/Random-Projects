use std::error::Error;

fn is_valid_credit_card(card_number: &str) -> Result<bool, Box<dyn Error>> {
    // Remove non-digit characters
    let card_number: String = card_number.chars().filter(|c| c.is_digit(10)).collect();

    // Check card length and prefix
    let card_type = match card_number.as_str() {
        number if number.starts_with("34") || number.starts_with("37") => CardType::AmericanExpress,
        number if number.starts_with("4") => CardType::Visa,
        number if number.starts_with("51") || number.starts_with("52") || number.starts_with("53") ||
                  number.starts_with("54") || number.starts_with("55") => CardType::Mastercard,
        number if number.starts_with("6011") => CardType::Discover,
        _ => return Err("Invalid card type".into()),
    };

    // Check length based on card type
    let valid_lengths = match card_type {
        CardType::AmericanExpress => [15],
        CardType::Visa => [13, 16],
        CardType::Mastercard => [16],
        CardType::Discover => [16],
    };
    if !valid_lengths.contains(&card_number.len()) {
        return Err("Invalid card length".into());
    }

    // Apply Luhn algorithm
    if !luhn_checksum(&card_number) {
        return Err("Invalid checksum".into());
    }

    Ok(true)
}

fn luhn_checksum(card_number: &str) -> bool {
    let mut sum = 0;
    let mut double_next = false;
    for digit in card_number.chars().rev().map(|c| c.to_digit(10).unwrap()) {
        let digit = if double_next {
            let doubled = digit * 2;
            doubled - if doubled > 9 { 9 } else { 0 }
        } else {
            digit
        };
        sum += digit;
        double_next = !double_next;
    }
    sum % 10 == 0
}

#[derive(Debug)]
enum CardType {
    AmericanExpress,
    Visa,
    Mastercard,
    Discover,
}

fn main() {
    let card_number = "37828224345678"; // Example American Express card

    match is_valid_credit_card(card_number) {
        Ok(valid) => println!("Card is valid: {}", valid),
        Err(err) => println!("Error: {}", err),
    }
}
