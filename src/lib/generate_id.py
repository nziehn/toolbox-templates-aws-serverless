import random
import string


def generate_id(size=16, chars=string.ascii_uppercase + string.digits):
    '''
    Generate a random string of :size characters
    '''
    return ''.join(random.choice(chars) for _ in range(size))