import tkinter as tk
from tkinter import ttk

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("500x500")
        self.root.config(bg="#f0f8ff")  # Light blue background

        # Predefined exchange rates (relative to 1 USD)
        self.exchange_rates = {
            "USD": 1.0,
            "EUR": 0.93,
            "INR": 82.5,
            "GBP": 0.78,
            "AUD": 1.45,
            "CAD": 1.36,
            "SGD": 1.35,
            "JPY": 143.5,
            "CNY": 7.28,
            "NZD": 1.60
        }

        # Currency Options
        self.currencies = list(self.exchange_rates.keys())

        # Title Label
        self.title_label = tk.Label(
            self.root, text="Currency Converter", font=("Helvetica", 20, "bold"),
            bg="#4682b4", fg="white", padx=10, pady=10
        )
        self.title_label.pack(fill=tk.X)

        # Input Frame
        self.input_frame = tk.Frame(self.root, bg="#f0f8ff", pady=20)
        self.input_frame.pack(fill=tk.BOTH, expand=True)

        # From Currency
        self.from_currency_label = tk.Label(
            self.input_frame, text="From Currency:", font=("Helvetica", 14), bg="#f0f8ff"
        )
        self.from_currency_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.from_currency_combo = ttk.Combobox(
            self.input_frame, values=self.currencies, state="readonly", font=("Helvetica", 12)
        )
        self.from_currency_combo.grid(row=0, column=1, padx=10, pady=10)
        self.from_currency_combo.set("USD")

        # To Currency
        self.to_currency_label = tk.Label(
            self.input_frame, text="To Currency:", font=("Helvetica", 14), bg="#f0f8ff"
        )
        self.to_currency_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.to_currency_combo = ttk.Combobox(
            self.input_frame, values=self.currencies, state="readonly", font=("Helvetica", 12)
        )
        self.to_currency_combo.grid(row=1, column=1, padx=10, pady=10)
        self.to_currency_combo.set("INR")

        # Amount
        self.amount_label = tk.Label(
            self.input_frame, text="Amount:", font=("Helvetica", 14), bg="#f0f8ff"
        )
        self.amount_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        self.amount_entry = ttk.Entry(self.input_frame, font=("Helvetica", 12))
        self.amount_entry.grid(row=2, column=1, padx=10, pady=10)

        # Convert Button
        self.convert_button = tk.Button(
            self.input_frame, text="Convert", font=("Helvetica", 14, "bold"),
            bg="#4682b4", fg="white", padx=10, pady=5, command=self.convert_currency
        )
        self.convert_button.grid(row=3, columnspan=2, pady=20)

        # Result
        self.result_label = tk.Label(
            self.root, text="", font=("Helvetica", 16, "bold"), bg="#f0f8ff", fg="#333333"
        )
        self.result_label.pack(pady=10)

    def convert_currency(self):
        try:
            from_currency = self.from_currency_combo.get()
            to_currency = self.to_currency_combo.get()
            
            amount_text = self.amount_entry.get().strip()
            if not amount_text:
                raise ValueError("Amount cannot be empty.")
            
            amount = float(amount_text)
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
            
            # Calculate conversion
            from_rate = self.exchange_rates[from_currency]
            to_rate = self.exchange_rates[to_currency]
            result = (amount / from_rate) * to_rate

            self.result_label.config(
                text=f"{amount} {from_currency} = {result:.2f} {to_currency}", fg="green"
            )
        except ValueError as e:
            self.result_label.config(text=f"Invalid input: {e}", fg="red")
        except KeyError:
            self.result_label.config(text="Selected currency is not available.", fg="red")
        except Exception as e:
            self.result_label.config(text=f"Error: {e}", fg="red")

# Main Function
if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
