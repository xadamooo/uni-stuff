import json
import urllib.request
import operator

'zmodyfikowanie pliku binarnego:'


filename1 = 'D:\\PWR\\Visual Studio\\systemy_informatyczne_internetu_rzeczy\\sample.bin'

with open(filename1, 'rb') as f:
    print(f.read())

with open(filename1, 'rb+') as f:
    f.seek(0)
    b1 = bytearray(b'systemy informatyczne internetu rzeczy')
    f.write(b1)


'''zmodyfikowanie json:'''


filename2 = 'D:\\PWR\\Visual Studio\\systemy_informatyczne_internetu_rzeczy\\sample2.json'

with open(filename2, 'r+') as f:
    json_data = json.load(f)
    json_data['size'] = "Small"
    f.seek(0)
    f.write(json.dumps(json_data))
    f.truncate()


'''sortowanie wartosci w json:'''

filename3 = 'D:\\PWR\\Visual Studio\\systemy_informatyczne_internetu_rzeczy\\sample3.json'

url = 'https://api.github.com/users?since=100'
data = urllib.request.urlopen(url).read()
output = json.loads(data)
output.sort(key=operator.itemgetter('id'), reverse=True)

json_object = json.dumps(output, indent=4)
with open(filename3, "w") as f3:
    f3.write(json_object)
