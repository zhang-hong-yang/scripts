# coding=utf-8
import subprocess
import os


def install_detail(msg):
    print("=" * 20)
    print('start execute shell: {0}'.format(msg))
    print("=" * 20)


def execute(command, shell=True):
    install_detail(command)
    res = subprocess.call(command, shell=shell)
    if res != 0:
        raise RuntimeError(r'{0}	failed'.format(command))


def main():
    execute("yum install -y wget")

    yum_group_install = 'yum groupinstall -y "development tools"'
    execute(yum_group_install)

    yum_libraries = 'yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel expat-devel'
    execute(yum_libraries)

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


if __name__ == '__main__':
    # mwget 下载命令
    # mwget --n=100 htpp://www.xxxx
    main()
