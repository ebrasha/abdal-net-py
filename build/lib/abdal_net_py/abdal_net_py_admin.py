"""
 # Project Name: Abdal NetPy
 # Programmer: Ebrahim Shafiei
 # Programmer WebSite: https://hackers.zone/
 # Programmer Email: Prof.Shafiei@Gmail.com
 # License : MIT
 # Current Date : 2023-05-30
 # Current Time : 12:51 AM
 # File Description: no description
"""


class AdminCheck:
    def __init__(self):
        pass

    def win_ad_check(self):
        """
        True mean is admin
        False mean is normal user

        :return:
        """
        try:
            is_admin = (os.getuid() == 0)
        except AttributeError:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        return is_admin

