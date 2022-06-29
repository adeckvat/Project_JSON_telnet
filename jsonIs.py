import json
import enumIs as list

array = ["A", "B"]
path_to_template_file = "0300-PDU-FED-029-11AJ12-A-template.json"

#---------------------------
# Open the .json file
with open(path_to_template_file, "r") as fileRead:
    # Load its content and make a new dictionary
    data = json.load(fileRead)

# Working with JSON file
#-----------------------------------

def path(output_file, fileName): #have fan
    filePathNameWExt =  output_file + '/' + fileName

    return filePathNameWExt

#-----------------------------------
# Open (or create) an .json file 
# and store the new version of the data.
for j in list.Room_11_Row_1:
    for i in array:
        create_file_name = path("/home/chopper/IdeaProjects/JSON/rackUpdate/configs", f'0300-PDU-FED-029-11A{j.name}16-{i}.json')
        change_data_name = data["devices"]["data"][0]["attributes"]["name"] = f'0300-PDU-FED-029-11A{j.name}16-{i}' # Это пиздец
        change_data_from_address = data["devices"]["data"][0]["attributes"]["from_address"] = f'0300-PDU-FED-029-11A{j.name}16-{i}@nw.mts.ru' # Не такой уж и пиздец
        change_data_from_address_snmp = data["network_smtp"]["data"][0]["attributes"]["from_address"] = f'0300-PDU-FED-029-11A{j.name}16-{i}@nw.mts.ru' # Нормально, пойдет
        with open(create_file_name, 'w') as fileWrite:
            json.dump(data, fileWrite, indent = 4)

#-------------------------------------
fileRead.close()
fileWrite.close()

#----------------------

#Comments - may usefull
#outfile Записать вывод infile в заданный outfile 
#sort_keys=True сортировка по алфавиту
#separators=(',', ':') Компактное кодирование
#indent, tab, no-indent, compact Взаимоисключающие параметры управления пробелами
#json-lines Анализируйте каждую строку ввода как отдельный объект JSON
#json.loads Расшифровка JSON args = 'r'
#json.dumps Записб фалй args = 'w'
#with open(path, 'args')