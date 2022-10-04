from . import main


# For health check
@main.route('/')
def index():
    return 'OK'
