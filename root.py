from tkinter import *

def reply():
	question = message_window.get()
	chat_window.insert(END, "You : "+ question + '\n')
	message_window.delete(0, END)

def Quit():
	global root
	root.quit()

root = Tk() 	# Object of TK class
root.configure(bg = 'green')
root.title('Advance Chat Bot Application')
root.geometry('400x550') 	# size of window

main_menu = Menu(root) 		# Main Menu

main_menu.add_command(label = 'Quit', command = Quit)
root.config(menu = main_menu)

chat_window = Text(root, bd = 1, bg = 'black', fg = 'white',font = ('times new roman', 20),
			  width = 50, height = 8, wrap = 'word')
chat_window.place(x = 6, y = 6, height = 385, width = 370)

message_window = Entry(root, font = ('verdana', 20,'bold'), bg = 'purple', fg = 'yellow')
message_window.place(x = 10, y = 405, height = 50, width = 380)

src = PhotoImage(file = 'image.png')
button = Button(root, image = src,
				   width = 12, height = 5, font = ('Arial', 20), fg = 'white', command = reply)
button.place(x = 150, y = 470, height = 70, width = 90)

scroll_bar = Scrollbar(root, command = chat_window.yview())
scroll_bar.place(x = 375, y = 5, height = 385)

root.mainloop()