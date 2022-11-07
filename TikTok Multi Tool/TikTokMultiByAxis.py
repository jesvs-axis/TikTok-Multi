from selenium import webdriver
from os import system, name
import chromedriver_binary
from time import time, strftime, gmtime, sleep
import pyfiglet, os, threading
import chromedriver_autoinstaller

# Check if the current version of chromedriver exists
# and if it doesn't exist, download it automatically,
# then add chromedriver to path
chromedriver_autoinstaller.install()

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear()
system('title Axis Multi-Tool')

print(pyfiglet.figlet_format("Axis Multi-Tool", font="slant"))
print("1. Viewbot.\n2. Heartbot.\n3. Followerbot.\n3. Sharebot.\n4. ReportVideo.\n5. Credits.\n")

auto = int(input("Mode: "))


if auto == 1 or auto == 2 or auto == 3:
    vidUrl = input("TikTok video URL (copy the url from chrome not from copy url tiktok feature): ")

    start = time()
    time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome( options=chrome_options)
    driver.set_window_size(1024, 650)

    Views = 0
    Hearts = 0
    Followers = 0

def beautify(arg):
    return format(arg, ',d').replace(',', '.')

def title1(): # Update the title IF option 1 was picked.
    global Views
    
    while True:
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        system(f'title Axis Multi-Tool ^| Views Sent: {beautify(Views)} ^| Elapsed Time: {time_elapsed}')

def title2(): # Update the title IF option 2 was picked.
    global Hearts
    
    while True:
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        system(f'title Axis Multi-Tool ^| Hearts Sent: {beautify(Hearts)} ^| Elapsed Time: {time_elapsed}')

def title3(): # Update the title IF option 3 was picked.
    global Followers
    
    while True:
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        system(f'title Axis Multi-Tool ^| Followers Sent: {beautify(Followers)} ^| Elapsed Time: {time_elapsed}')
        
def title4(): # Update the title IF option 1 was picked.
    global Shares
    
    while True:
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        system(f'title Axis Multi-Tool ^| Shares Sent: {beautify(Shares)} ^| Elapsed Time: {time_elapsed}')

    
def loop1():
    global Views
    sleep(10)
    
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button").click()
        
    except:
        print("[-] The captcha is unsolved!")
        driver.refresh()
        loop1()
        
    try:
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/form/div/input").send_keys(vidUrl)
        
        sleep(1)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/form/div/div/button").click()
        
        sleep(5)
        driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9V\"]/div[1]/div/form/button").click()
        
        driver.refresh()
        Views += 1000
        print("[+] Views sended!")
        
        sleep(300)
        loop1()
        
    except:
        print("[-] An error occured. Retrying..") 
        driver.refresh()
        loop1()

def loop2():
    global Hearts
    sleep(10)
    
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[2]/div/button").click()
        
    except:
        print("[-] The captcha is unsolved!")
        driver.refresh()
        loop2()
        
    try:
        sleep(2)
        driver.find_element_by_xpath('//*[@id="sid2"]/div/form/div/input').send_keys(vidUrl)
        
        sleep(1)
        driver.find_element_by_xpath('//*[@id="sid2"]/div/form/div/div/button').click()
        
        sleep(5)
        driver.find_element_by_xpath('//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/button').click()
        
        sleep(6)
        hearts = driver.find_element_by_xpath('//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/span').text.split()
        
        Hearts += int(hearts[0])
        print("[+] Hearts sended!")
        
        sleep(5)
        driver.refresh()
        
        sleep(1800)
        loop2()
        
    except:
        print("[-] An error occured. Retrying..") 
        driver.refresh()
        loop2()

