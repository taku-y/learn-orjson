use ndarray::{array, Array1};
use serde_json::json;
use serde::Serialize;
use std::fs::File;
use std::io::Write;

#[derive(Serialize)]
struct Data {
    name: String,
    x: Vec<Array1<f32>>,
}

fn main() {
    // Create object
    let data = Data {
        name: "test".to_string(),
        x: vec![
            array![1.0, 2.0, 3.0],
        ],
    };

    // Serialize object to JSON
    let json = json!(data);

    // Write JSON to file
    let mut file = File::create("data.json").unwrap();
    file.write_all(serde_json::to_string_pretty(&json).unwrap().as_bytes())
        .unwrap();
}
