import tkinter as tk
import time
from rfid_mod import *
import imageio
from PIL import Image, ImageTk
import threading as thr
import time as ti
from tkinter import messagebox
azzedine = user(702455483582,"azzedine lakhdar",350)
houssam = user(659916243695,"houssam elhazami",9000000)
current_Promotions = 1000
products = ["chips","riz","coca-cola","Tide","chargeur","PC","Chwin-Gum","bouteille d'eau","isabelle","kiri","la vache qui rit","joli","oreo","mirindina","sidi ali"] 
number_of_articles=[]
number_of =0
tmp_text = ""
tmp_search=[]
for i in range(len(products)):
    number_of_articles.append(0)
products_selected = []   
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.shared_data = {'Promotions':tk.IntVar()}

        container = tk.Frame(self)
        container.pack()#side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, MenuPage, commanderPage, compte_infosPage, PromotionsPage,ConfirmationPage):
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
    def command(self,wind,product,entry,facture):
        amount = entry.get()
        global products_selected
        tmp_text = ""
        tmp_num = 0
        print("amount : ",str(amount))
        if amount=="":
            messagebox.showerror("entréé invalide", "vous n'avez pas entrer aucune valeur SVP entrez une valeur entier ")
            wind.destroy()
        else:
            try:
                if int(amount)!=0:
                    products_selected.append(product)
                    products_selected= list(set(products_selected))
                    number_of_articles[product] = amount
                    print("amount not zero")
                    wind.destroy()
                elif int(amount)==0:
                    number_of_articles[product] = 0
                    try:
                        products_selected.remove(products_selected[products_selected.index(int(product))])
                    except:
                        print("hola")
                    wind.destroy()
                    #global tmp_search
            except ValueError:
                messagebox.showerror("entréé invalide", "le nombre d'articles doit etre entier SVP reentrez un nombre")
                wind.destroy()
        tmp_search = []
        for i in products_selected:
            if (products[i] not in tmp_search):
                tmp_text = tmp_text + str(number_of_articles[i]) + "->"+products[i]+"\n"
                tmp_search.append(products[i])
        facture.set(tmp_text)
        #products_selected.sort()
        print("product selected from sampleApp ",products_selected,"\n")
        print("number of every article from SampleApp : ",number_of_articles,"\n")
        print("amount from SampleApp",amount,"\n")
    def enlever_article(self,product,wind,facture):
        number_of_articles[product] = 0
        try:
            products_selected.remove(products_selected[products_selected.index(int(product))])
        except:
            print("hola")
        wind.destroy()
        tmp_search = []
        tmp_text = ""
        for i in products_selected:
            if (products[i] not in tmp_search):
                tmp_text = tmp_text + str(number_of_articles[i]) + "->"+products[i]+"\n"
                tmp_search.append(products[i])
        facture.set(tmp_text)
    def new_window(self,i,facture):
        print("from new window : ",str(i))
        top = tk.Toplevel(self)
        top_frame = tk.Frame(top)
        label = tk.Label(top, text="entrez le nombre de "+products[i]+" que vous voullez")
        label.pack(side="top", fill="both", expand=True, padx=20, pady=20)
        mylabel = tk.Label(top,
                                                      text='Enter amount',
                                                      font=('orbitron',13))
        mylabel.pack(pady=10)
        enter_button = tk.Button(top,
                                                     text='confirmer',
                                                     command=lambda:self.command(top,i,myentry,facture),
                                                     relief='raised',
                                                     borderwidth=3,
                                                     width=40,
                                                     height=3)
        enter_button.pack(pady=10)
        enlever_button = tk.Button(top,
                                                     text='enlevez de mon panier',
                                                     command=lambda:self.enlever_article(i,top,facture),
                                                     relief='raised',
                                                     borderwidth=3,
                                                     width=40,
                                                     height=3)
        enlever_button.pack(pady=10)
        cash = tk.StringVar()
        myentry = tk.Entry(top,
                                                  textvariable=cash,
                                                  font=('orbitron',12),
                                                  width=22)
        myentry.pack(side="bottom",padx=20, pady=20)
        cash = myentry.get()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller
        self.controller.title('depot automatique')
        self.controller.state('normal')
        heading_label = tk.Label(self,text='depot automatique',font=('orbitron',45,'bold','italic'),foreground='#ffffff',background='#3d3d5c')
        heading_label.pack(pady=5)
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
                    img= Image.fromarray(image)
                    #Resize the Image using resize method
                    resized_image= img.resize((150,100), Image.ANTIALIAS)
                    frame_image = ImageTk.PhotoImage(resized_image)
                    label.config(image=frame_image)
                    label.image = frame_image
                    ti.sleep(0.006)
        #videoFrame = tk.Frame(self, relief='raised', borderwidth=5)
        #videoFrame.pack(expand=True, fill='both')
        #videoFrame.pack_propagate(0)
        my_label = tk.Label(self)
        my_label.pack()
        #global thread
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
        heading_label.pack(pady=5)

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
                                                            borderwidth=3)
        commander_button.grid(row=0,column=0,pady=5)

        def compte_infos():
            controller.show_frame('compte_infosPage')
            
        compte_infos_button = tk.Button(button_frame,
                                                            text='compte_infos',
                                                            command=compte_infos,
                                                            relief='raised',
                                                            borderwidth=3)
        compte_infos_button.grid(row=1,column=0,pady=5)

        def Promotions():
            controller.show_frame('PromotionsPage')
            
        Promotions_button = tk.Button(button_frame,
                                                            text='Promotions',
                                                            command=Promotions,
                                                            relief='raised',
                                                            borderwidth=3)
        Promotions_button.grid(row=2,column=0,pady=5)

        def exit():
            controller.show_frame('StartPage')
            
        
       
        exit_button = tk.Button(button_frame,
                                                            text='Exit',
                                                            command=exit,
                                                            relief='raised',
                                                            borderwidth=3)
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
        heading_label.pack(pady=5)

        choose_amount_label = tk.Label(self,
                                                           text='cliquez sur produit autant de fois que vous le voulez / cliquez sur enlevez le dernier article pour annuler le dernier article',
                                                           font=('orbitron',13),
                                                           fg='white',
                                                           bg='#3d3d5c')
        choose_amount_label.pack()
        #button_frame = tk.Frame(self,bg='#33334d')
        #button_frame.pack(fill='both',expand=True)
        master_frame = tk.Frame(self,bg='Light Blue', bd=9, relief=tk.RIDGE)
        master_frame.pack(fill="x",side = "left")
        side_frame = tk.Frame(self,bg='Light Blue', bd=9, relief=tk.RIDGE)
        side_frame.pack(fill="x",side="right")
        def confirmer():
            controller.show_frame('ConfirmationPage')
        confirm_button = tk.Button(side_frame,
                                                       text="confirmer",
                                                       command=lambda:confirmer(),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=20,
                                                       bg='blue',fg='white',
                                                       height=3)
        confirm_button.pack()
        drop_button = tk.Button(side_frame,
                                                       text="enlevez le dernier",
                                                       command=lambda:enlever(),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=20,
                                                       bg='blue',fg='white',
                                                       height=3)
        drop_button.pack()
        cancel_button = tk.Button(side_frame,
                                                       text="vider le panier",
                                                       command=lambda:clear(),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=20,
                                                       bg='blue',fg='white',
                                                       height=3)
        cancel_button.pack()
        exit_button= tk.Button(side_frame,
                                                       text="exit",
                                                       command=lambda:exit2(),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=20,
                                                       bg='blue',fg='white',
                                                       height=3)
        exit_button.pack()
        """drop_button = tk.Button(side_frame,
                                                       text="enlevez le dernier article",
                                                       command=lambda:commander(5),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=20,
                                                       bg='blue',fg='white',
                                                       height=3)
        drop_button.pack()"""
        commande_list_text = tk.StringVar()
        command_list = tk.Label(side_frame, textvariable=commande_list_text)
        command_list.pack()
        commande_list_text.set("your articles will be shown here")
        #cmd_frame = tk.Frame(self,bg='Light Blue', bd=3, relief=tk.RIDGE)
        #master_frame.columnconfigure(0, weight=1)
        def commander(product):
            controller.new_window(product,commande_list_text)
            """global products_selected
            products_selected.append(amount)
            products_selected= list(set(products_selected))
            tmp_text = ""
            tmp_num = 0
            #global tmp_search
            tmp_search = []
            number_of_articles[amount] = number_of_articles[amount]+1
            for i in products_selected:
                if (products[i] not in tmp_search):
                    tmp_text = tmp_text + str(number_of_articles[i]) + "->"+products[i]+"\n"
                    tmp_search.append(products[i])
            commande_list_text.set(tmp_text)
            #products_selected.sort()
            print(products_selected)
            print(number_of_articles)
            print(amount)"""
        def enlever():
            #print(products_selected)
            #print("product selected from commander page before remove : ",products_selected[len(products_selected)-1])
            number_of_articles[products_selected[len(products_selected)-1]] = 0
            products_selected.remove(products_selected[len(products_selected)-1])
            print("product selected from commander page after remove : ",products_selected,"\n")
            global tmp_text
            tmp_text = ""
            global tmp_search
            tmp_search = []
            for i in products_selected:
                if (products[i] not in tmp_search):
                    tmp_text = tmp_text + str(number_of_articles[i]) + "->"+products[i]+"\n"
                    tmp_search.append(products[i])
            commande_list_text.set(tmp_text)
        
        
        def clear():
            del products_selected[:]
            del number_of_articles[:]
            for i in range(len(products)):
                number_of_articles.append(0)
            commande_list_text.set("your articles will be shown here")
        
        def exit2():
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
        #yscrollbar = tk.Scrollbar(canvas)
        #yscrollbar.pack( side = "right", fill = "y" )
        ROWS=len(products)
        COLS=3
        # Add the buttons to the frame.
        row_selected =0
        for i in range(0, int(ROWS)):
            if i%3 == 0:
                buttons_first_row = tk.Button(button_frame,
                                                                       text=products[i],
                                                                       command=lambda i=i:commander(int(i)),
                                                                       relief='raised',
                                                                       borderwidth=3)
                buttons_first_row.grid(row=row_selected,column=0,pady=10)
            elif i%3 == 1:
                buttons_second_row = tk.Button(button_frame,
                                                                       text=products[i],
                                                                       command=lambda i=i:commander(int(i)),
                                                                       relief='raised',
                                                                       borderwidth=3)
                buttons_second_row.grid(row=row_selected,column=1,pady=10)
            elif i%3 == 2:
                buttons_third_row = tk.Button(button_frame,
                                                                       text=products[i],
                                                                       command=lambda i=i:commander(int(i)),
                                                                       relief='raised',
                                                                       borderwidth=3)
                buttons_third_row.grid(row=row_selected,column=2,pady=10)
                row_selected=row_selected+1

        # Create canvas window to hold the buttons_frame.
        canvas.create_window((0,0), window=button_frame, anchor=tk.NW)
        #yscrollbar.config( command = canvas.yview)
        button_frame.update_idletasks()  # Needed to make bbox info available.
        bbox = canvas.bbox(tk.ALL)  # Get bounding box of canvas with Buttons.
        ROWS_DISP = 9  # Number of rows to display.
        COLS_DISP = 3  # Number of columns to display.
        # Define the scrollable region as entire canvas with only the desired
        # number of rows and columns displayed.
        w, h = bbox[2]-bbox[1], bbox[3]-bbox[1]
        dw, dh = int((w/COLS) * COLS_DISP), int((h/ROWS) * ROWS_DISP)
        canvas.configure(scrollregion=bbox, width=dw, height=dh,yscrollcommand=vsbar.set)

        """def other_amount(_):
            global current_Promotions
            current_Promotions -= int(cash.get())
            controller.shared_data['Promotions'].set(current_Promotions)
            cash.set('')
            controller.show_frame('MenuPage')
            
        other_amount_entry.bind('<Return>',other_amount)"""

        """bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
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

        tick()"""
   

class ConfirmationPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller
        
        heading_label = tk.Label(self,
                                                     text='depot automatique',
                                                     font=('orbitron',45,'bold'),
                                                     foreground='#ffffff',
                                                     background='#3d3d5c')
        heading_label.pack(pady=5)

        space_label = tk.Label(self,height=4,bg='#3d3d5c')
        space_label.pack()
        #global tmp_text
        for i in products_selected:
            if (products[i] not in tmp_search):
                tmp_text = tmp_text + str(number_of_articles[i]) + "->"+products[i]+"\n"
                tmp_search.append(products[i])
            print("from confirmation page")
        cash = tk.StringVar()
        commande_list_text1 = tk.StringVar()
        command_list1 = tk.Label(self, textvariable=commande_list_text1)
        command_list1.pack()
        commande_list_text1.set(tmp_text)
        #global tmp_text
        #global tmp_search
        print("product selected : ",products_selected)
        #commande_list_text.set(tmp_text)

        def compte_infos_cash():
            global current_Promotions
            current_Promotions += int(cash.get())
            controller.shared_data['Promotions'].set(current_Promotions)
            controller.show_frame('MenuPage')
            cash.set('')
        #global tmp_search
        def show_facture():
            for i in products_selected:
                if (products[i] not in tmp_search):
                    tmp_text = tmp_text + str(number_of_articles[i]) + "->"+products[i]+"\n"
                    tmp_search.append(products[i])
            print( "745896",tmp_text,"\n")
            
        enter_button = tk.Button(self,
                                                     text='afficher ma facture',
                                                     command=show_facture,
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
class compte_infosPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller
        
        heading_label = tk.Label(self,
                                                     text='depot automatique',
                                                     font=('orbitron',45,'bold'),
                                                     foreground='#ffffff',
                                                     background='#3d3d5c')
        heading_label.pack(pady=5)

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
                                                     borderwidth=3)
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
        heading_label.pack(pady=5)

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
                                                    borderwidth=3)
        menu_button.grid(row=0,column=0,pady=5)

        def exit():
            controller.show_frame('StartPage')
            
        exit_button = tk.Button(button_frame,
                                                 text='Exit',
                                                 command=exit,
                                                 relief='raised',
                                                 borderwidth=3)
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
    #root = tk.Tk()               #Bind Tkinter to the root object
    app.geometry('800x480')
    app.mainloop()
