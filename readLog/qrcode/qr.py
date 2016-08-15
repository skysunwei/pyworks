import qrcode

for line in open('product'):
    data = line.strip('\n').split(',')

    img = qrcode.make(data[1])
    img.save(data[0] + '.png')

