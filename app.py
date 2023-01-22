from flask import Flask, request
import qrcode

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    link = request.args.get('link')
    img = qrcode.make(link)
    img.save('qr.png')
    return 'QR image of {} saved as qr.png'.format(link)


if __name__ == '__main__':
    app.run()
