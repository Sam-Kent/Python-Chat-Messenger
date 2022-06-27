import socket
import re
import time
import pynput
import sys
import threading


def decode_this(msg2):
    decode1 = {
        "346": "A",
        "459": "B",
        "250": "C",
        "225": "D",
        "436": "E",
        "498": "F",
        "998": "G",
        "525": "H",
        "159": "I",
        "978": "J",
        "735": "K",
        "714": "L",
        "254": "M",
        "947": "N",
        "941": "O",
        "121": "P",
        "844": "Q",
        "523": "R",
        "173": "S",
        "194": "T",
        "500": "U",
        "347": "V",
        "122": "W",
        "835": "X",
        "516": "Y",
        "638": "Z",
        "310": "a",
        "362": "b",
        "924": "c",
        "262": "d",
        "900": "e",
        "528": "f",
        "843": "g",
        "973": "h",
        "647": "i",
        "264": "j",
        "660": "k",
        "412": "l",
        "533": "m",
        "424": "n",
        "353": "o",
        "324": "p",
        "658": "q",
        "440": "r",
        "697": "s",
        "646": "t",
        "447": "u",
        "342": "v",
        "524": "w",
        "511": "x",
        "212": "y",
        "815": "z",
        "780": "0",
        "325": "1",
        "414": "2",
        "413": "3",
        "431": "4",
        "152": "5",
        "642": "6",
        "639": "7",
        "386": "8",
        "701": "9",
        "149": "~",
        "588": "!",
        "827": "@",
        "537": "#",
        "140": "$",
        "157": "%",
        "903": "^",
        "862": "&",
        "510": "*",
        "151": "(",
        "330": ")",
        "828": "_",
        "120": "-",
        "118": "+",
        "466": "=",
        "434": "{",
        "917": "}",
        "737": "[",
        "464": "]",
        "221": "|",
        "390": "\\",
        "544": ",",
        "115": ".",
        "332": "/",
        "920": "<",
        "443": ">",
        "383": "?",
        "643": "'",
        "626": ":",
        "612": ";",
        "781": "`",
        "317": '"',
        "112": " ",
    }

    msg3 = ""
    msg2 = re.findall(r'\d{3}', msg2.decode())
    for x in msg2:
        if x in decode1:
            msg3 = msg3 + decode1.get(x)

        else:
            msg3 = msg3 + x

    return msg3


def encode_this(msg):
    encode1 = {
        "A": "346",
        "B": "459",
        "C": "250",
        "D": "225",
        "E": "436",
        "F": "498",
        "G": "998",
        "H": "525",
        "I": "159",
        "J": "978",
        "K": "735",
        "L": "714",
        "M": "254",
        "N": "947",
        "O": "941",
        "P": "121",
        "Q": "844",
        "R": "523",
        "S": "173",
        "T": "194",
        "U": "500",
        "V": "347",
        "W": "122",
        "X": "835",
        "Y": "516",
        "Z": "638",
        "a": "310",
        "b": "362",
        "c": "924",
        "d": "262",
        "e": "900",
        "f": "528",
        "g": "843",
        "h": "973",
        "i": "647",
        "j": "264",
        "k": "660",
        "l": "412",
        "m": "533",
        "n": "424",
        "o": "353",
        "p": "324",
        "q": "658",
        "r": "440",
        "s": "697",
        "t": "646",
        "u": "447",
        "v": "342",
        "w": "524",
        "x": "511",
        "y": "212",
        "z": "815",
        "0": "780",
        "1": "325",
        "2": "414",
        "3": "413",
        "4": "431",
        "5": "152",
        "6": "642",
        "7": "639",
        "8": "386",
        "9": "701",
        "~": "149",
        "!": "588",
        "@": "827",
        "#": "537",
        "$": "140",
        "%": "157",
        "^": "903",
        "&": "862",
        "*": "510",
        "(": "151",
        ")": "330",
        "_": "828",
        "-": "120",
        "+": "118",
        "=": "466",
        "{": "434",
        "}": "917",
        "[": "737",
        "]": "464",
        "|": "221",
        "\\": "390",
        ",": "544",
        ".": "115",
        "/": "332",
        "<": "920",
        ">": "443",
        "?": "383",
        "'": "643",
        ":": "626",
        ";": "612",
        "`": "781",
        '"': "317",
        " ": "112",
        }

    #while y in msg not in encode1:
    #    msg = input("USE VALID CHARACTERS. Enter your message here: ")
    msg2 = ""
    for x in msg:
        if x in encode1:
            msg2 = msg2 + encode1.get(x)

        else:
            msg2 = msg2 + x

    return msg2


def typing(m):
    global con
    con.send(encode_this("XZYT125@#$%").encode())


def loading(m):
    print("typing", end="")
    count = 0
    while True:
        sys.stdout.write(".")
        time.sleep(1.2)
        count += 1
        sys.stdout.flush()
        if count % 4 == 0:
            sys.stdout.write("\b" * 4 + " " * 4 + "\b" * 4)
            sys.stdout.flush()


nec = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
nec.bind(("", 56995))
nec.listen()
print("Establishing Connection...")
con, dre = nec.accept()
print("Connection Acquired")
print(f"Connection from {dre}")

#con.setblocking(False)

def boardf():
    board = pynput.keyboard.Listener(on_press=typing)
    with board:
        board.join()


#threading.Thread(target=boardf()).start()


while True:
        output = con.recv(1024)
        output = output.decode()
        if output == "Client diconnected from the server":
            print("\nClient diconnected from the server. \nNo connection. \nServer shutting down...")
            time.sleep(1)
            break

        elif output == "XZYT125@#$%":
            #loading()
            pass

        elif output.isdigit():
            output = output.encode()
            print(decode_this(output))
            msg = input("\n>>> ")
            con.send(encode_this(msg).encode())

        else:
            print(output)



con.close()







