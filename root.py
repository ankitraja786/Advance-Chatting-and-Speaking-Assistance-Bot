from tkinter import*

root = Tk() 	# Object of TK class
root.configure(bg = 'red')
root.title('Advance Chat Bot Application')
root.geometry('400x500') 	# size of window

main_menu = Menu(root) 		# Main Menu
file_menu = Menu(root)		# Sub Menu in File

file_menu.add_command(label = 'New')
file_menu.add_command(label = 'Save As')
file_menu.add_command(label = 'Exit')

main_menu.add_cascade(label = 'File', menu = file_menu)
main_menu.add_command(label = 'Edit')
main_menu.add_command(label = 'Quit')
root.config(menu = main_menu)

chat_window = Text(root, bd = 1, bg = 'black', width = 50, height = 8)
chat_window.place(x = 6, y = 6, height = 385, width = 370)

message_window = Text(root, bg = 'black', width = 30, height = 4)
message_window.place(x = 128, y = 400, height = 88, width = 260)

button = Button(root, text = 'Send', bg = 'blue', activebackground = 'green',
				   width = 12, height = 5, font = ('Arial', 20), fg = 'white')
button.place(x = 6, y = 400, height = 88, width = 120)

scroll_bar = Scrollbar(root, command = chat_window.yview())
scroll_bar.place(x = 375, y = 5, height = 385)

root.mainloop()