def loop3():
    global Followers
    sleep(10)
    
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[1]/div/button").click()
        
    except:
        print("[-] The captcha is unsolved!")
        driver.refresh()
        loop3()
        
    try:
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"sid\"]/div/form/div/input").send_keys(vidUrl)
        
        sleep(1)
        driver.find_element_by_xpath("//*[@id=\"sid\"]/div/form/div/div/button").click()
        
        sleep(5)
        driver.find_element_by_xpath("//*[@id=\"c2VuZF9mb2xsb3dlcnNfdGlrdG9r\"]/div[1]/div/form/button").click()
        sleep(6)
        folls = driver.find_element_by_xpath('//*[@id="c2VuZF9mb2xsb3dlcnNfdGlrdG9r"]/span').text.split()
        
        Followers += int(folls[0])
        print("[+] Followers sended!")
        driver.refresh()
        
        sleep(1800)
        loop3()
        
    except:
        print("[-] An error occured. Retrying..")
        driver.refresh()
        loop3()

def loop4():
    global Shares
    sleep(10)
    
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[5]/div/button").click()
        
    except:
        print("[-] The captcha is unsolved!")
        driver.refresh()
        loop4()
        
    try:
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"sid7\"]/div/form/div/input").send_keys(vidUrl)
        
        sleep(1)
        driver.find_element_by_xpath("//*[@id=\"sid7\"]/div/form/div/div/button").click()
        
        sleep(5)
        driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9s\"]/div[1]/div/form/button").click()
        
        driver.refresh()
        Shares += 100
        print("[+] Shares sended!")
        
        sleep(300)
        loop4()
        
    except:
        print("[-] An error occured. Retrying..")
        driver.refresh()
        loop4()

clear()

print(pyfiglet.figlet_format("Tiktok Multi-Tool", font="slant"))
print("Log:")

if auto == 1:
    driver.get("https://zefoy.com/")
    
    a = threading.Thread(target=title1)
    b = threading.Thread(target=loop1)
    
    a.start()
    b.start()
    
elif auto == 2:
    driver.get("https://zefoy.com/")
    
    a = threading.Thread(target=title2)
    b = threading.Thread(target=loop2)
    
    a.start()
    b.start()
    
elif auto == 3:
    driver.get("https://zefoy.com/")
    
    a = threading.Thread(target=title3)
    b = threading.Thread(target=loop3)
    
    a.start()
    b.start()
    
elif auto == 4:
    from requests import request
from pystyle import Colorate, Colors, Center
from os import system
from threading import Thread
from json import loads
from re import findall

report_video = 0
report_user = 0


def user_info(username: str) -> dict:
    html_data = request(
        "GET", f"https://livecounts.io/tiktok-live-follower-counter/{username}"
    ).text
    parsed_info = loads(findall(r'n">(.*)<\/s', html_data)[0])

    return parsed_info["props"]["pageProps"]["data"]


def status(report_video, report_user):
    print(
        Colorate.Horizontal(
            Colors.blue_to_cyan,
            "[i] User Report(s): {} | Video Report(s): {}".format(
                report_user, report_video
            ),
        ),
        end="\r",
    )


def report(id, aweme_id, sessionid):
    global report_video

    url = "https://api31-normal-useast1a.tiktokv.com/aweme/v1/aweme/feedback/?request_tag_from=h5&reason=111&owner_id={}&report_type=video&object_id={}&report_desc=%EF%BF%BDUser%20violates%20community%20guidelines%20on%20multiple%20occasions%20by%20spreading%20illegal%20activities%2Fscams%20and%20by%20insulting%2Fharassing%20people%20please%20remove%20this%20content!%20(Offending%20content%20in%20video%20and%20caption)%EF%BF%BD&aid=1180".format(
        id, aweme_id
    )

    headers = {
        "accept-encoding": "gzip",
        "sdk-version": "2",
        "cookie": "sessionid={}".format(sessionid),
        "user-agent": "com.ss.android.ugc.trill/240303 (Linux; U; Android 12; en_US; Pixel 6 Pro; Build/SP2A.220405.004;tt-ok/3.10.0.2)",
    }

    while True:
        try:
            request("GET", url, headers=headers)

            report_video += 1

            status(report_video, report_user)
        except Exception:
            continue
        break


