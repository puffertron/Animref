import tkinter as tk

root = tk.Tk()

root.title('AnimRef')

window_w = 700
window_h = 200

center_x = int(root.winfo_screenwidth() / 2  - window_w / 2)
center_y = int(root.winfo_screenheight() / 2 - window_h / 2)


root.geometry(f"{window_w}x{window_h}+{center_x}+{center_y}")
root.mainloop()

