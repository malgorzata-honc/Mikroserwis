Mikroserwis oraz klient wykonujący proste działania arytmetyczne. 

Serwer: 
- kod napisany jest w Pythonie,
- skrypt do uruchomienia w main.py
- mikroserwis na localhoście
- wykorzystana została gotowa biblitoeka Flask, która tworzy instancję klasy Flask.

Klient:
- kod napisany w C#,
- skrypt do uruchomia w Program.cs
- obsługuje 4 endpointy: add, substract, divide, multiply

Komunikacja: 
- Klient łączy się z odpowiednim endpointem, a następnie wysyłane jest żądanie HTTP (metodą POST) z podanymi wcześniej przez użytkownika liczbami.
Zastosowano gotową metodę C#  - PostAsJsonAsync (ze strony Microsoft: _Wysyła żądanie POST do określonego identyfikatora URI zawierającego value serializowany kod JSON w treści żądania_.)


Rozproszenie żadań:
- W celu implementacji mikroserwisu rozpraszającego żądania pomiędzy trzy instancje mikroserwisu wykorzystano styrategię **Round Robin Load Balancing**. 
Pozwala ona na tworzenie listy instancji serwisu i rotacyjne przekierowywanie żądań do kolejnych instancji zgodnie z cyklem.
Stworzono listę adresów URL serviceUrls reprezentujących różne operacje (add, subtract, multiply, divide). Następnie w każdym wywołaniu żądania wybierany jest adres URL w sposób cykliczny. 
To pozwala na równoważenie obciążenia wysyłanych żądań pomiędzy różnymi instancjami mikroserwisu.

Logi: 
- Dodano logi do kodu serwisu, które będą śledzić, do której konkretnej instancji trafiają żądania. 
Wykorzystano moduł logging do dodania logów przed przekazaniem żądania do konkretnej instancji. Logi zostały dodane przed wywołaniem funkcji obsługującej żądanie dla każdego endpointu, aby śledzić, które żądania trafiają do której instancji.  Zapisanie logów odbywa się do pliku requests.log

Uruchomienie:
- Najpierw należy uruchomić kod serwera (main.py). Po uruchomieniu klienta (z poziomu cmd komendą 'dotnet run') należy wpisać działanie jakie ma zostać wykonane (add, substract, divide, multiply), 
a nastepnie liczbę pierwszą i liczbę drugą (liczby zmiennoprzecinkowe oddzielone znakiem ','). 
