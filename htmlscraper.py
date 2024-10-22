import requests

r1 = input(f"Please provide the url and page (ex: http://google.com/index.html): ")

r = requests.get(r1)

web_headers = r.headers
print("Here are the headers returned")
print(web_headers)

web_html = r.text
print("Here is the html returned in the body of the webpage")
print(web_html)

web_status_code = r.status_code
print("Here is the HTTP status code returned")
print (web_status_code)

web_cookies = r.cookies
print("Here are the cookies returned from the page")
print(web_cookies)
