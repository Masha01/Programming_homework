import os
def delete(dirname):
    for root, dirs, files in os.walk(dirname):
        for f in files:
            os.remove(os.path.join(root, f))
        for d in dirs:
            delete(os.path.join(root,d))
        os.rmdir(root)
delete('кот')

def print_tree(dirname, space = 0):
    for root, dirs, files in os.walk(dirname):
        print(''*root)
        for i in files:
            print(''*space,' **()'.format(i)
        space += 2
        
