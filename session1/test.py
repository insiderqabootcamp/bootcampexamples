from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.useinsider.com")

current_url = driver.current_url

if "google.com" in current_url:
    print("Test Başarılı: Google ana sayfasına gidildi!")
else:
    print(f"Test Başarısız: Beklenen URL 'google.com', Ancak Alınan URL '{current_url}'")

driver.quit()