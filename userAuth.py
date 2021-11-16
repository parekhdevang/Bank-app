import click
import time

master_pin = 1234


@click.command()
def auth():
    """Authenticate the user."""
    count = 0
    while True:
        if count >= 3:
            print("Excceeded the number of tries. Wait for 30s")
            time.sleep(30)
            count = 0

        try:
            temp_pin = int(input("Please enter your pin: "))
            if temp_pin != master_pin:
                print("Wrong pin, please try again.")
                count += 1
            elif temp_pin == master_pin:
                print("Welcome to the jungle!")
                break
        except:
            count += 1
            pass

if __name__ == '__main__':
    auth()
