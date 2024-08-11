use std::fs::{File, OpenOptions};
use std::io::{Read, Write};
use serde::{Deserialize, Serialize};
use clap::{App, Arg, SubCommand};
use syntect::{html, parsing, util};

#[derive(Debug, Serialize, Deserialize, Clone)]
struct Snippet {
    id: usize,
    title: String,
    language: String,
    tags: Vec<String>,
    code: String,
}

#[derive(Debug, Serialize, Deserialize)]
struct SnippetStore {
    snippets: Vec<Snippet>,
}

fn save_snippets(snippets: &Vec<Snippet>, file_path: &str) -> Result<(), Box<dyn std::error::Error>> {
    let serialized = serde_json::to_string_pretty(snippets)?;
    let mut file = OpenOptions::new().write(true).create(true).open(file_path)?;
    file.write_all(serialized.as_bytes())?;
    Ok(())
}

fn load_snippets(file_path: &str) -> Result<Vec<Snippet>, Box<dyn std::error::Error>> {
    let mut file = File::open(file_path)?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;
    let snippets: Vec<Snippet> = serde_json::from_str(&contents)?;
    Ok(snippets)
}

fn search_snippets(snippets: &Vec<Snippet>, query: &str) -> Vec<&Snippet> {
    snippets.iter().filter(|s| {
        s.title.contains(query) || s.code.contains(query) || s.tags.iter().any(|t| t.contains(query))
    }).collect()
}

fn highlight_code(code: &str, language: &str) -> String {
    let ss = syntect::parsing::SyntaxSet::load_defaults_newlines();
    let syntax = ss.find_syntax_by_extension(language).unwrap_or_else(|| ss.find_syntax_plain_text());
    let mut hs = syntect::highlighting::Highlighter::new(syntax);
    let mut style = syntect::highlighting::Style::default();
    let mut state = parsing::ParseState::new(syntax);
    let mut output = String::new();
    for line in code.lines() {
        let ops = hs.highlight_line(line, &mut state);
        html::append_styled_str(&mut output, &style, &ops);
    }
    output
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let matches = App::new("snippet_manager")
        .version("1.0")
        .author("Your Name")
        .about("Manages code snippets")
        .subcommand(SubCommand::with_name("add")
            .about("Adds a new snippet")
            .arg(Arg::with_name("title").required(true))
            .arg(Arg::with_name("language").required(true))
            .arg(Arg::with_name("tags").multiple(true))
            .arg(Arg::with_name("code").required(true)))
        .subcommand(SubCommand::with_name("list")
            .about("Lists all snippets"))
        .subcommand(SubCommand::with_name("search")
            .about("Searches for snippets")
            .arg(Arg::with_name("query")))
        .subcommand(SubCommand::with_name("show")
            .about("Shows a snippet")
            .arg(Arg::with_name("id").required(true)))
        .get_matches();

    let snippet_file = "snippets.json";
    let mut snippets = load_snippets(snippet_file)?;

    match matches.subcommand() {
        ("add", Some(sub_matches)) => {
            let title = sub_matches.value_of("title").unwrap();
            let language = sub_matches.value_of("language").unwrap();
            let tags: Vec<_> = sub_matches.values_of("tags").unwrap_or_default().collect();
            let code = sub_matches.value_of("code").unwrap();

            let snippet = Snippet {
                id: snippets.len() + 1,
                title: title.to_string(),
                language: language.to_string(),
                tags,
                code: code.to_string(),
            };
            snippets.push(snippet);
            save_snippets(&snippets, snippet_file)?;
        }
        ("list", Some(_)) => {
            for snippet in &snippets {
                println!("{}: {} ({})", snippet.id, snippet.title, snippet.language);
            }
        }
        ("search", Some(sub_matches)) => {
            let query = sub_matches.value_of("query").unwrap_or("");
            let results = search_snippets(&snippets, query);
            for snippet in results {
                println!("{}: {} ({})", snippet.id, snippet.title, snippet.language);
            }
        }
        ("show", Some(sub_matches)) => {
            let id_str = sub_matches.value_of("id").unwrap();
            let id: usize = id_str.parse()?;
            let snippet = snippets.iter().find(|s| s.id == id).unwrap();
            println!("Title: {}", snippet.title);
            println!("Language: {}", snippet.language);
            println!("Tags: {:?}", snippet.tags);
            println!("Code:\n{}", highlight_code(&snippet.code, &snippet.language));
        }
        _ => {}
    }

    Ok(())
}
