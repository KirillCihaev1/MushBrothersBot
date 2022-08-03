import gspread
gc = gspread.service_account(filename='valiant-monitor-358218-ac41a0a1e0fe.json')
sh = gc.open("Заказы")
worksheet = sh.worksheet("Заказы")


def add_order(order_id, user_id, item_list, email, phone, message, date, status):
    i = len(worksheet.col_values(1)) + 1
    worksheet.update('A' + str(i), order_id)
    worksheet.update('B' + str(i), user_id)
    worksheet.update('C' + str(i), item_list)
    worksheet.update('D' + str(i), email)
    worksheet.update('E' + str(i), phone)
    worksheet.update('G' + str(i), message)
    worksheet.update('H' + str(i), date)
    worksheet.update('I' + str(i), status)


def set_address(order_id, address):
    i = worksheet.find(str(order_id), in_column=1).row
    worksheet.update("F" + str(i), address)


