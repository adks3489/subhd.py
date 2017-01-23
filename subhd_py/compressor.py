'''
This modules handles file decompression / extractions.
'''
import rarfile
import zipfile

class BaseCompressedFileHandler(object):
    '''Base Compressed File Handler.

    This exists since the interface of rarfile and zipfile
    are very similar. This might changes in time.

    Args:
        sub_buff: archieve binary data instance to be supplied.
        compression_class: modules to pass around.

    '''
    def __init__(self, sub_buff, compression_class):
        self.archieve_object = compression_class(sub_buff)

    def list_info(self):
        '''Return the file lists of the archieve.

        Returns:
            info_list: a list of dictionaries contains:
                       'size', 'name', 'info_obj'.

        '''
        info_list = []
        for i in self.archieve_object.infolist():
            info = {
                'size': i.file_size,
                'name': i.filename,
                'info_obj': i
            }
            info_list.append(info)
        return info_list

    def extract(self, filename):
        '''Extract subtitle, given its filename.

        Args:
            filename: the subtitle of filename to be extracted.
        Returns:
            raw_sub: the string data of the subtitle.

        '''
        raw_subfile = self.archieve_object.open(filename, 'r')
        raw_sub = raw_subfile.read()
        raw_subfile.close()
        return raw_sub

    def extract_bestguess(self, conv_type = 'zht'):
        '''Extract subtitle by choosing the largest one.

        Returns:
            raw_sub: the string data of the subtitle.
        '''
        info = self.list_info()
        #candidate = max(info, key=lambda x: x['size'])
        def extract_score(filename, conv_type = 'zht'):
            point = 0
            if filename.split('.')[-1] in ('srt', 'ssa', 'ass'):
                point = point + 1 
            convs = ('cht', 'zht')
            if conv_type == 'zhs':
               convs = ('chs', 'zhs')
            if filename.split('.')[-2] in convs:
                point = point + 1
            return point

        candidate = max(info, key=lambda x: extract_score(x['name'] ,conv_type))
        return (candidate['name'], self.extract(candidate['name']))

class RARFileHandler(BaseCompressedFileHandler):
    '''RAR File Handler, subclass from BaseCompressedFileHandler.

    Args:
        sub_buff: archieve binary data instance to be supplied.
        compression_class: modules to pass around.

    '''
    def __init__(self, sub_buff):
        super(RARFileHandler, self).__init__(sub_buff, rarfile.RarFile)

class ZIPFileHandler(BaseCompressedFileHandler):
    '''ZIP File Handler, subclass from BaseCompressedFileHandler

    Args:
        sub_buff: archieve binary data instance to be supplied.
        compression_class: modules to pass around.

    '''
    def __init__(self, sub_buff):
        super(ZIPFileHandler, self).__init__(sub_buff, zipfile.ZipFile)
