
from classes import UNISI_Class
import pyautogui
import json,time,datetime


def SearchStartingClass(classes_list):
    c_time = time.localtime()
    current_time = time.strftime("%H", c_time)

    for item in classes_list:
        if "{:02d}".format(int(item['hour_start_time'])) == current_time:
            return item['name']

if __name__ == '__main__':

    # Finding Starting Class
    try:
        with open('/project_path/AutoClassJoiner/Classes_TMP_file.json') as json_file:
            classes_list = json.load(json_file)
    except Exception as error_message:
        print(error_message)

    Starting_Class = SearchStartingClass(classes_list)


    try:
        # Finding Class link
        with open('/project_path/AutoClassJoiner/LinkCourses.json') as json_file:
            class_links = json.load(json_file)
    except Exception as error_message:
        print(error_message)

    class_link=(class_links[str(Starting_Class)])

    # Clean screen (Ctrl+Super+D)
    #keyboard.press_and_release('alt+D')
    pyautogui.keyDown("alt")
    pyautogui.press("d")
    pyautogui.keyUp("alt")
    ####################d

    if 'webex' in class_link:
        Starting_Class  = UNISI_Class(Starting_Class, class_link,GMeet=False)
        #Starting_Class.Join2Class()    #need a way to avoid captha
    else:
        Starting_Class = UNISI_Class(Starting_Class, class_link)
        Starting_Class.Join2Class()

    with open('/project_path/AutoClassJoiner/joinclasslog.txt','a') as log_file:
        log_file.write('OK '+Starting_Class.Name+' - '+ str(datetime.datetime.now())+'\n'),
    log_file.close()


