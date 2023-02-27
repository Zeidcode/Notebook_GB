def out_red(text):
    print("\033[31m {}" .format(text))

def out_blue(text):
    print("\033[34m {}" .format(text))

def out_yellow(text):
    print("\033[33m\033[5m {}" .format(text))

def result_color(text):
    print("\033[37m\033[44m {}" .format(text))