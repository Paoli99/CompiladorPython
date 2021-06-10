from tkinter import * 
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from config import default 

import lexer 

config = default 
window = tk.Tk()
window.title("Compilador")
window.config(bg = 'white')
window.geometry(f'{config["reference_width"] + 30}x{config["reference_height"]+230}')
window.wm_maxsize(config["reference_width"] + 30, config["reference_height"]+230)


ttk.Label(window,
		text = "Compilador",
		font = ("Times New Roman", 15),).grid(column = 0,row = 0)


def click():
	errorCanvas.delete("all") 
	code = codeText.get('1.0', 'end-1c')   
	print(code)

	#text = input('basic > ')
	result, error = lexer.run('<archivo>', code)

	if error: 
		print(error.as_string())
		errorMessage = error.as_string()

		#lista.insert(lista.index('end'), str(errorMessage))
		errorCanvas.create_text(200,100, text = errorMessage)
	else: 
		print(result)
		results = result 
		errorCanvas.create_text(200,80, text = 'Analisis correcto!')
		errorCanvas.create_text(200,100, text = results)

def abrirTxt():
    pass 

codeText = scrolledtext.ScrolledText(window,
									wrap = tk.WORD,
									width = int(config["reference_width"]),
									height = 20,
									font = ("Times New Roman",
											10))

codeText.grid(row = 1, column = 0, pady = 10, padx = 10)
codeText.columnconfigure(0, weight=1)
codeText.columnconfigure(1, weight=3)



errorFrame= Frame(window, width = int(config["reference_width"]), height= int(config["reference_height"]),  bg = "black")
errorFrame.grid(row = 2, column = 0, sticky="EWNS")
errorCanvas = Canvas(errorFrame, bg = "light gray", width = int(config["reference_width"]), height= int(config["reference_height"]))
errorCanvas.grid(row = 2, column = 0, sticky="EWNS")


tool_bar_frame = Frame(window, width = 40, height = 10, bg = config["color_bg_general"] )
tool_bar_frame.grid(row = 0, column = 0, sticky=W)

btnRun = Button(tool_bar_frame, text = 'Run Code',  font= config["fuente_fields"], command = click, bg = config["color_bg_botones"], fg=config["color_letra_botones"])
btnRun.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = W)

btnOpenTxt = Button(tool_bar_frame, text = 'Abrir archivo', font= config["fuente_fields"], command = abrirTxt, bg = config["color_bg_botones"], fg=config["color_letra_botones"])
btnOpenTxt.grid(row = 0, column = 3, padx = 5, pady = 5, sticky = W)


codeText.focus()
window.mainloop()