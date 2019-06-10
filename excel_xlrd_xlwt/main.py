# coding: utf-8
import os

def simplest():
    import xlwt
    workbook = xlwt.Workbook(encoding = 'ascii')
    worksheet = workbook.add_sheet('My Worksheet')

    worksheet.write(2, 3, 'Value of Row 2, Column 3')

    workbook.save('simplest.xls')

def set_font():
    import xlwt
    workbook = xlwt.Workbook(encoding = 'ascii')
    worksheet = workbook.add_sheet('My Worksheet')

    font = xlwt.Font() # Create the Font
    font.name = 'PT Mono'
    font.bold = True
    font.underline = True
    font.italic = True
    font.height = 0x0300 # 字体大小， 300 ~ 38.5
    style = xlwt.XFStyle() # Create the Style
    style.font = font # Apply the Font to the Style
    worksheet.write(0, 0, 'Unformatted value')
    worksheet.write(1, 0, 'Formatted value', style) # Apply theStyle to the Cell
    workbook.save('set_font.xls')
    '''
    font.struck_out = True # May be: True, False
    font.escapement = xlwt.Font.ESCAPEMENT_SUPERSCRIPT # May be:ESCAPEMENT_NONE, ESCAPEMENT_SUPERSCRIPT, ESCAPEMENT_SUBSCRIPT
    font.family = xlwt.Font.FAMILY_ROMAN # May be: FAMILY_NONE,FAMILY_ROMAN, FAMILY_SWISS, FAMILY_MODERN, FAMILY_SCRIPT,FAMILY_DECORATIVE
    font.charset = xlwt.Font.CHARSET_ANSI_LATIN # May be:CHARSET_ANSI_LATIN, CHARSET_SYS_DEFAULT, CHARSET_SYMBOL,CHARSET_APPLE_ROMAN, CHARSET_ANSI_JAP_SHIFT_JIS,CHARSET_ANSI_KOR_HANGUL, CHARSET_ANSI_KOR_JOHAB,CHARSET_ANSI_CHINESE_GBK, CHARSET_ANSI_CHINESE_BIG5,CHARSET_ANSI_GREEK, CHARSET_ANSI_TURKISH, CHARSET_ANSI_VIETNAMESE,CHARSET_ANSI_HEBREW, CHARSET_ANSI_ARABIC, CHARSET_ANSI_BALTIC,CHARSET_ANSI_CYRILLIC, CHARSET_ANSI_THAI, CHARSET_ANSI_LATIN_II,CHARSET_OEM_LATIN_I
    font.colour_index = ?
    font.get_biff_record = ?
    font.height = 0x00C8 # C8 in Hex (in decimal) = 10 points inheight.
    font.outline = ?
    font.shadow = ?
    '''


def eg00():
    ''' 创建工作簿&表 写入数据 保存文件
    '''

    # 创建工作簿(workbook)，添加工作表(worksheet)
    wb = xlwt.Workbook()
    ws = wb.add_sheet('my sheet')

    # 写入
    for i in range(56):
        ws.write(i, 0, str(i))
        ws.write(i, 1, i * i)
        ws.write(i, 2, 'Content')

    # 保存
    filename = 'result_000.xls'
    wb.save(filename)
    print("Done!")

def eg01():
    '''
        创建工作簿、表
        定义单元格 pattern 属性
        写入， 保存
    '''

    # 创建工作簿(workbook)，添加工作表(worksheet)
    wb = xlwt.Workbook()
    ws = wb.add_sheet('my sheet')
    print("Created workbook and 'my sheet'")

    # 根据属性写入写数据
    print("writing with some style...")
    for i in range(56):

        # 创建 pattern 单元格
        pattern = xlwt.Pattern()  # Create the pattern
        #   pattern属性：填充
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN  # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12

        # 颜色码选取:颜色范围是 8~63, 共56种
        COLOR_CODE = 8 + i
        pattern.pattern_fore_colour = COLOR_CODE 
        pattern.pattern_back_colour = 2

        # style 接收 pattern属性
        style = xlwt.XFStyle()  # Create the pattern
        style.pattern = pattern  # Add pattern to style

        ws.write(i, 0, 'color code')        # NO style
        ws.write(i, 1, str(COLOR_CODE))     # NO style
        ws.write(i, 2, 'Content', style)    # with style!!

    tall_style = xlwt.easyxf('font:height 720')  # 36pt
    ws.row(0).set_style(tall_style)

    ws.col(3).width = 256 * 36

    ''' 列宽： 以字符0宽度的1/256为单位，如果想设置20个0的宽度，就是20*256
    '''

    ws.write(0, 3, '0'*32)
    filename = 'result_001.xls'
    wb.save(filename)
    print("Done! file saved to", filename)

def eg02():
    import xlwt
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('My Sheet')

    # write_merge 4个参数：  行范围2个， 列范围2个；
    worksheet.write_merge(0, 0, 0, 3, 'First Merge') # Merges row 0'scolumns 0 through 3.

    font = xlwt.Font() # Create Font
    font.bold = True # Set font to Bold
    style = xlwt.XFStyle() # Create Style
    style.font = font # Add Bold Font to Style

    # 第二次合并
    worksheet.write_merge(2, 5, 2, 7, 'Second Merge', style) # Mergesrow 1 through 2's columns 0 through 3.

    workbook.save('Excel_Workbook.xls')

def eg03():
    ''' 打开 xls, 修改内容， 保存
    '''
    from xlrd import open_workbook
    from xlutils.copy import copy
    
    # 打开
    rb = open_workbook('res.xls')
    
    # 获取sheet（0）
    rs = rb.sheet_by_index(0)
    
    wb = copy(rb)       
    # 利用xlutils.copy函数，将xlrd.Book转为xlwt.Workbook，再用xlwt模块进行存储

    
    #通过get_sheet()获取的sheet有write()方法
    ws = wb.get_sheet(0)
    ws.write(2, 2, 'changed!')
    
    wb.save('res1.xls')

def eg04_merge_patterns():
    ''' 演示： 合并单元格
    '''
    import xlwt
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('My Sheet')

    # write_merge 4个参数：  行范围2个， 列范围2个；
    worksheet.write_merge(0, 0, 0, 3, 'First Merge') # Merges row 0'scolumns 0 through 3.

    font = xlwt.Font() # Create Font
    font.bold = True # Set font to Bold
    style = xlwt.XFStyle() # Create Style
    style.font = font # Add Bold Font to Style

    # 第二次合并
    worksheet.write_merge(2, 5, 2, 7, 'Second Merge', style) # Mergesrow 1 through 2's columns 0 through 3.

    workbook.save('res.xls')
    os.system("explorer .")

if __name__ == "__main__":
    tmp()

    # https://blog.csdn.net/ngforever/article/details/14225495
    # openpyxl xlsxwriter xlutils
    # https://blog.csdn.net/COCO56/article/details/84403107