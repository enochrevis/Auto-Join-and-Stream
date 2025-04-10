import pyautogui

pyautogui.PAUSE = 1

def click_picture(picture):
    pictureX, pictureY = pyautogui.locateCenterOnScreen(picture)
    pyautogui.click(pictureX, pictureY)

def begin_streaming():
        try:
            click_picture('stream-icon.png')
            click_picture('go-live-button.png')
            click_picture('grant-access-button.png')
        except:
            print("Failed to start stream.")

def check_channel_capacity(channel):
    try:
        pyautogui.locateOnScreen(channel)
        return 1
    except:
        return 0

while True:
    try:
        pyautogui.locateOnScreen('streaming.png')
        print("Currently streaming")

    except:
        print("Currently not streaming, check to see if already in voice chat...")

        try:
            pyautogui.locateOnScreen('not-streaming.png')
            print("Currently in voice chat, starting stream...")
            begin_streaming()
        
        except:
            print("Currently not in voice chat, joining...")

            try:
                activeChannels = check_channel_capacity('albedo-vator-channel-capacity-0.png') << 2
                activeChannels += check_channel_capacity('wanmin-restaurant-channel-capacity-0.png') << 1
                activeChannels += check_channel_capacity('jade-chamber-channel-capacity-0.png')
                allOnesMask = 0b111

                if (activeChannels & allOnesMask):
                    click_picture('albedo-vator.png')
                    begin_streaming()
                elif (activeChannels ^ (1 << 2)):
                    click_picture('albedo-vator.png')
                    begin_streaming()
                elif (activeChannels ^ (1 << 1)):
                    click_picture('wanmin-restaurant.png')
                    begin_streaming()
                elif (activeChannels ^ 1):
                    click_picture('jade-chamber.png')
                    begin_streaming()
                else:
                    click_picture('albedo-vator.png')
                    begin_streaming()

            except:
                print("Failed to click picture, retrying...")

