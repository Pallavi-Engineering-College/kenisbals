def main():
    # Exchange rates
    USD_TO_EUR = 0.85
    USD_TO_GBP = 0.74
    USD_TO_INR = 82.50

    # Display welcome message
    print("Welcome to the Currency Converter!")

    try:
        usd_amount = float(input("Enter the amount in USD: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    # Calculate equivalent amounts
    eur_amount = usd_amount * USD_TO_EUR
    gbp_amount = usd_amount * USD_TO_GBP
    inr_amount = usd_amount * USD_TO_INR

    # Display results
    print(f"\nAmount in EUR: {eur_amount:.1f} EUR")
    print(f"Amount in GBP: {gbp_amount:.1f} GBP")
    print(f"Amount in INR: {inr_amount:.1f} INR")

    # Show thank you message
    print("\nThank you for using the Currency Converter!")

if __name__ == "__main__":
    main()
