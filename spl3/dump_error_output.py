import subprocess

from globals import start_time

def get_error_dump_after_crash():
    logcat_command = ['timeout', '3s', 'adb', 'logcat', '-v', 'time']
    logcat_process = subprocess.Popen(logcat_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


    grep_command = ['grep', '-i', 'runtime']
    grep_process = subprocess.Popen(grep_command, stdin=logcat_process.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


    awk_command = ["awk", f"$2 > \"{start_time}\""]
    awk_process = subprocess.Popen(awk_command, stdin=grep_process.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


    output, error = awk_process.communicate()


    return output.decode('utf-8')
