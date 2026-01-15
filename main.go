package main

import (
    "encoding/json"
    "fmt"
    "io"
    "net/http"
    "os"
)

func main() {
    url := "https://www.kernel.org/releases.json"

    resp, err := http.Get(url)
    if err != nil {
        fmt.Println("Error making the HTTP request:", err)
        os.Exit(1)
    }
    defer resp.Body.Close()

    body, err := io.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading the response body:", err)
        os.Exit(1)
    }

    var data map[string]interface{}
    if err := json.Unmarshal(body, &data); err != nil {
        fmt.Println("Error parsing the JSON response:", err)
        os.Exit(1)
    }

    // Extract the value from the JSON response
    latest_stable := data["latest_stable"].(map[string]interface{})
    version := latest_stable["version"].(string)

    // Print the selected value to the console
    fmt.Println("Latest stable linux kernel is ", version)
}
