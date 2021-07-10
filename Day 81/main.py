from morse_code import morse_code

header = '''
___  ______________  _____ _____    _____ ___________ _____   _____  _____ _   _  ___________  ___ _____ ___________ 
|  \/  |  _  | ___ \/  ___|  ___|  /  __ \  _  |  _  \  ___|  |  __ \|  ___| \ | ||  ___| ___ \/ _ \_   _|  _  | ___ \\
| .  . | | | | |_/ /\ `--.| |__    | /  \/ | | | | | | |__    | |  \/| |__ |  \| || |__ | |_/ / /_\ \| | | | | | |_/ /
| |\/| | | | |    /  `--. \  __|   | |   | | | | | | |  __|   | | __ |  __|| . ` ||  __||    /|  _  || | | | | |    / 
| |  | \ \_/ / |\ \ /\__/ / |___   | \__/\ \_/ / |/ /| |___   | |_\ \| |___| |\  || |___| |\ \| | | || | \ \_/ / |\ \ 
\_|  |_/\___/\_| \_|\____/\____/    \____/\___/|___/ \____/    \____/\____/\_| \_/\____/\_| \_\_| |_/\_/  \___/\_| \_|                                                                                
'''

print(header)

user_input = input("Please enter a string: ")
converted_morse_code = ""

for alphabet in user_input.lower():
    single_code = morse_code.get(alphabet)
    if single_code is None:
        converted_morse_code += "/ "
    else:
        converted_morse_code += single_code + " "

print(converted_morse_code)
