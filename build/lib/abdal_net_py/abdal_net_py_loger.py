import os
from datetime import datetime
import psutil


def error_writer(error_content, file_name):
    """
    log writer
    :param error_content:
    :param file_name:
    :return:
    """

    def get_size(bytes, suffix="B"):
        """
        Scale bytes to its proper format
        e.g:
            1253656 => '1.20MB'
            1253656678 => '1.17GB'
        """
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor

    try:
        svmem = psutil.virtual_memory()
        get_current_date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S').__str__()
        log_file_name = file_name
        if os.path.exists(log_file_name):
            mode_write = 'a'  # append if already exists
        else:
            mode_write = 'w'  # make a new file if not

        error_log_writer = open(log_file_name, mode_write)
        error_log_writer.write(
            "[ " + get_current_date_time + " ]" + " - " + error_content.__str__() + f"  [  Available Memory Usage: {get_size(svmem.available)} ] " + f" [ Total CPU Usage: {psutil.cpu_percent()}% ] " + " \n")
        error_log_writer.close()
    except Exception as e:
        print(e.__str__())
        pass
