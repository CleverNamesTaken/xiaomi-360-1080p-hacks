import base64,argparse,qrcode
parser=argparse.ArgumentParser()
parser.add_argument("password",type=str,help="Your WiFi password")
parser.add_argument("SSID",type=str,help="Name of your WiFi network")
args=parser.parse_args()



key = '89JFSjo8HUbhou5776NJOMp9i90ghg7Y78G78t68899y79HY7g7y87y9ED45Ew30O0jkkl'.encode('utf-8')
string=(args.password).encode('utf-8')

b='1234567890123456' #bindkey
s=base64.b64encode(bytes(args.SSID,'utf-8'))

result=b''
for key, string in zip(key,string):
    result+=bytes([key ^ string])
p=(base64.b64encode(result))
t="America/New_York"

full='b={}&s={}&p={}&t={}'.format(b,s.decode('utf-8'),p.decode('utf-8'),t)

qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
        )

qr.add_data(full)
qr.make(fit=True)
img = qr.make_image()
img.save(args.SSID+"_QR.jpg")
print("Created {} for SSID {} and password {}".format(args.SSID+"_QR.jpg", args.SSID, args.password))

