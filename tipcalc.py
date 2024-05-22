class TipCalculator:
    def __init__(self, bill_amount, tip_percentage):
        self.__bill_amount = bill_amount
        self.__tip_percentage = tip_percentage

    def __calculate_tip(self):
        tip_amount = self.__bill_amount * (self.__tip_percentage / 100)
        total_amount = self.__bill_amount + tip_amount
        return tip_amount, total_amount

    def calculate_and_display_tip(self):
        tip_amount, total_amount = self.__calculate_tip()
        print(f"\nTip amount: ${tip_amount:.2f}")
        print(f"Total amount (including tip): ${total_amount:.2f}")

def main():
    try:
        bill_amount = float(input("Enter the total bill amount: $"))
        tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): "))

        calculator = TipCalculator(bill_amount, tip_percentage)
        calculator.calculate_and_display_tip()

    except ValueError:
        print("Please enter valid numeric values.")

main()

a=10
b=67
a=a+b
b=a-b
a=a-b
print(a,b)

