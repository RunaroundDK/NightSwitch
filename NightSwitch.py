import subprocess
import time


def main():
    print ("""
    Enter 60m for 1 hour
    s for seconds
    m for minutes
    h for hours
    d for days
    """)
    smhd = input('[0]: ')
    subprocess.Popen('sleep %s && shutdown' % (smhd), shell=True)
    print ("The system will shutdown after " + smhd)
    print ("Please do not close terminal...")

main()


#https://www.cyberciti.biz/faq/linux-unix-sleep-bash-scripting/
#https://stackoverflow.com/questions/33901726/run-command-after-1-hour-in-linux