def banner():
    system("cls")
    print(
        Colorate.Horizontal(
            Colors.blue_to_cyan,
            Center.XCenter(
                """
                 _     _____                       _   
     /\         (_)   |  __ \                     | |  
    /  \   __  ___ ___| |__) |___ _ __   ___  _ __| |_ 
   / /\ \  \ \/ / / __|  _  // _ \ '_ \ / _ \| '__| __|
  / ____ \  >  <| \__ \ | \ \  __/ |_) | (_) | |  | |_ 
 /_/    \_\/_/\_\_|___/_|  \_\___| .__/ \___/|_|   \__|
                                 | |                   
                                 |_|                                                                 
                """
            ),
        )
    )


if __name__ == "__main__":
    banner()

    sessionid = input(Colorate.Horizontal(Colors.blue_to_cyan, "[?] Session ID >>> "))

    banner()

    username = input(Colorate.Horizontal(Colors.blue_to_cyan, "[?] Username >>> "))
    id = user_info(username)["userId"]

    banner()

    print(Colorate.Horizontal(Colors.blue_to_cyan, "[i] Please wait..."), end="\r")

    url = "https://api31-normal-useast1a.tiktokv.com/aweme/v1/aweme/feedback/?request_tag_from=h5&reason=311&owner_id={}&report_type=user&object_id={}&report_desc=%EF%BF%BDUser%20violates%20community%20guidelines%20on%20multiple%20occasions%20by%20spreading%20illegal%20activities%2Fscams%20and%20by%20insulting%2Fharassing%20people%20please%20remove%20this%20content!%20(Offending%20content%20in%20video%20and%20caption)%EF%BF%BD&aid=1180".format(
        id, id
    )

    headers = {
        "accept-encoding": "gzip",
        "sdk-version": "2",
        "cookie": "sessionid={}".format(sessionid),
        "user-agent": "com.ss.android.ugc.trill/240303 (Linux; U; Android 12; en_US; Pixel 6 Pro; Build/SP2A.220405.004;tt-ok/3.10.0.2)",
    }

    request("GET", url, headers=headers)

    report_user += 1

    status(report_video, report_user)
    while True:
        max_cursor = 0

        while True:
            url = "https://api2-19-h2.musical.ly/aweme/v1/aweme/post/?max_cursor={}&user_id={}&count=200&retry_type=no_retry&mcc_mnc=&app_language=en&language=en&region=US&sys_region=US&carrier_region=&carrier_region_v2=&build_number=10.1.7&timezone_offset=3600&timezone_name=Europe%2FBerlin&is_my_cn=0&fp=&pass-region=1&pass-route=1&iid=7127307272354596614&device_id=7083579838678386182&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=100107&version_name=10.1.7&device_platform=android&ab_version=10.1.7&ssmix=a&device_type=Pixel%2B6%2BPro&device_brand=google&os_api=30&os_version=12&openudid=fe44d963d8b2c849&manifest_version_code=2019021215&resolution=1080*2268&dpi=443&update_version_code=2019021215&_rticket=1659461968895&ts=1659461970&as=a1iosdfgh&cp=androide1".format(
                max_cursor, id
            )

            headers = {
                "Host": "api2-19-h2.musical.ly",
                "Connection": "keep-alive",
                "Accept-Encoding": "gzip",
                "cookie": "sessionid={}".format(sessionid),
                "sdk-version": "1",
                "User-Agent": "com.zhiliaoapp.musically/2019021215 (Linux; U; Android 12; en_US; Pixel 6 Pro; Build/SP2A.220405.004; Cronet/58.0.2991.0)",
            }

            response = request("GET", url, headers=headers).json()

            try:
                if response["status_msg"] == "No more videos":
                    break
            except Exception:
                try:
                    max_cursor = response["max_cursor"]
                except Exception:
                    break

            aweme_list = response["aweme_list"]

            for aweme in aweme_list:
                Thread(
                    target=report,
                    args=(
                        id,
                        aweme["aweme_id"],
                        sessionid,
                    ),
                ).start()
    
elif auto == 5:
    print("This program was created by @Axis.fn. [github.com/jesvs-axis]")
    print("If you notice any errors write me on Telegram: Sonurus")

else:
    print(f"{auto} is not a valid option. Please pick 1, 2, 3 or 4")
