use std::env;
use std::fs;
use std::io::ErrorKind;
use std::collections::HashMap;

fn main() {
    let args: Vec<String> = env::args().collect();
    let mut tokens = HashMap::new();
    let file_path = &args[1];
    let contents = file_reader(file_path.to_string());
    let mut index = 0;

    for val in &contents {
        println!("val: {val}");
        for pos_char in val.to_string().chars() {
            println!("pos_char: {pos_char}");
            if pos_char.is_whitespace() {
                tokens.insert("WHITE", pos_char);
            } else if pos_char.is_alphabetic() {
                tokens.insert("CHAR", pos_char);
            } else {
                tokens.insert("UNKNOWN", pos_char);
            }
        }
    }

    for (key, val) in tokens {
        println!("key {key} value {val}")
    }
}

fn file_reader(path: String) -> Result<String, std::io::Error> {
    let got_file = fs::read_to_string(path);
    let got_file = match got_file {
        Ok(file) => file,
        Err(error) => match error.kind() {
            ErrorKind::NotFound => panic!("Couldn't find file"),
            _ => panic!("Unexpected error")
        }
    };

    Ok(got_file)
}