def print_file_info(file_name):
  f = None
  try:
    f = open(file_name, 'r')
    print(f.read())
  except:
    print('文件不存在')
  finally:
    if f:
      f.close()

def append_to_file(file_name):
    print_file_info(file_name)
    f = open(file_name, 'a')
    str = input('请输入追加内容')
    f.write('\n')
    f.write(str)
    f.close()
    print_file_info(file_name)