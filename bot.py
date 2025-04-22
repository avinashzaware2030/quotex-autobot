from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from strategy import calculate_indicators, generate_signal
import pandas as pd

# ===== CONFIG =====
EMAIL = "तुझं_quotex_email"
PASSWORD = "तुझं_quotex_password"
TRADE_AMOUNT = 70
TRADE_TIMEFRAME = "5"  # 5 minute
PAIR = "EUR/USD"
# ===================

def setup_driver():
    options = Options()
    options.add_argument("--headless")  # GUI नको असल्यास headless ठेवा
    driver = webdriver.Chrome(options=options)
    return driver

def login_quotex(driver):
    driver.get("https://quotex.io/en/sign-in")
    sleep(3)
    driver.find_element(By.NAME, "email").send_keys(EMAIL)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.TAG_NAME, "button").click()
    sleep(5)

def get_fake_data():  # इथे आपल्याला Quotex API असेल तर त्याचं वापर करायचं
    # Placeholder candle data
    data = {
        'Close': [1.2, 1.21, 1.22, 1.25, 1.24, 1.26, 1.28, 1.27, 1.3, 1.32, 1.35, 1.34]
    }
    return pd.DataFrame(data)

def place_trade(driver, action):
    if action == "BUY":
        print("Placing BUY trade...")
        # driver.find_element(By.ID, "buy-button").click()
    elif action == "SELL":
        print("Placing SELL trade...")
        # driver.find_element(By.ID, "sell-button").click()
    else:
        print("No valid signal.")

def main():
    df = get_fake_data()
    df = calculate_indicators(df)
    signal = generate_signal(df)
    print("Signal:", signal)

    driver = setup_driver()
    login_quotex(driver)
    place_trade(driver, signal)
    driver.quit()

if __name__ == "__main__":
    main()
