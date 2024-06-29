from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

# Capabilities options for Chrome (Opsi capabilities untuk Chrome)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-gpu")  # Added option to turn off GPU (Menambahkan opsi untuk mematikan GPU)

# Function to fill out the form (Fungsi untuk mengisi form)
def fill_form(name, email):
    driver = webdriver.Chrome(options=chrome_options)
    form_url = "ENTER YOUR LINK GOOGLE FORM" # Fill in your Google From link (Isikan link Google From Anda)

    try:
        driver.get(form_url)
        wait = WebDriverWait(driver, 10)

        # Fill in the email (Isi email)
        email_field = wait.until(EC.element_to_be_clickable((By.XPATH, 'ENTER YOUR EXISTING EMAIL TEXT IN CHROME INSPECTOR'))) # Take the XPATH from the Input Text Email inspect in the Inspector in Chrome (Ambil XPATH dari inspect Input Text Email pada Inspector yang ada di Chrome)
        email_field.send_keys(email)

        # Fill in the name (Isi nama)
        name_field = wait.until(EC.element_to_be_clickable((By.XPATH, 'ENTER YOUR EXISTING NAME TEXT IN CHROME INSPECTOR'))) # Take the XPATH from inspect Input Text Name in the Inspector in Chrome (Ambil XPATH dari inspect Input Text Nama pada Inspector yang ada di Chrome)
        name_field.send_keys(name)

        # Choose a random answer for each multiple choice question (Pilih jawaban acak untuk setiap pertanyaan pilihan ganda)
        for i in range(1, 21):  # Change the number of questions as needed (Ubah jumlah pertanyaan sesuai kebutuhan)
            question_xpath = f'(//div[@role="radiogroup"])[{i}]//div[@role="radio"]'
            options = wait.until(EC.presence_of_all_elements_located((By.XPATH, question_xpath)))
            random.choice(options).click()

        # Click the submit button (Klik tombol submit)
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '')))
        submit_button.click()

        # Wait a few seconds before closing the browser (Tunggu beberapa detik sebelum menutup browser)
        time.sleep(3)

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

    finally:
        driver.quit()

# Name and email to be used [adjust to number of respondents] (Nama dan email yang akan digunakan [sesuaikan dengan jumlah responden])
emails = ["audyagam@students.amikom.ac.id", "rendraaditya@students.amikom.ac.id", "edgardzakielvanuar@students.amikom.ac.id"]
names = ["Audy Agam Raisan", "Rendra Aditya", "Edgard Zaki Elvanuar"]

# Repeat filling in the form to the last data (Mengulang pengisian form sampai ke data terakhir)
for i in range(len(names)):
    fill_form(names[i], emails[i])
