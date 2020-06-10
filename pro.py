import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Please Eat n Drink Something ",
            message="Eating and drinking well is fundamental to good health and well-being. Healthy eating and drinking helps us to maintain",
            timeout=10

        )
    time.sleep(30)
