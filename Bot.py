from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests

# Telegram API details
TELEGRAM_API_KEY = "7703010489:AAF_Z5zxHfgEuzYqAgzDZun5obG39fE1p8Q"
CHAT_IDS = ["2011774729","7520300427"]  # Replace with your chat IDs //7520300427-> client

# Websites to monitor
WEBSITES = ["https://tracksino.com/crazytime", "https://tracksino.com/crazytime-a"]

# JavaScript paths to monitor
JS_PATH_RESULT = "#spin-history > tbody > tr:nth-child(1) > td:nth-child(3) > center > i"
JS_PATH_INSTANCE = "#spin-history > tbody > tr:nth-child(1) > td:nth-child(1)"

# Class names to check against
CLASS_NAME_MAPPING = {
    "ico-crazytime-cf": "CoinFlip",
    "ico-crazytime-ch": "CashHunt",
    "ico-crazytime-pa": "Pachinko",
    "ico-crazytime-ct": "CrazyTime"
}

# Store last instance per game to avoid duplicate messages
last_instances = {}

def send_telegram_message(message):
    """Send a message to multiple Telegram chat IDs."""
    url = f"https://api.telegram.org/bot{TELEGRAM_API_KEY}/sendMessage"
    for chat_id in CHAT_IDS:
        payload = {
            "chat_id": chat_id,
            "text": message
        }
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print(f"Message sent successfully to chat ID {chat_id}.")
        else:
            print(f"Failed to send message to chat ID {chat_id}: {response.status_code}, {response.text}")

def monitor_website(url):
    """Monitor the given website and check for game results and instance changes."""
    driver.get(url)
    time.sleep(1)  # Allow time for the page to load
    
    try:
        # Get the game result
        result_element = driver.find_element(By.CSS_SELECTOR, JS_PATH_RESULT)
        class_name = result_element.get_attribute("class").strip()
        game_result = CLASS_NAME_MAPPING.get(class_name, "Unknown")
        
        # Get the instance value
        instance_element = driver.find_element(By.CSS_SELECTOR, JS_PATH_INSTANCE)
        instance_value = instance_element.text.strip()
        
        # Determine the game name
        game_name = "CrazyTimeA" if "crazytime-a" in url else "CrazyTime"
        unique_key = f"{game_name}:{url}"
        
        print(f"Website: {url}, Game: {game_name}, Result: {game_result}, Instance: {instance_value}")
        
        # Only proceed if the game result is in the target classes
        if game_result != "Unknown" and last_instances.get(unique_key) != instance_value:
            last_instances[unique_key] = instance_value
            message = (
                f"Game: {game_name},\n"
                f"Spin Result: {game_result},\n"
                f"Instance: {instance_value}"
            )
            send_telegram_message(message)
    except Exception as e:
        print(f"Error monitoring {url}: {e}")

# Configure WebDriver for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.binary_location = "/home/render/chrome/opt/google/chrome/google-chrome"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    while True:
        for website in WEBSITES:
            monitor_website(website)
        time.sleep(1)  # Wait before checking again
finally:
    driver.quit()
