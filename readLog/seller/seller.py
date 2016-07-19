for line in open('seller'):
    kv = line.split(',')
    print 'insert `channelandsaler`(`channeluserid`, `saleruserid`) values('+\
          kv[1].strip('\n') + ',' + kv[0] + ');'

