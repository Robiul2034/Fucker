from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Sample data for multiple accounts
names = ["Fucked", "Fucker", "Account Fuck"]
emails = ["fuck@mail.com", "fuck@email.com", "fuck@maill.com"]
passwords = ["password123", "password123", "password123"]
mobile_numbers = ["1234567890", "0987654321", "1122334455"]

# Path to ChromeDriver
driver_path = "/path/to/chromedriver"

# URL for account creation page
url = "https://vut26itsolution.xyz/register.php"  # Replace with your test URL

# Initialize the browser
driver = webdriver.Chrome(driver_path)
driver.get(url)

try:
    # Loop to create accounts, simulating up to 1000 submissions
    for i in range(1000):
        # Use sample data in a round-robin fashion
        name = names[i % len(names)]
        email = f"test_user{i}@example.com"  # Ensure unique emails
        password = passwords[i % len(passwords)]
        mobile = mobile_numbers[i % len(mobile_numbers)]

        # Fill in the name
        name_field = driver.find_element(By.ID, "name_field_id")  # Replace with actual field ID
        name_field.clear()
        name_field.send_keys(name)

        # Fill in the email
        email_field = driver.find_element(By.ID, "email_field_id")  # Replace with actual field ID
        email_field.clear()
        email_field.send_keys(email)

        # Fill in the password
        password_field = driver.find_element(By.ID, "password_field_id")  # Replace with actual field ID
        password_field.clear()
        password_field.send_keys(password)

        # Fill in the mobile number
        mobile_field = driver.find_element(By.ID, "mobile_field_id")  # Replace with actual field ID
        mobile_field.clear()
        mobile_field.send_keys(mobile)

        # Submit the form
        submit_button = driver.find_element(By.ID, "submit_button_id")  # Replace with actual button ID
        submit_button.click()

        # Wait for a short duration between each submission
        time.sleep(1)  # Adjust time as necessary

        # Return to the form page for the next submission
        driver.get(url)

    print("Account creation simulation completed.")
finally:
    driver.quit()
