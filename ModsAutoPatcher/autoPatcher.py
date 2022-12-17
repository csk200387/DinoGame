import requests, os
from shutil import move
from getpass import getuser
from time import sleep, strftime

username = getuser()
path = f"C:\\Users\\{username}\\AppData\\Roaming\\.minecraft\\mods" # REAL PATH
#path = "C:\\Users\\csk20\\Desktop\\pyinstaller\\mods" # TEST PATH

def openModsFolder() :
    os.startfile(path)

def getModsList1() :
    fileList = [file for file in os.listdir() if file.endswith(".jar")]
    return fileList

def getModsList() :
    req = requests.get("https://raw.githubusercontent.com/csk200387/Toy/main/ModsAutoPatcher/modsList.txt")
    data = req.text.strip()
    return data.split("\n")

def checkServer() :
    list = getModsList()
    if list == [''] :
        print("아직 자동패치기 사용 기간이 아닙니다. 다음에 다시 시도해주세요")
        os.system("pause")
        exit()

def checkMods() :
    list = [file for file in os.listdir() if file.endswith(".jar")]
    if list :
        fname = strftime('%Y%m%d_BACKUP')
        #fname = strftime('%Y%m%d_%H:%M_BACKUP')
        try :
            os.mkdir(fname)
            print(f"현재 모드와 충돌을 방지하기 위해 기존의 모드 파일은 {fname} 폴더로 이동됩니다.")
            for i in list :
                move(i, fname)
        except :
            print(f"{fname} 과 같은 이름의 폴더가 있습니다\n폴더를 삭제하고 다시 실행해주세요")
            os.startfile(path)
            os.system("pause")
            exit()

def fileDownload() :
    list = getModsList()
    print(f"{len(list)} 개의 다운받을 파일이 있습니다.")
    sleep(1)
    for i in list :
        fileName = i.split("/")[-1]
        print(f"Download : {fileName}") 
        down = requests.get(i)
        with open(fileName, "wb") as f :
            f.write(down.content)

if __name__ == "__main__" :
    os.chdir(path)
    menu = input("마인크래프트 모드 반자동 적용기 1.0v\n메뉴 :\n1. mods파일 열기\n2. 모드 자동패치\n3. 프로그램 종료 : ")
    if menu == "1" :
        openModsFolder()
    elif menu == "2" :
        checkServer()
        checkMods()
        fileDownload()
        os.startfile(path)
    elif menu == "3" :
        exit()
    os.system("pause")
