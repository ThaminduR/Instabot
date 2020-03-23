from time import sleep
import datetime
import data
import traceback
import random


def login(webdriver):

    # Open the instagram page
    webdriver.get(
        'https://www.instagram.com/accounts/login/?source=auth_switcher')

    sleep(4)

    # Find username and password fields and set their input using our constants
    username = webdriver.find_element_by_name('username')
    username.send_keys(data.INST_USER)
    password = webdriver.find_element_by_name('password')
    password.send_keys(data.INST_PASS)

    # Get the login button
    try:
        button_login = webdriver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button')
    except:
        button_login = webdriver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[6]/button/div')

    sleep(2)

    button_login.click()

    sleep(3)

    # if a popup occurs after logging in, press not now.
    try:
        notnow = webdriver.find_element_by_css_selector(
            'body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
        notnow.click()
    except:
        return


def follow_people(webdriver):

    # a list to store newly followed users
    new_followed = []

    # counters
    followed = 0
    likes = 0

    # Iterate theough all the hashtags
    for hashtag in data.HASHTAGS:

        # Visit the hashtag
        webdriver.get(
            'https://www.instagram.com/explore/tags/' + hashtag + '/')

        sleep(5)

        # Get the first post
        first_thumbnail = webdriver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
        first_thumbnail.click()
        sleep(random.randint(1, 3))

        print(hashtag)
        
        try:
            # iterate the first 100 posts
            for x in range(1, 100):

                t_start = datetime.datetime.now()

                sleep(2)

                # Get the poster's username
                username = webdriver.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/a').text

                try:
                    print("Detected: {0}".format(username))

                    # Don't press the button if the text doesn't say follow
                    if webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':

                        # Click follow
                        webdriver.find_element_by_xpath(
                            '/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                        followed += 1

                        print("Followed: {0}".format(
                            username))
                        new_followed.append(username)

                        # like the picture
                        button_like = webdriver.find_element_by_xpath(
                            '/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
                        button_like.click()
                        likes += 1

                        print("Liked {0}'s post".format(username))
                        sleep(random.randint(5, 15))

                    # Next picture
                    webdriver.find_element_by_link_text('Next').click()
                    sleep(random.randint(15, 25))

                except:
                    traceback.print_exc()
                    continue

                t_end = datetime.datetime.now()
                t_elapsed = t_end - t_start

                print("This iteration took {0} seconds".format(
                    t_elapsed.total_seconds()))

        except:
            traceback.print_exc()
            continue
        print("First hashtag iteration complete !")
        print('Liked {} photos.'.format(likes))
        print('Followed {} new people.'.format(followed))
