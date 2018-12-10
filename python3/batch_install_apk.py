import os
import subprocess


def install_akp(apks: list):
    print(f"需要安装的apk:{apks}")
    for apk in apks:
        print(f"install : {apk}")
        try:
            subprocess.call(f'adb install -r "{apk}"', shell=False)
        except Exception as e:
            print(f"安装{apk}失败")


def main():
    all_files = os.listdir(os.getcwd())
    apks = [file for file in all_files if file.endswith(".apk")]
    install_akp(apks)


if __name__ == '__main__':
    main()
