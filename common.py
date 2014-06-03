#-*-coding:utf8 -*-
import pdb
import traceback
import codecs


class FileOper(object):

    '''文件操作类
    文件操作,读取文件,写入文件,根据值写入,根据数组写入等等
    '''

    def file_read(self, file_path):
        '''读取文件内容,返回一个数组
        '''
        result = []
        with open(file_path, 'r') as f:
            for line in f.readlines():
                result.append(line.replace('\n', '').strip())  # 首先过滤字符串前后空格
        return result

    def file_write(self, file_path, content):
        '''写入内容到某个文件中
        '''
        try:
            # 普通的write和writelines接口无法写入utf8,需要通过codecs的open函数写入
            fw = codecs.open(file_path, 'w', 'utf-8')
            fw.write(content)
            fw.close()
        except:
            print 'error!:'
            print traceback.format_stack()
            fw.close()

    def file_writelines(self, file_path, lines):
        '''写入内容到某个文件中,此时的内容是一个数组
        '''
        try:
            fw = codecs.open(file_path, 'w', 'utf-8')
            fw.writelines(lines)
            fw.close()
        except:
            print 'error!:'
            print traceback.format_stack()
            pdb.set_trace()
            fw.close()


class Config(object):

    '''配置文件类
    存放全局变量,通过Config方式调用
    '''
    # 存放待监控文件,考虑到兼容性建议通过相对路径存放,文件夹直接提供名字即可,新增加文件不会触发监控事件
    watch_file_path = ['./watch_file']
