using System;
using Anthropic;
using System.Threading.Tasks;
using Anthropic.Models.Messages;


public class Message
{
    public string Role { get; set; } = string.Empty;
    public string Content { get; set; } = string.Empty;
}

public class SystemPrompt
{
    public static async Task Main()
    {
        string apiKey = Environment.GetEnvironmentVariable("ANTHROPIC_API_KEY");
        var client = new AnthropicClient() { ApiKey = apiKey };  
        List<Message> messages = new List<Message>();
        string user_message = "How do I solve 5x+3=2 for x";
        add_user_message(messages, user_message);   
        string response = await chat(client, user_message);
        add_assistant_message(messages, response);
        Console.WriteLine(response);

    }

    public static void add_user_message(List<Message> messages, string text)
    {
        var user_message = new Message { Role = "user", Content = text };
        messages.Add(user_message);
        Console.WriteLine($"-------------\r\nUser: {text}");
    }

    public static void add_assistant_message(List<Message> messages, string text)
    {
        var user_message = new Message { Role = "assistant", Content = text };
        messages.Add(user_message);
        Console.WriteLine($"-------------\r\assistant: {text}");
    }


    public static async Task<string> chat(AnthropicClient client, string user_message)
    {
        var system_prompt = @"You are a patient math tutor.
                        Do not directly answer a student's questions.
                        Guide them to a solution step by step.";
        var parameters = new MessageCreateParams()
        {
            MaxTokens = 1000,

            Messages =
            [
                new()
        {
            Role = Role.User,
            Content = user_message,

        },new()
        {
            Role = Role.Assistant,
            Content = system_prompt,

        },
    ],
            Model = Model.ClaudeSonnet4_0,
        };


        var message = await client.Messages.Create(parameters);

        return message.Content[0].Value.ToString();
    }

}
