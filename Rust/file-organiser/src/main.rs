use std::fs::{create_dir_all, rename};
use std::path::{Path, PathBuf};
use walkdir::WalkDir;
use clap::{Arg, Command};

fn main() {
    let matches = Command::new("file_organizer")
        .version("1.0")
        .author("Your Name <your_email@example.com>")
        .about("Organizes files based on their extensions")
        .arg(Arg::new("source")
            .short('s')
            .long("source")
            .value_name("DIR")
            .help("Sets the source directory to organize")
            .takes_value(true)
            .required(true))
        .arg(Arg::new("destination")
            .short('d')
            .long("destination")
            .value_name("DIR")
            .help("Sets the destination directory")
            .takes_value(true)
            .required(true))
        .get_matches();

    let source_dir = matches.value_of("source").unwrap();
    let dest_dir = matches.value_of("destination").unwrap();

    let extensions: Vec<&str> = vec![".txt", ".jpg", ".png", ".mp3"]; // Customize extensions

    for entry in WalkDir::new(source_dir) {
        let entry = entry.unwrap();
        let path = entry.path();
        if path.is_file() {
            let ext = path.extension().and_then(|s| s.to_str()).unwrap_or("");
            if extensions.contains(&ext) {
                let dest_path = Path::new(dest_dir).join(ext.trim_start_matches('.'));
                create_dir_all(&dest_path).expect("Failed to create destination directory");
                let new_path = dest_path.join(path.file_name().unwrap());
                if new_path != *path {
                    rename(path, &new_path).expect("Failed to move file");
                }
            }
        }
    }
}
