import json

# Example content
content = """async function fetchData() {
    let response = await fetch('https://api.example.com/data');
    let data = await response.json();
    console.log(data);
}
fetchData();"""

# Convert content to a JSON-compatible string
json_string = json.dumps(content)

# Display the JSON string
print(json_string)
