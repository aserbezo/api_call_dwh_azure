import tkinter

import requests
from PIL import ImageTk, Image
from tkinter import messagebox

from function_helpers import Function

from main import main_logic, get_database_status


def pause_servers():
    for i in final:
        resource_name = i["resource_group_nane"]
        server_name = i['server_name']
        database_name = i['database_name']
        header = {'Authorization': entry_token.get(), 'Content-Type': 'application/json'}
        url = f'https://management.azure.com/subscriptions/{entry_subs_id.get()}/resourceGroups/{resource_name}' \
              f'/providers/Microsoft.Sql/servers/{server_name}/databases' \
              f'/{database_name}/pause?api-version=2020-11-01-preview'

        response = requests.post(headers=header)
        print(response)
    return 'it paused'


def resume_servers():
    for i in final:
        resource_name = i["resource_group_nane"]
        server_name = i['server_name']
        database_name = i['database_name']
        header = {'Authorization': entry_token.get(), 'Content-Type': 'application/json'}
        url = f'https://management.azure.com/subscriptions/{entry_subs_id.get()}/resourceGroups/{resource_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/resume?api-version=2021-02-01-preview'

        response = requests.post(url, headers=header)
        print(response)
    return 'it s resumed'


def clear_result():
    global display_result_frame
    display_result_frame.destroy()
    display_result_frame = tkinter.Frame(window, width=300, height=300)
    display_result_frame.pack()
    # button_clear_display = tkinter.Button(display_result_frame, text='Clear', width=20)
    # button_clear_display.pack(pady=10)


def display_result():
    token = entry_token.get()
    subs = entry_subs_id.get()

    header = {'Authorization': token, 'Content-Type': 'application/json'}
    RESOURCE_GROUP_NAMES_AND_SERVERS = main_logic(header, subs)
    print(RESOURCE_GROUP_NAMES_AND_SERVERS)
    DATABASE_STATUS = get_database_status(header, subs, RESOURCE_GROUP_NAMES_AND_SERVERS)
    print(DATABASE_STATUS)
    for i in DATABASE_STATUS:
        resource_name = i["resource_group_name"]
        server_name = i['server_name']
        database_name = i['database_name']
        status = i['status']
        result_label = tkinter.Label(display_result_frame,
                                     text=f'Resource Name:{resource_name} Server Name: {server_name} Database Name: {database_name} Status: {status}',
                                     font=('Ariel', 10, 'italic'))
        result_label.pack(pady=1)
    FINAL = DATABASE_STATUS
    return FINAL


window = tkinter.Tk()
window.geometry('1000x800')
img = ImageTk.PhotoImage(Image.open('logo.png'))
logo_container = tkinter.Frame(window, width=300, height=700)
label_image = tkinter.Label(logo_container, image=img)

logo_container.pack(side='top', fill='both')
label_image.pack()

token_subs_get = tkinter.Frame(window, width=300, height=300)
token_subs_get.pack(side='top', anchor='center', pady=10)
token_subs_get_label = tkinter.Label(token_subs_get, text='Please Enter your token and subs id: ',
                                     font=('Arierl', 12, 'bold'))
token_subs_get_label.pack()

entry_token_label = tkinter.Label(token_subs_get, text='Enter Token')
entry_token_label.pack()
entry_token = tkinter.Entry(token_subs_get, width=60)
entry_token.pack()

entry_subs_id_label = tkinter.Label(token_subs_get, text='Enter Subs Id')
entry_subs_id_label.pack(pady=10)
entry_subs_id = tkinter.Entry(token_subs_get, width=60)
entry_subs_id.pack(pady=10)

button_check_status = tkinter.Button(token_subs_get, text='Check', width=20)
button_check_status.pack(pady=10)
display_result_frame = tkinter.Frame(window, width=300, height=300)
display_result_frame.pack()
button_check_status['command'] = display_result
final = display_result
button_clear_display = tkinter.Button(window, text='Clear', width=20)
button_clear_display['command'] = clear_result
button_clear_display.pack(pady=10)

button_paused = tkinter.Button(window, text='Paused', width=20)
button_paused.pack(side='left', padx=20)
button_paused['command'] = pause_servers

button_resumed = tkinter.Button(window, text='Resume', width=20)
button_resumed.pack(side='right', padx=20)
button_resumed['command'] = resume_servers

window.mainloop()
