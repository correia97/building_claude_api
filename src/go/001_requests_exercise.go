package main

import (
	"bufio"
	"context"
	"fmt"
	"os"
	"strings"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
	"github.com/joho/godotenv"
)

func main() {

	// Load the appropriate .env file
	err := godotenv.Load(fmt.Sprintf(".env"))
	if err != nil {
		fmt.Printf("Error loading .env.%s file: %v\n", err)
		return
	}
	apiKey := os.Getenv("ANTHROPIC_API_KEY")
	client := anthropic.NewClient(
		option.WithAPIKey(apiKey),
	)
	messages := []string{}

	scanner := bufio.NewScanner(os.Stdin)
	for {
		var user_input string
		fmt.Print(">: ")
		if !scanner.Scan() {
			break
		}
		user_input = scanner.Text()

		if strings.TrimSpace(user_input) == "" {
			break
		}
		fmt.Println(">", user_input)
		add_user_message(messages, user_input)
		answer := chat(client, user_input)
		add_assistant_message(messages, answer)
		fmt.Println("-----")
		fmt.Println(answer)
		fmt.Println("-----")
	}
	// Handle any errors that occurred during scanning
	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, "Error reading input:", err)
	}
}

func chat(client anthropic.Client, user_message string) string {
	message, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
		MaxTokens: 1000,
		Messages: []anthropic.MessageParam{
			anthropic.NewUserMessage(anthropic.NewTextBlock(user_message)),
		},
		Model: anthropic.ModelClaudeSonnet4_5_20250929,
	})
	if err != nil {
		fmt.Fprintln(os.Stderr, "Error creating message:", err)
		panic(err.Error())
	}
	return message.Content[0].Text
}

func add_user_message(messages []string, text string) {
	messages = append(messages, text)
	fmt.Printf("--------------\r\nUser: %s\n", text)
}
func add_assistant_message(messages []string, text string) {
	messages = append(messages, text)
	fmt.Printf("--------------\r\nAssistant: %s\n", text)
}
