using System;
using System.Net.Http;
using System.Threading.Tasks; 

class Program
{
    static async Task Main(string[] args)
    {
        // Lista adresów URL instancji mikroserwisu
        string[] serviceUrls = {
            "http://localhost:5000/add",
            "http://localhost:5000/subtract",
            "http://localhost:5000/multiply",
            "http://localhost:5000/divide",
            "http://localhost:5001/add",
            "http://localhost:5001/subtract",
            "http://localhost:5001/multiply",
            "http://localhost:5001/divide",
            "http://localhost:5002/add",
            "http://localhost:5002/subtract",
            "http://localhost:5002/multiply",
            "http://localhost:5002/divide"
        };

        int currentInstanceIndex = 0;


        Console.WriteLine("Wybierz typ działania (add, subtract, multiply, divide):"); 
        String operation = Console.ReadLine();

        Console.WriteLine("Typ działania to: " + operation);


        Console.WriteLine("Podaj pierwszą liczbę: ");
        decimal num1 = Convert.ToDecimal(Console.ReadLine());

        Console.WriteLine("Podaj drugą liczbę: ");
        decimal num2 = Convert.ToDecimal(Console.ReadLine()); 

        
        using (HttpClient client = new HttpClient())
        {
             string apiUrl = serviceUrls[currentInstanceIndex]; // Wybieranie adresu URL z listy

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
        
        currentInstanceIndex = (currentInstanceIndex + 1) % serviceUrls.Length; // Przejście do następnej instancji
        
    }  
}

