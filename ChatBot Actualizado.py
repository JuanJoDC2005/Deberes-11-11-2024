from BankLibrary import BankAccount

# Clase hija para la cuenta de ahorros


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"¡Interés aplicado con éxito! El interés generado es de {interest:.2f}. Nuevo saldo: {self.balance:.2f}"

    def estimate_interest(self, months):
        estimated_interest = self.balance * self.interest_rate * months
        return f"Si dejas tu saldo intacto durante {months} meses, generarías un interés de {estimated_interest:.2f}."

# Clase hija para la cuenta corriente


class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance=0, overdraft_limit=500):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            return f"Has retirado {amount:.2f}. Nuevo saldo: {self.balance:.2f}"
        else:
            return f"No puedes retirar {amount:.2f}. Supera el límite de sobregiro."

    def set_overdraft_limit(self, new_limit):
        self.overdraft_limit = new_limit
        return f"El límite de sobregiro ha sido actualizado a {self.overdraft_limit:.2f}."

# Función principal del chatbot


def chatbot():
    print("¡Hola y bienvenido al Chatbot del Banco!")

    account_type = input(
        "¿Qué tipo de cuenta deseas abrir? ('ahorros' o 'corriente'): ").lower()

    if account_type == "ahorros":
        account_number = input(
            "Introduce un número de cuenta único para tu nueva cuenta de ahorros: ")
        account = SavingsAccount(account_number)
        print(f"Tu cuenta de ahorros ha sido creada con éxito. Número de cuenta: {
              account.account_number}")
    elif account_type == "corriente":
        account_number = input(
            "Introduce un número de cuenta único para tu nueva cuenta corriente: ")
        account = CheckingAccount(account_number)
        print(f"Tu cuenta corriente ha sido creada con éxito. Número de cuenta: {
              account.account_number}")
    else:
        print("No entendí lo que dijiste. Por favor, escoge entre 'ahorros' o 'corriente'.")
        return

    # Ciclo principal del chatbot
    while True:
        print("\nOpciones: 'depositar', 'retirar', 'saldo', 'aplicar_interes', 'estimar_interes', 'establecer_limite_sobregiro', 'salir'")
        action = input("¿Qué te gustaría hacer ahora? ").lower()

        if action == 'depositar':
            amount = float(input("¿Cuánto deseas depositar? "))
            print(account.deposit(amount))

        elif action == 'retirar':
            amount = float(input("¿Cuánto deseas retirar? "))
            print(account.withdraw(amount))

        elif action == 'saldo':
            print(f"Tu saldo actual es: {account.get_balance():.2f}")

        elif action == 'aplicar_interes' and isinstance(account, SavingsAccount):
            print(account.apply_interest())

        elif action == 'estimar_interes' and isinstance(account, SavingsAccount):
            months = int(
                input("¿Cuántos meses te gustaría estimar para el interés? "))
            print(account.estimate_interest(months))

        elif action == 'establecer_limite_sobregiro' and isinstance(account, CheckingAccount):
            new_limit = float(
                input("Introduce el nuevo límite de sobregiro: "))
            print(account.set_overdraft_limit(new_limit))

        elif action == 'salir':
            print("Gracias por usar el Chatbot del Banco. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor elige entre 'depositar', 'retirar', 'saldo', 'aplicar_interes', 'estimar_interes', 'establecer_limite_sobregiro' o 'salir'.")


# Ejecutar el chatbot
if __name__ == "__main__":
    chatbot()
