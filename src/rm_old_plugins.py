'''
Created on Feb 27, 2012

@author: silent
'''

import os
import sys

def search_duplicated_plugins(srcdir):
    print "Searching in " + srcdir

    result = []
    try:
        filelist = os.listdir(srcdir)
        filelist.sort()

        prevfile = filelist[len(filelist) - 1]

        for file in filelist:
            if file.rsplit('_', 1)[0] == prevfile.rsplit('_', 1)[0]:
                result.append(prevfile)

            prevfile = file
    except:
        print '%s access denied.' % srcdir

    return result


def confirem_to_delete(dupfiles):
    for file in dupfiles:
        print file
    print '-' * 80
    yn = raw_input(' Total %d files(dirs). Continue to delete? (y/n) ' % len(dupfiles))

    if yn == 'Y' or yn == 'y':
        return True
    return False


def delete_files(srcdir, dupfiles):
    for file in dupfiles:
        filepath = srcdir + '/' + file

        if os.path.isdir(filepath):
            delete_files(filepath, os.listdir(filepath))
            if os.path.exists(filepath):
                os.removedirs(filepath)
        else:
            os.remove(filepath)


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        f = sys.argv[0].split('/')

        print "Usage: " + f[len(f) - 1] + " eclipse_plugins_dir"
        sys.exit()

    srcdir = sys.argv[1]
    dupfiles = search_duplicated_plugins(srcdir)
    ret = confirem_to_delete(dupfiles)
    if ret:
        delete_files(srcdir, dupfiles)

    pass
