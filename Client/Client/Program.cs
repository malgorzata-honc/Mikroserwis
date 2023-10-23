using System;
using System.Net.Http;
using System.Threading.Tasks; 

class Program
{
    static async Task Main(string[] args)
    {
        Console.WriteLine("Wybierz typ działania (add, subtract, multiply, divide):"); 
        String operation = Console.ReadLine();

        Console.WriteLine("Typ działania to: " + operation);

        Console.ReadKey();

         Console.WriteLine("Podaj pierwszą liczbę: ");
        decimal num1 = Convert.ToDecimal(Console.ReadLine());

        Console.WriteLine("Podaj drugą liczbę: ");
        decimal num2 = Convert.ToDecimal(Console.ReadLine()); 

        

        using (HttpClient client = new HttpClient())
        {
            string apiUrl = $"http://localhost:5000/{operation}"; // Adres URL mikroserwisu

            var requestData = new
            {
                num1,
                num2
            };

            // Wysłanie żądania HTTP POST z danymi JSON
            var response = await client.PostAsJsonAsync(apiUrl, requestData);

            if (response.IsSuccessStatusCode)
            {
                var result = await response.Content.ReadAsAsync<dynamic>();
                Console.WriteLine($"Wynik {operation}: {result.result}");
            }
            else
            {
                Console.WriteLine("Błąd w żądaniu HTTP.");
            }
        } 
        
    }  
}

