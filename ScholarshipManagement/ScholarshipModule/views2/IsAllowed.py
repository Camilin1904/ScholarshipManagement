from ..forms import *
from ..models import *

def isAllowed(user, expectedRole):
    return(user.role == expectedRole)