import speedtest
import math
from hurry.filesize import size


class AbdalNetPy:
    class AbdalNetCalc:
        def __init__(self, size_bytes):
            self.size_bytes = size_bytes

        def convert_web_speed_size(self):
            if self.size_bytes == 0:
                return "0B"
            size_name = ("B", "Kbit/s", "Mbit/s", "Gbit/s", "Tbit/s", "Pbit/s", "Ebit/s", " Zbit/s", "Ybit/s")
            i = int(math.floor(math.log(self.size_bytes, 1024)))
            p = math.pow(1024, i)
            s = round(self.size_bytes / p, 2)
            return "%s %s" % (s, size_name[i])

    class AbdalUnitCalc:
        def __init__(self, size_bytes):
            self.size_bytes = size_bytes

        def convert_byte_to(self):
            convert_size_bytes = size(self.size_bytes)
            return convert_size_bytes
