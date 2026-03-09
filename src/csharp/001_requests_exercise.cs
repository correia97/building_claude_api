using System;
using Anthropic;
using System.Threading.Tasks;
using Anthropic.Models.Messages;

public class RequestsExercise
{
    public static async Task Main()
    {
        string apiKey = Environment.GetEnvironmentVariable("ANTHROPIC_API_KEY");
        var client = new AnthropicClient() { ApiKey = apiKey };
        List<Message> messages = new List<Message>();


        while (true)
        {
            Console.WriteLine("Enter your question: ");
            var user_input = Console.ReadLine();

            //# Add the initial user question
            add_user_message(messages, user_input);

            //# Get Claude's response
            var answer = await chat(client, user_input);

            //# Add Claude's response to the conversation history
            add_assistant_message(messages, answer);

            Console.WriteLine("-----");
            Console.WriteLine(answer);
            Console.WriteLine("-----");
        }



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
        var parameters = new MessageCreateParams()
        {
            MaxTokens = 1000,

            Messages =
            [
                new()
        {
            Role = Role.User,
            Content = user_message,

        },
    ],
            Model = Model.ClaudeSonnet4_0,
        };


        var message = await client.Messages.Create(parameters);

        return message.Content[0].Value.ToString();
    }

}



