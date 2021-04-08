import os

os.path.exists('test_os')
if not os.path.exists('test_os'):
    os.mkdir('test_os')
if not os.path.exists('test_os/test_os.txt'):
    f=open('test_os/test_os.txt','w')
    f.write('aru,i love you')
    f.close()
else:
    os.remove('test_os/test_os.txt')
    os.rmdir('test_os')