try:
    from Tkinter import Tk, END
    import ttk
    import tkMessageBox as message
except ImportError:
    from tkinter import Tk, END
    from tkinter import messagebox as message
    from tkinter import ttk
import json
import keygen

class RootWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        f0 = ttk.Frame(self)
        f1 = ttk.Frame(self)
        f2 = ttk.Frame(self)
        f3 = ttk.Frame(self)
        f4 = ttk.Frame(self)
        f5 = ttk.Frame(self)
        f6 = ttk.Frame(self)
        f7 = ttk.Frame(self)
        f8 = ttk.Frame(self)
        self.password_choices = ['mypass',]
        ttk.Label(f0, text='Kii U Generator', font='Helvetica 20 bold').pack(side='left', padx=10, pady=10)
        ttk.Label(f1, text='Input:', font='Helvetica 16 bold').pack(side='left', padx=10, pady=(10,0))
        ttk.Label(f2, text='Title id:').pack(side='left', padx=10, pady=10)
        self.enter_tid = ttk.Entry(f2, width=20)
        self.enter_tid.pack(side='left', padx=10, pady=10)
        ttk.Label(f3, text='Common key:').pack(side='left', padx=10, pady=10)
        self.enter_ckey = ttk.Entry(f3, width=35)
        self.enter_ckey.pack(side='left', padx=10, pady=10)
        ttk.Button(f3, text='Save', command=self.save_ckey).pack(padx=5, pady=10)
        ttk.Label(f4, text='Password:').pack(side='left', padx=10, pady=10)
        self.enter_pwd = ttk.Combobox(f4, values=self.password_choices)
        self.enter_pwd.set('mypass')
        self.enter_pwd.pack(side='left', padx=10, pady=10)
        ttk.Button(f5, text='Generate title key', command=self.generate_clicked).pack(padx=10, pady=10)
        ttk.Label(f6, text='Generated keys:', font='Helvetica 16 bold').pack(side='left', padx=10, pady=(10,0))
        ttk.Label(f7, text='Unencrypted title key:', font='Helvetica 11 bold').pack(side='left', padx=10, pady=10)
        self.unencrypted_box = ttk.Entry(f7, width=35)
        self.unencrypted_box.pack(side='left', padx=10, pady=10)
        ttk.Label(f8, text='Encrypted title key:', font='Helvetica 11 bold').pack(side='left', padx=10, pady=10)
        self.encrypted_box = ttk.Entry(f8, width=35)
        self.encrypted_box.pack(side='left', padx=10, pady=10)
        try:
            self.enter_ckey.insert(END, keygen.get_ckey())
        except:
            pass
        f0.pack(anchor='center')
        f1.pack(anchor='w')
        f2.pack(anchor='w')
        f3.pack(anchor='w')
        f4.pack(anchor='w')
        f5.pack(anchor='w')
        f6.pack(anchor='w')
        f7.pack(anchor='w')
        f8.pack(anchor='w')

    def generate_clicked(self):
        ckey = self.enter_ckey.get().strip()
        if not keygen.verify_ckey(ckey):
            message.showerror('ERROR', 'Incorrect common key found. Please add the correct key to the common key input field. Key must be plaintext.')
            return
        tid = self.enter_tid.get().replace('-','')
        pwd = self.enter_pwd.get().strip()
        keys = keygen.main(tid, ckey, pwd)
        self.unencrypted_box.delete('0', END)
        self.encrypted_box.delete('0', END)
        self.encrypted_box.insert(END, keys[0])
        self.unencrypted_box.insert(END, keys[1])

    def save_ckey(self):
        with open('ckey.json', 'w') as f:
            json.dump({'commonkey': self.enter_ckey.get()}, f)



root = RootWindow()
root.title('Kii U Generator')
root.mainloop()
        
                    
