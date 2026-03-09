package main

import (
	"context"
	"fmt"
	"os"

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
	message := "How do I solve 5x+3=2 for x"
	add_user_message(messages, message)
	response := chat(client, message)
	add_assistant_message(messages, response)
	fmt.Println(response)

}

func chat(client anthropic.Client, user_message string) string {

	system_prompt := `You are a patient math tutor.
Do not directly answer a student's questions.
Guide them to a solution step by step.`

	message, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
		MaxTokens: 1000,
		Messages: []anthropic.MessageParam{
			anthropic.NewUserMessage(anthropic.NewTextBlock(user_message)),
		},
		Model: anthropic.ModelClaudeSonnet4_5_20250929,
		System: []anthropic.TextBlockParam{
			{Text: system_prompt}},
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
