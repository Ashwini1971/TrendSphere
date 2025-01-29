import xlrd

def read_locators(sheet_name):
    workbook = xlrd.open_workbook()
    sheet = workbook.sheet_by_name(sheet_name)
    rows = sheet.get_rows()
    return {}

