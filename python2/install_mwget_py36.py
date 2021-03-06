# coding=utf-8
import subprocess
import os

PYTHON_VERSION = "3.6.7"
INSTALL_PATH = "/usr/local/python3"


def install_detail_info(msg):
    print("=" * 20)
    print('start execute shell: {0}'.format(msg))
    print("=" * 20)


def execute(command, shell=True):
    install_detail_info(command)
    res = subprocess.call(command, shell=shell)
    if res != 0:
        raise RuntimeError(r'{0}	failed'.format(command))


def install_mwget():
    execute('wget http://jaist.dl.sourceforge.net/project/kmphpfm/mwget/0.1/mwget_0.1.0.orig.tar.bz2')
    execute('tar -xjvf mwget_0.1.0.orig.tar.bz2')
    # 切换到解压文件路径
    os.chdir(os.path.join(os.getcwd(), 'mwget_0.1.0.orig'))
    execute('./configure')
    execute('make && make install')

    print("=" * 10),
    print("mwget安装完成"),
    print("=" * 10)
    print("多线程下载命令: mwget --n=线程数 http://网址")


def install_pytho3():
    download_python_code = r'mwget --n=100 https://www.python.org/ftp/python/{0}/Python-{0}.tgz'.format(PYTHON_VERSION)
    execute(download_python_code)

    mkdir_install_path = r'mkdir -p {0}'.format(INSTALL_PATH)
    execute(mkdir_install_path)

    tar_zip = r'tar -zxvf Python-{0}.tgz'.format(PYTHON_VERSION)
    execute(tar_zip)

    # 进入源码目录

    code_directory = r'Python-{0}'.format(PYTHON_VERSION)

    os.chdir(os.path.join(os.getcwd(), code_directory))

    execute(r'./configure --prefix={0}'.format(INSTALL_PATH))

    execute('make && make install')

    soft_link = r'ln -s {0}/bin/python3 /usr/bin/python3'.format(INSTALL_PATH)
    execute(soft_link)

    pip_soft_link = r'ln -s {0}/bin/python3/bin/pip3 /usr/bin/pip3'.format(INSTALL_PATH)
    execute(pip_soft_link)

    print("=" * 20),
    print("check version"),
    print("=" * 20)

    execute("{0}/bin/python3 -V".format(INSTALL_PATH))
    execute("{0}/bin/pip3 -V".format(INSTALL_PATH))

    print("手动将/usr/local/python3/bin加入PATH")
    print("编辑")
    print("vim ~/.bash_profile")

    edit_bash_profile = """
            # .bash_profile
            # Get the aliases and functions
            if  [  - f ~ / .bashrc ]; then
            . ~ / .bashrc
            fi
            # User specific environment and startup programs
            PATH = $PATH:$HOME/bin:/usr/local/python3/bin:
            export PATH
            """
    print(edit_bash_profile)
    print("使修改生效")
    print("source ~/.bash_profile")


def main():
    execute("yum install -y wget")

    yum_group_install = 'yum groupinstall -y "development tools"'
    execute(yum_group_install)

    yum_libraries = 'yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel expat-devel'
    execute(yum_libraries)

    install_mwget()
    install_pytho3()


if __name__ == '__main__':
    # mwget 下载命令
    # mwget --n=100 htpp://www.xxxx
    main()
