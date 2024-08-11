use std::io::{Read, Write};
use zip::{ZipWriter, CompressionMethod};
use std::path::Path;
use clap::{App, Arg};

fn main() {
    // Get file paths from user input
    let file_paths = get_file_paths();

    // Create a ZIP archive
    let zip_file = std::fs::File::create("output.zip").unwrap();
    let mut zip_writer = ZipWriter::new(zip_file);

    // Iterate over files, compress (optional), and add to ZIP
    for file_path in file_paths {
        let file_name = file_path.file_name().unwrap().to_str().unwrap();
        let mut file = std::fs::File::open(&file_path).unwrap();

        // Optional: compress file using Huffman algorithm
        let compressed_data = huffman_compress(&mut file); // Implement Huffman compression

        // Add file to ZIP
        let mut zip_file = zip_writer.start_file(file_name, CompressionMethod::Stored).unwrap();
        zip_file.write_all(&compressed_data).unwrap();
    }

    zip_writer.finish().unwrap();
}

fn get_file_paths() -> Vec<String> {
    let matches = App::new("zip_creator")
        .version("1.0")
        .author("Your Name <your_email@example.com>")
        .about("Creates a ZIP archive from given files")
        .arg(
            Arg::with_name("FILES")
                .help("Sets the input files to use")
                .required(true)
                .multiple(true)
                .index(1),
        )
        .get_matches();

    matches.values_of_os("FILES")
        .unwrap()
        .map(|v| v.to_str().unwrap().to_string())
        .collect()
}

fn huffman_compress(data: &mut impl Read) -> Vec<u8> {
    // Implement Huffman compression algorithm
    unimplemented!()
}
