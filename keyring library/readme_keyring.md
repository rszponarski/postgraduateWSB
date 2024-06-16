# Biblioteka Keyring - Bezpieczne zarządzanie danymi poufnymi

Biblioteka `keyring` to narzędzie w języku Python, które umożliwia bezpieczne przechowywanie i zarządzanie hasłami, tokenami dostępu oraz innymi poufnymi danymi w aplikacjach. Jest to szczególnie przydatne, gdy aplikacja wymaga przechowywania poufnych informacji, ale nie chcesz trzymać ich w kodzie źródłowym.

## Główne cechy

- **Bezpieczne składowanie danych:** Biblioteka `keyring` współpracuje z systemowymi mechanizmami przechowywania haseł, takimi jak macOS Keychain, Windows Credential Store czy Linux Secret Service, zapewniając bezpieczne przechowywanie danych na różnych platformach.
  
- **Prosta integracja:** Umożliwia łatwą integrację z aplikacjami Python, eliminując potrzebę bezpośredniego zarządzania skomplikowanymi mechanizmami bezpieczeństwa.

## Instalacja

Możesz zainstalować bibliotekę `keyring` za pomocą `pip`:

```bash
pip install keyring
```

## Przykład użycia
Poniżej znajduje się prosty przykład, jak używać biblioteki keyring:

```bash
import keyring

# Zapisanie hasła
service_name = "moja-aplikacja"
username = "użytkownik"
password = "tajne_hasło"

keyring.set_password(service_name, username, password)

# Odczytanie hasła
retrieved_password = keyring.get_password(service_name, username)
print(f"Odczytane hasło: {retrieved_password}")
```

## Składnia głównych komend używanych w bibliotece keyring.

1. keyring.set_password
```sh
keyring.set_password(service_name, username, password)
```
Opis:
Ta komenda zapisuje hasło dla danego użytkownika i usługi w bezpiecznym
magazynie haseł.

```sh
# service_name: Nazwa usługi, do której odnosi się hasło (np. "moja-aplikacja").
# username: Nazwa użytkownika, dla którego zapisywane jest hasło.
# password: Hasło, które ma być zapisane.

#Przykład:

keyring.set_password("moja-aplikacja", "użytkownik", "tajne_hasło")

# W tym przykładzie hasło "tajne_hasło" zostanie zapisane dla użytkownika "użytkownik" w kontekście usługi "moja-aplikacja".
```

2. keyring.get_password
```sh
keyring.get_password(service_name, username)
```

Opis:
Ta komenda pobiera hasło dla danego użytkownika i usługi z bezpiecznego magazynu haseł.

```sh
keyring.get_password(service_name, username)

# service_name: Nazwa usługi, do której odnosi się hasło (np. "moja-aplikacja").
# username: Nazwa użytkownika, dla którego pobierane jest hasło.

# Zwraca hasło jako string, jeśli istnieje dla podanego service_name
# i username. Jeśli hasło nie istnieje, zwraca None.

retrieved_password = keyring.get_password("moja-aplikacja", "użytkownik")
print(f"Odczytane hasło: {retrieved_password}")

# W tym przykładzie hasło zapisane dla użytkownika "użytkownik" w kontekście usługi "moja-aplikacja" zostanie pobrane i wyświetlone.
```

3. keyring.delete_password

```sh
keyring.delete_password(service_name, username)
```

Opis:
Ta komenda usuwa hasło dla danego użytkownika i usługi z bezpiecznego
magazynu haseł.

```sh
keyring.delete_password(service_name, username)

# service_name: Nazwa usługi, do której odnosi się hasło (np. "moja-aplikacja").
# username: Nazwa użytkownika, dla którego usuwane jest hasło.

keyring.delete_password("moja-aplikacja", "użytkownik")
# W tym przykładzie hasło zapisane dla użytkownika "użytkownik" w kontekście usługi "moja-aplikacja" zostanie usunięte.
```

4. keyring.get_keyring()

```sh
keyring.get_keyring()
```

Opis:
Ta komenda zwraca obecnie używany backend keyring (mechanizm przechowywania haseł).

```sh
keyring.get_keyring()

# Zwraca instancję aktualnie używanego keyring backend.

current_keyring = keyring.get_keyring()
print(f"Obecnie używany keyring: {current_keyring}")
W tym przykładzie zostanie wyświetlona informacja o aktualnie używanym mechanizmie przechowywania haseł.
```
