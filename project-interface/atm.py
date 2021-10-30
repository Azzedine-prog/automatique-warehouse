import tkinter as tk
import time
import imageio
from PIL import Image, ImageTk
import threading as thr
import time as ti
current_Promotions = 1000
products = ["chips","riz","coca-cola","Tide","chargeur","PC","Chwin-Gum","bouteille d'eau","isabelle","kiri","la vache qui rit","joli","oreo","mirindina","sidi ali"] 
products_selected = []
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.shared_data = {'Promotions':tk.IntVar()}

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, MenuPage, commanderPage, compte_infosPage, PromotionsPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller
        self.controller.title('depot automatique')
        self.controller.state('zoomed')
        heading_label = tk.Label(self,text='depot automatique',font=('orbitron',45,'bold','italic'),foreground='#ffffff',background='#3d3d5c')
        heading_label.pack(pady=25)
        space_label = tk.Label(self,height=4,bg='#3d3d5c')
        space_label.pack()
        video_name = "Creditcard.mp4" #This is your video file path
        video = imageio.get_reader(video_name)
        """img_array = []
        for image in video.iter_data():
            img_array.append(Image.fromarray(image))"""
        def stream(label):
            #print(img_array)
            while True:
                for image in video.iter_data():
                    #Load an image in the script
                    #img= Image.fromarray(image)
                    #Resize the Image using resize method
                    #resized_image= img.resize((640,360), Image.ANTIALIAS)
                    frame_image = ImageTk.PhotoImage(Image.fromarray(image))
                    label.config(image=frame_image)
                    label.image = frame_image
                    ti.sleep(0.006)
        #videoFrame = tk.Frame(self, relief='raised', borderwidth=5)
        #videoFrame.pack(expand=True, fill='both')
        #videoFrame.pack_propagate(0)
        my_label = tk.Label(self)
        my_label.pack()
        thread = thr.Thread(target=stream, args=(my_label,))
        thread.daemon = 1
        thread.start()
        def check_Rfid():
            controller.show_frame('MenuPage')      
               
        enter_button = tk.Button(self,text='Enter',command=check_Rfid,relief='raised',borderwidth = 3,width=40,height=3)
        enter_button.pack(pady=10)

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='mastercard.png')
        mastercard_label = tk.Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        american_express_photo = tk.PhotoImage(file='american-express.png')
        american_express_label = tk.Label(bottom_frame,image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image = american_express_photo

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)   
        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')
        tick()
        


