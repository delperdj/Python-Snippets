# JDD 12/2023
# Currency Conversion

import requests, sys, threading, time

# function for timer
def display_timer(stop_event):
    start_time = time.time()
    while not stop_event.is_set():
        elapsed_time = time.time() - start_time
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        formatted_time = f"\r\x1b[11;30;42m Waiting for response... {int(hours):02}:{int(minutes):02}:{int(seconds):02}\x1b[0m"
        print(formatted_time, end="")
        time.sleep(0.5)

# function to convert currency
def convert_currency(amount, from_currency, to_currency, api_key):
    stop_event = threading.Event()
    timer_thread = threading.Thread(target=display_timer, args=(stop_event,))
    timer_thread.start()

    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        headers = {'apikey': api_key}
        response = requests.get(url, headers=headers, timeout=10)
    except KeyboardInterrupt:
        stop_event.set()
        timer_thread.join()
        print("\nAPI call cancelled.")
        return None
    except requests.exceptions.Timeout:
        stop_event.set()
        timer_thread.join()
        print("\nAPI call timed out.")
        return None
    except requests.exceptions.RequestException as e:
        stop_event.set()
        timer_thread.join()
        print(f"\nAPI call failed: {e}")
        return None

    stop_event.set()
    timer_thread.join()

    if response.status_code != 200:
        print("\nError fetching exchange rate data.")
        return None
    data = response.json()
    rate = data['rates'].get(to_currency)
    
    if rate is None:
        print("\nConversion rate not found.")
        return None

    return amount * rate

def main():
    print("\nWelcome to the PyCurrency Conversion!")
    
    api_key = 'eb2e8e0dad533f4f953f18d1'  # API key from ExchangeRate-API
    
    if len(sys.argv) > 3:
        # if command line arugements exist, it will excute this
        amount = float(sys.argv[1])
        from_currency = sys.argv[2].upper()
        to_currency = sys.argv[3].upper()
    else:
        # ask for input for conversion
        amount = float(input("Enter the amount to be converted: \n"))
        from_currency = input("Enter the currency you are converting from (e.g., USD, EUR): \n").upper()
        to_currency = input("Enter the currency you are converting to (e.g., USD, EUR): \n").upper()

	# pass input to function for conversion
    converted_amount = convert_currency(amount, from_currency, to_currency, api_key)
    if converted_amount is not None:
        # show returned converated amount from function
        print(f"\r{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    else:
        print("\rConversion failed. Please check your input currencies.")

# main

if __name__ == "__main__":
    main()

# end
