import string
import secrets


def generate_password(length):
    """
    return complex password
    :param length:
    :return:
    """
    alphabet = string.ascii_letters + string.digits + "*&^%$#"
    password = []
    for i in range(length):
        password.append(secrets.choice(alphabet))

    return "".join(password)


def pass_list(counter, length):
    """
    return complex password with length and With a specified number of password
    :param counter:
    :param length:
    :return:
    """
    password_list = []
    for i in range(counter):
        password_list.append(generate_password(length))
    return password_list


def ir_mobile_generator(prefix):
    """
    iranian mobile phone generate
    :param prefix:
    :return:
    """
    mobile_number_list = []
    for num in range(1111111, 9999999):
        mobile_number_list.append(prefix + str(num))
    return mobile_number_list
