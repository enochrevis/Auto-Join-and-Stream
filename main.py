import pyautogui

pyautogui.PAUSE = 1

def click_picture(picture):
    pictureX, pictureY = pyautogui.locateCenterOnScreen(picture)
    pyautogui.click(pictureX, pictureY)

while True:
    try:
        pyautogui.locateOnScreen('streaming.png')
        print("Currently streaming")
    except:
        print("Currently not streaming, joining voice chat...")

        try:
            click_picture('secret-test-channel.png')

            click_picture('stream-icon.png')

            click_picture('go-live-button.png')

            click_picture('grant-access-button.png')
            
        except:
            print("Failed to click picture, retrying...")

