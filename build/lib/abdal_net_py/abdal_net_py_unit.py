import math
from hurry.filesize import size


def convert_web_speed_size(size_bytes):
    """
    Convert byte to other Units of information and show in xbit vs xbyte
    :param size_bytes:
    :return:
    """
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "Kbit/s", "Mbit/s", "Gbit/s", "Tbit/s", "Pbit/s", "Ebit/s", " Zbit/s", "Ybit/s")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"


def convert_byte_to(size_bytes):
    """
    Convert byte to other Units of information
    :param size_bytes:
    :return:
    """
    convert_size_bytes = size(size_bytes)
    return convert_size_bytes


def convert_size_by_unit(size_bytes, to='GB'):
    """
    Convert byte to other unit by select unit
    :param size_bytes:
    :param to:
    :return:
    """
    if size_bytes == 0:
        return 0, ''
    power = {'B': 0, 'KB': 1, 'MB': 2, 'GB': 3, 'TB': 4, 'EB': 5, 'ZB': 6, 'YB': 7}
    i = power[to]
    p = math.pow(1024, i)
    float_size = round(size_bytes / p, 2)
    return float_size
