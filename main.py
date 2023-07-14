import PyPDF2
import re
import os

""""""""""""""""""""""
1. Fill module MSN
2. Fil specific module Msn
   ex: 
   FlexRay: Fr
   Eeprom: Eep

"""""""""""""""""""""""

MSN = "MCU"
Msn = MSN.capitalize()
"""""""""""""""""""""""
Fill specific module here
"""""""""""""""""""""""
# Msn = "Eep"
""""""""""""""""""""""""""
# Đường dẫn tới file cần xóa
file_SWS = "./OUTPUT/AUTOSAR_SWS_"+MSN+"Driver.txt"
file_Output = "./OUTPUT/Output_"+Msn+".txt"
file_PDF = "./SWS/AUTOSAR_SWS_"+MSN+"Driver.pdf"

try:
    os.remove(file_SWS)
except:
    print(f"{file_SWS} does not exist")
try:
    os.remove(file_Output)
except:
    print(f"{file_Output} has been deleted")

print("Processing...")
# mở file PDF
pdf_file = open(file_PDF, 'rb')

# tạo đối tượng của PyPDF2 để đọc file PDF
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# tạo file txt để lưu nội dung của file PDF
with open(file_SWS,'w', encoding="utf-8") as txt_file:
    text = ""
    # đọc từng trang trong file PDF
    for page_num in range(pdf_reader.numPages):
        print("Reading page", page_num)
        # lấy nội dung của trang hiện tại
        page_obj = pdf_reader.getPage(page_num)
        text = page_obj.extractText()
        # ghi nội dung vào file txt
        txt_file.write(text.replace("\r", ""))
# đóng file
pdf_file.close()
txt_file.close()

with open(file_SWS, 'r', encoding="utf-8") as file:
    content = file.readlines()
file.close()
OutTmp= open('tmp.txt', 'a')
OutTmp1= open('tmp1.txt', 'a')
# Tìm kiếm chuỗi trong nội dung file
pattern = r"(?:\W).*SWS.*_.*"+Msn+".*_.*\d(?:])"
print("Find SWS_"+MSN)
for line in content:
    result = re.search(pattern, line)
    if result:
        # print(result.group())
        try:
            print(result.group().replace(" ", ""), file = OutTmp)
            print(result.group(), file = OutTmp1)
        except:
            print(result.group().encode("utf-8"), file = OutTmp)
            print(result.group().encode("utf-8"), file = OutTmp1)
OutTmp.close()
OutTmp1.close()

with open('tmp1.txt', 'r', encoding="utf-8") as file:
    SWS_REQ = file.readlines()
    numReq = len(SWS_REQ)
file.close()
for line in SWS_REQ:
    if line in content:
        print (line)

# Mở file và đọc nội dung
with open('tmp.txt', 'r', encoding="utf-8") as file:
    lines = file.readlines()
file.close()


final_output =""
# Tìm các ký tự bị trùng
char_count = {}
for char in lines:
    if char in char_count:
        char_count[char] += 1
    else: 
        char_count[char] = 1
        final_output +=char.replace(" ", "")
      
OutTmp2= open('tmp2.txt', 'a')
print(final_output, file = OutTmp2)
OutTmp2.close()

with open("tmp2.txt", 'r') as file:
    content2 = file.readlines()
    numlines = len(content2)
file.close()

process = 0
output= open(file_Output, 'a')
pat="SWS.*_.*"+Msn+".*_.*\d"
print("Processing output")
for line in content2:
    process= process+1
    rate = int((process * 100)/numlines)
    result = re.search(pat, line)
    if result:
        print(result.group(), file = output)
    print(f"Processing: {rate}%")
output.close()


try:
    os.remove("./tmp.txt")
except:
    print("tmp.txt does not exist")

# try:
#     os.remove("./tmp1.txt")
# except:
#     print("tmp1.txt does not exist")

try:
    os.remove("./tmp2.txt")
except:
    print("tmp2.txt does not exist")

print("Completed!!")

