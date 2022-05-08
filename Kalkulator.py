import PySimpleGUI as sg

def create(theme):
    sg.theme(theme)
    sg.set_options(font= 'Arial 35', button_element_size=(2,1))
    button_size = (2,1)
    layout = [
         [sg.Text('Output',
                  font= 'Arial 40',
                  justification='right',
                  expand_x= True,
                  pad= (5,10),
                  right_click_menu = theme_menu,
                  key= '-TEXT-',
                  )
          ],
         [sg.Button('Clear', expand_x= True), sg.Button('Enter', expand_x= True)],
         [sg.Button(7, size = button_size),sg.Button(8, size = button_size), sg.Button(9, size = button_size), sg.Button('*', size= (3,1))],
         [sg.Button(4, size = button_size), sg.Button(5, size = button_size), sg.Button(6, size = button_size), sg.Button('/', size= (3,1))],
         [sg.Button(1, size = button_size), sg.Button(2, size = button_size), sg.Button(3, size = button_size), sg.Button('-',size= (3,1))],
         [sg.Button(0, size = button_size), sg.Button('.', size = (3,1)), sg.Button('+', expand_x= True)],
      ]
    return sg.Window('Calculator',layout)
theme_menu = ['Menu',['Black','Blue','DarkGrey8','Random']]
window = create('Purple')
current_num = []
full_operation = []
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        window.close()
        window = create(event)
    if event in ['0','1','2','3','4','5','6','7','8','9','.']:
        current_num.append(event)
        num_string = ''.join(current_num)
        window['-TEXT-'].update(num_string)
    if event in ['+','-','/','*']:
        full_operation.append(''.join(current_num))
        current_num = []
        full_operation.append(event)
        window['-TEXT-'].update('')
    if event == 'Enter':
        full_operation.append(''.join(current_num))
        result = eval(''.join(full_operation))
        window['-TEXT-'].update(result)
        full_operation = []

    if event == 'Clear':
        current_num = []
        full_operation = []
        window['-TEXT-'].update('')

window.close()