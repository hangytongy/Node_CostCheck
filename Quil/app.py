import time
import main
import plotting
from datetime import datetime
from telegram_push import send_photo_telegram

if __name__ == "__main__":
    while True:
        now = datetime.now().strftime("%Y-%m-%d")
        print(f"running script for date {now}")
        main.run_script()
        print("Data Saved")
        time.sleep(5)
        file = plotting.plot_df()
        print("plotted")

        if file == None:
            pass
        else:
            send_photo_telegram(file,f"Quil Mining Profitability updated {now}")
        time.sleep(60)
