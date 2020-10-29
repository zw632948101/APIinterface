import openpyxl

def excelRead(filePath,sheetName):
    """
    读取excel中的测试用例，一个字典对应一条用例，以列表结果返回
    """
    wb = openpyxl.load_workbook(filePath)
    cells = wb.get_sheet_by_name(sheetName)
    list = [i for i in cells]
    title = [l.value for l in list[0]]
    value = [[n.value for n in m] for m in list[1:]]
    res = [dict(zip(title, o)) for o in value]
    return res