class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller
   
        heading_label = tk.Label(self,
                                                     text='depot automatique',
                                                     font=('orbitron',45,'bold'),
                                                     foreground='#ffffff',
                                                     background='#3d3d5c')
        heading_label.pack(pady=25)

        main_menu_label = tk.Label(self,
                                                           text='Main Menu',
                                                           font=('orbitron',13),
                                                           fg='white',
                                                           bg='#3d3d5c')
        main_menu_label.pack()

        selection_label = tk.Label(self,
                                                           text='Please make a selection',
                                                           font=('orbitron',13),
                                                           fg='white',
                                                           bg='#3d3d5c',
                                                           anchor='w')
        selection_label.pack(fill='x')

        button_frame = tk.Frame(self,bg='#33334d')
        button_frame.pack(fill='both',expand=True)

        def commander():
            controller.show_frame('commanderPage')
            
        commander_button = tk.Button(button_frame,
                                                            text='commander',
                                                            command=commander,
                                                            relief='raised',
                                                            borderwidth=3,
                                                            width=50,
                                                            height=5)
        commander_button.grid(row=0,column=0,pady=5)

        def compte_infos():
            controller.show_frame('compte_infosPage')
            
        compte_infos_button = tk.Button(button_frame,
                                                            text='compte_infos',
                                                            command=compte_infos,
                                                            relief='raised',
                                                            borderwidth=3,
                                                            width=50,
                                                            height=5)
        compte_infos_button.grid(row=1,column=0,pady=5)

        def Promotions():
            controller.show_frame('PromotionsPage')
            
        Promotions_button = tk.Button(button_frame,
                                                            text='Promotions',
                                                            command=Promotions,
                                                            relief='raised',
                                                            borderwidth=3,
                                                            width=50,
                                                            height=5)
        Promotions_button.grid(row=2,column=0,pady=5)

        def exit():
            controller.show_frame('StartPage')
            
        
       
        exit_button = tk.Button(button_frame,
                                                            text='Exit',
                                                            command=exit,
                                                            relief='raised',
                                                            borderwidth=3,
                                                            width=50,
                                                            height=5)
        exit_button.grid(row=3,column=0,pady=5)


        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='mastercard.png')
        mastercard_label = tk.Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        american_express_photo = tk.PhotoImage(file='american-express.png')
        american_express_label = tk.Label(bottom_frame,image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image = american_express_photo

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')

        tick()


class commanderPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller


        heading_label = tk.Label(self,
                                                     text='depot automatique',
                                                     font=('orbitron',45,'bold'),
                                                     foreground='#ffffff',
                                                     background='#3d3d5c')
        heading_label.pack(pady=25)

        choose_amount_label = tk.Label(self,
                                                           text='Choose the amount you want to commander',
                                                           font=('orbitron',13),
                                                           fg='white',
                                                           bg='#3d3d5c')
        choose_amount_label.pack()

        #button_frame = tk.Frame(self,bg='#33334d')
        #button_frame.pack(fill='both',expand=True)
        master_frame = tk.Frame(self,bg='Light Blue', bd=3, relief=tk.RIDGE)
        master_frame.pack(fill='both',expand=True)
        #master_frame.columnconfigure(0, weight=1)
        def commander(amount):
            global current_Promotions
            current_Promotions -= amount
            controller.shared_data['Promotions'].set(current_Promotions)
            controller.show_frame('MenuPage')
        # Create a frame for the canvas and scrollbar(s).
        #frame2 = tk.Frame(master_frame, bg='Red', bd=2, relief=tk.FLAT)
        #frame2.pack(fill='both',expand=True)

        # Add a canvas in that frame.
        canvas = tk.Canvas(master_frame, bg='Yellow')
        canvas.grid(row=0, column=0,sticky="NSEW")
        #canvas.config(width=200, height=200)

        # Create a vertical scrollbar linked to the canvas.
        vsbar = tk.Scrollbar(master_frame, orient=tk.VERTICAL, command=canvas.yview)
        #vsbar = tk.Scrollbar(frame2, orient=tk.VERTICAL, command=canvas.yview)
        vsbar.grid(row=0, column=10, sticky="NSEW")
        #canvas.configure(yscrollcommand=vsbar.set)

        # Create a horizontal scrollbar linked to the canvas.
        """hsbar = tk.Scrollbar(master_frame, orient=tk.HORIZONTAL, command=canvas.xview)
        hsbar.grid(row=1, column=0, sticky=tk.EW)
        canvas.configure(xscrollcommand=hsbar.set)"""

        # Create a frame on the canvas to contain the grid of buttons.
        button_frame = tk.Frame(canvas)
        ROWS=len(products)
        COLS=3
        # Add the buttons to the frame.
        for i in range(0, int(ROWS)):
            if i%3 == 0:
                three_hundred_button = tk.Button(button_frame,
                                                                       text=products[i],
                                                                       command=lambda:commander(300),
                                                                       relief='raised',
                                                                       borderwidth=3,
                                                                       width=50,
                                                                       height=5)
                three_hundred_button.grid(row=0,column=0,pady=10)
            elif i%3 == 1:
                three_hundred_button = tk.Button(button_frame,
                                                                       text=products[i],
                                                                       command=lambda:commander(300),
                                                                       relief='raised',
                                                                       borderwidth=3,
                                                                       width=50,
                                                                       height=5)
                three_hundred_button.grid(row=int(i),column=1,pady=10)
            elif i%3 == 2:
                three_hundred_button = tk.Button(button_frame,
                                                                       text=products[i],
                                                                       command=lambda:commander(300),
                                                                       relief='raised',
                                                                       borderwidth=3,
                                                                       width=50,
                                                                       height=5)
                three_hundred_button.grid(row=int(i),column=2,pady=10)

        # Create canvas window to hold the buttons_frame.
        canvas.create_window((0,0), window=button_frame, anchor=tk.NW)

        button_frame.update_idletasks()  # Needed to make bbox info available.
        bbox = canvas.bbox(tk.ALL)  # Get bounding box of canvas with Buttons.
        ROWS_DISP = 4  # Number of rows to display.
        COLS_DISP = 3  # Number of columns to display.
        # Define the scrollable region as entire canvas with only the desired
        # number of rows and columns displayed.
        w, h = bbox[2]-bbox[1], bbox[3]-bbox[1]
        dw, dh = int((w/COLS) * COLS_DISP), int((h/ROWS) * ROWS_DISP)
        canvas.configure(scrollregion=bbox, width=dw, height=dh)

        """def other_amount(_):
            global current_Promotions
            current_Promotions -= int(cash.get())
            controller.shared_data['Promotions'].set(current_Promotions)
            cash.set('')
            controller.show_frame('MenuPage')
            
        other_amount_entry.bind('<Return>',other_amount)"""

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='mastercard.png')
        mastercard_label = tk.Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        american_express_photo = tk.PhotoImage(file='american-express.png')
        american_express_label = tk.Label(bottom_frame,image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image = american_express_photo

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')

        tick()
   

class compte_infosPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller

        heading_label = tk.Label(self,
                                                     text='depot automatique',
                                                     font=('orbitron',45,'bold'),
                                                     foreground='#ffffff',
                                                     background='#3d3d5c')
        heading_label.pack(pady=25)

        space_label = tk.Label(self,height=4,bg='#3d3d5c')
        space_label.pack()

        enter_amount_label = tk.Label(self,
                                                      text='Enter amount',
                                                      font=('orbitron',13),
                                                      bg='#3d3d5c',
                                                      fg='white')
        enter_amount_label.pack(pady=10)

        cash = tk.StringVar()
        compte_infos_entry = tk.Entry(self,
                                                  textvariable=cash,
                                                  font=('orbitron',12),
                                                  width=22)
        compte_infos_entry.pack(ipady=7)

        def compte_infos_cash():
            global current_Promotions
            current_Promotions += int(cash.get())
            controller.shared_data['Promotions'].set(current_Promotions)
            controller.show_frame('MenuPage')
            cash.set('')
            
        enter_button = tk.Button(self,
                                                     text='Enter',
                                                     command=compte_infos_cash,
                                                     relief='raised',
                                                     borderwidth=3,
                                                     width=40,
                                                     height=3)
        enter_button.pack(pady=10)

        two_tone_label = tk.Label(self,bg='#33334d')
        two_tone_label.pack(fill='both',expand=True)

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='mastercard.png')
        mastercard_label = tk.Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        american_express_photo = tk.PhotoImage(file='american-express.png')
        american_express_label = tk.Label(bottom_frame,image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image = american_express_photo

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')

        tick()


class PromotionsPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller

        
        heading_label = tk.Label(self,
                                                     text='depot automatique',
                                                     font=('orbitron',45,'bold'),
                                                     foreground='#ffffff',
                                                     background='#3d3d5c')
        heading_label.pack(pady=25)

        global current_Promotions
        controller.shared_data['Promotions'].set(current_Promotions)
        Promotions_label = tk.Label(self,
                                                  textvariable=controller.shared_data['Promotions'],
                                                  font=('orbitron',13),
                                                  fg='white',
                                                  bg='#3d3d5c',
                                                  anchor='w')
        Promotions_label.pack(fill='x')

        button_frame = tk.Frame(self,bg='#33334d')
        button_frame.pack(fill='both',expand=True)

        def menu():
            controller.show_frame('MenuPage')
            
        menu_button = tk.Button(button_frame,
                                                    command=menu,
                                                    text='Menu',
                                                    relief='raised',
                                                    borderwidth=3,
                                                    width=50,
                                                    height=5)
        menu_button.grid(row=0,column=0,pady=5)

        def exit():
            controller.show_frame('StartPage')
            
        exit_button = tk.Button(button_frame,
                                                 text='Exit',
                                                 command=exit,
                                                 relief='raised',
                                                 borderwidth=3,
                                                 width=50,
                                                 height=5)
        exit_button.grid(row=1,column=0,pady=5)

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='mastercard.png')
        mastercard_label = tk.Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        american_express_photo = tk.PhotoImage(file='american-express.png')
        american_express_label = tk.Label(bottom_frame,image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image = american_express_photo

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')

        tick()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
