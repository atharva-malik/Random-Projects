use reqwest::blocking::Client;
use serde::{Deserialize, Serialize};
use geolocator::{Geocoder, Location};

#[derive(Debug, Serialize, Deserialize)]
struct WeatherResponse {
    main: Main,
    weather: Vec<Weather>,
    name: String,
}

#[derive(Debug, Serialize, Deserialize)]
struct Main {
    temp: f32,
    feels_like: f32,
    temp_min: f32,
    temp_max: f32,
    pressure: i32,
    humidity: i32,
}

#[derive(Debug, Serialize, Deserialize)]
struct Weather {
    main: String,
    description: String,
}

fn get_weather_by_zipcode(zipcode: &str, api_key: &str) -> Result<WeatherResponse, Box<dyn std::error::Error>> {
    let url = format!("https://api.openweathermap.org/data/2.5/weather?zip={},us&appid={}", zipcode, api_key);
    let response = Client::new().get(&url).send()?;
    let weather: WeatherResponse = response.json()?;
    Ok(weather)
}

fn get_weather_by_location(api_key: &str) -> Result<WeatherResponse, Box<dyn std::error::Error>> {
    let geocoder = Geocoder::new();
    let location = geocoder.locate()?;
    let lat = location.latitude;
    let lon = location.longitude;

    let url = format!("https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}", lat, lon, api_key);
    let response = Client::new().get(&url).send()?;
    let weather: WeatherResponse = response.json()?;
    Ok(weather)
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Replace with your OpenWeatherMap API key
    let api_key = "YOUR_API_KEY";

    // Option 1: Get weather by zip code
    let zipcode = "10001"; // Replace with your zip code
    let weather = get_weather_by_zipcode(zipcode, api_key)?;
    println!("Weather for zip code {}: {:?}", zipcode, weather);

    // Option 2: Get weather by location
    let weather = get_weather_by_location(api_key)?;
    println!("Weather for your location: {:?}", weather);

    Ok(())
}
