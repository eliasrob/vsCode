import webbrowser, sys, pyperclip

commandlineArg = sys.argv

if len(commandlineArg) >1:
    print("commandline:")
    print(commandlineArg)
    address = ''.join(commandlineArg[1:])
    print("äddress")
    print(address)
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

