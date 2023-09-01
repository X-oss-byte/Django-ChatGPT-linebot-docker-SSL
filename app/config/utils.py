# If you don't do this you will have to add the host IP in INTERNAL_IPS = ('127.0.0.1',)
# And it will change, then you will have to change INTERNAL_IPS again.

def show_toolbar(request):
    return not request.is_ajax()
