import random
from users.models import User
def formatNumber(number):
    formatted_number = "{:,}".format(number)
    return formatted_number

def yetuVerification(yetucode):
    usuarioData = User.objects.filter(yetucode=yetucode)
    if usuarioData.exists:
        numberCode = random.randint(1000, 9000)
        newyetucode = (f'YT{numberCode}')
        return newyetucode
    else:
        return yetucode
