#Python 提供了一个办法，把这些定义存放在文件中，为一些脚本或者交互式的解释器实例使用，这个文件被称为模块
#模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py
import function

#import一个我们写的py文件时会自动运行一整遍
#可以用__name__控制它不运行
if __name__ == '__main__':
   pass
else:
   print("",end="")

#在模块多时为了避免混乱，应该使用分级文件管理：
sound/                          顶层包
      __init__.py               初始化 sound 包
      formats/                  文件格式转换子包
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  声音效果子包
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  filters 子包
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
#这样导入时就输入import sound.effects.echo全称
#或者from sound.effects import echo

