#json to csv
import csv
from tkinter import *  #  Python GUI
from tkinter.filedialog import askopenfiles, askopenfile
from tkinter.messagebox import showwarning, showinfo
global input_files, output_files
input_files = None
output_files = None

window = Tk()
window.title("JSON to CSV")
window.geometry("640x480+100+100")
input_warn=Label(window, text="Open JSON Files 버튼을 눌러 변경하고 싶은 json 파일(들)을 꼭 선택해주세요.", width=100, height=5, fg="black",wraplength=300)
output_warn=Label(window, text="Open CSV File 버튼을 눌러 csv 파일을 하나만 선택해주세요.\n선택된 CSV File에 새로운 JSON파일이 병합됩니다.\nCSV File 선택은 필수가 아닙니다.", width=400, height=3, fg="red",wraplength=400)
input_warn.pack()
output_warn.pack()


def open_json():
    files = askopenfiles(mode ='r', filetypes =[('json', '*.json')])
    if files != "":
        input_files = files
        file_names = ""
        for file in input_files:
            file_name = str(file.name).split('/')[-1]
            file_names += file_name+', ' 
        texts = "불러오기 성공한 파일 리스트 :\n"+file_names[:-2]
        showinfo(title="Open JSON list", message=texts)
 
    
def open_csv():
    file = askopenfile(mode ='r', filetypes =[('csv', '*.csv')])
    if file != "":
        output_file = file
        texts = "불러오기 성공한 CSV 파일 :\n"+str(file.name).split('/')[-1]
        showinfo(title="Open CSV list", message=texts) 

def delete_csv():
    try:
        output_files = None    
        showinfo(title="Delete CSV File", message="CSV 파일을 삭제했습니다.\n선택한 CSV 파일이 없습니다.") 
    except: 
        showwarning(title="Delete CSV File", message="[ERROR] CSV 파일을 삭제 실패.")

def json_to_csv():
    try:
        if input_files is None:
            showwarning(title="JSON to CSV", message="변환 실패\n선택된 JSON 파일이 없습니다.\nJSON 파일 선택은 필수입니다.")
        elif output_files is None:
            
            showinfo(title="JSON to CSV", message="변환 성공!\n선택하신 JSON 파일(들)이 CSV파일로 변환되었습니다.")  
        else:
            showinfo(title="JSON to CSV", message="변환 성공!\n선택하신 JSON 파일(들)이 선택하신 CSV파일에 병합되었습니다.") 
    except:
         showwarning(title="JSON to CSV", message="[ERROR] 변환 실패.")

btn = Button(window, text ='Open JSON Files', command = lambda:open_json())
btn.pack(side = TOP, pady = 5)

btn = Button(window, text ='Open CSV File', command = lambda:open_csv())
btn.pack(side = TOP, pady = 5)
btn = Button(window,foreground="red", text ='Delete CSV File', command = lambda:delete_csv())
btn.pack(side = TOP, pady = 5)

btn = Button(window, foreground="blue",  text ='JSON to CSV', command = lambda:json_to_csv())
btn.pack(side = BOTTOM, pady = 5)

window.mainloop()