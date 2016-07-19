for line in open('shenghui.txt'):
    kv = line.split(',')
    print '\'' + kv[0] + '\' => [\'' + kv[1].strip('\n') + '\'],'
