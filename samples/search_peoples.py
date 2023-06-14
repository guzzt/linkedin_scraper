from linkedin_scraper import Person, actions
import undetected_chromedriver as uc
from time import sleep

driver = uc.Chrome()
# sleep(60)
actions.login(driver, "email","passw")
sleep(10)
actions.save_cookies(driver)
person = Person('https://www.linkedin.com/in/andre-iguodala-65b48ab5',driver=driver)
print(person)
exit(0)
for i in range(1,101):
	links = actions.search_peoples(driver, "medico", page=i)
	for l in links:
		if 'https://www.linkedin.com/in/' in l:
			driver.get(l)
			sleep(5)
			true_link = driver.current_url
			print(true_link)
			try:
				person = Person(true_link,driver=driver)
				print(person)
			except Exception as e:
				print(str(e))
