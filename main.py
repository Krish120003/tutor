import ollama
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Set up Chrome driver
driver = webdriver.Chrome()


driver.get("https://excalidraw.com/")

# Wait for the page to load (waiting for canvas element)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "canvas")))

# Give some time for the page to fully render
time.sleep(2)

images = []
client = ollama.Client(
    host="http://100.110.46.126:5001",
)

i = 0
while True:
    input("Enter to continue...")

    # Take screenshot
    screenshot_name = f"excalidraw_screenshot_{i}.png"
    driver.save_screenshot(screenshot_name)
    images.append(screenshot_name)
    print("Screenshot saved successfully!")
    i += 1

    image_prompt = [
        {
            "role": "user",
            "content": "This is a screenshot of the workspace canvas.",
            "images": [img],
        }
        for img in images
    ]

    response = client.chat(
        model="llama3.2-vision",
        messages=[
            {
                "role": "user",
                "content": "You are watching screenhots of a canvas. Your goal is to be an AI tutor and teach students some concepts. The screenshots showcase the student's work in progress. Watch their work, and give them advice as needed. However, only nudge them in the right direction, don't give them the full answer.",
            },
            *image_prompt,
            {
                "role": "user",
                "content": "What advice would you give to the student right now?",
            },
        ],
    )

    print(response)
