from tkinter import *
import random,os
from tkinter import messagebox

class Bill_app:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1350x700+0+0')
        self.root.title('Billing software')
        
        title=Label(self.root,text="BILLING SOFTWARE",bd=12,relief=GROOVE,bg='Black',fg='white',font=('times new roman',30,'bold'),pady=2).pack(fill=X)
        #==============variables===========
        #--------cosmetics-------------------------
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.shampu=IntVar()
        self.gel=IntVar()
        self.loshan=IntVar()

        #--------grocery-------------------------
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()

        #--------cold drink-------------------------
        self.maza=IntVar()
        self.cock=IntVar()
        self.frooti=IntVar()
        self.thumbsup=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()

        #---------total product price and taxes
        self.cosmetic_price=StringVar()
        self.glocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.glocery_tax=StringVar()
        self.cold_drink_tax=StringVar()

        #------costumer--------
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()

        
        #===============custermer info fram===============
        F1=LabelFrame(self.root,text="Customer Information",bd=7,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg="Black")
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name:",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)
        
        cphone_lbl=Label(F1,text="Phone No:",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphone_txt=Entry(F1,width=15,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5)
 
        cbill_lbl=Label(F1,text="Bill No:",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        cbill_txt=Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=5)
        
        search_button=Button(F1,text="Search",command=self.find_bill, font=("times new roman",18,"bold"),bd=7,relief=SUNKEN,bg="blue",fg="white").grid(row=0,column=6,padx=20,pady=5)

        #===============Cosmetic  fram===============
        F2=LabelFrame(self.root,text="Consmetic",bd=7,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg="Black")
        F2.place(x=5,y=180,width=325,height=380)

        bath_lbl=Label(F2,text="Bath Soap:",font=("times new roman",15,"bold"),bg="Black",fg="lightgrey").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Face_cream_lbl=Label(F2,text="Face cream:",font=("times new roman",15,"bold"),bg="Black",fg="lightgrey").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Face_cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        
        Face_w_lbl=Label(F2,text="Face Wash:",font=("times new roman",15,"bold"),bg="Black",fg="lightgrey").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Face_w_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Hair_s_lbl=Label(F2,text="Hair Shampu:",font=("times new roman",15,"bold"),bg="Black",fg="lightgrey").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Hair_s_txt=Entry(F2,width=10,textvariable=self.shampu,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Hair_g_lbl=Label(F2,text="Hair Gel:",font=("times new roman",15,"bold"),bg="Black",fg="lightgrey").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Hair_g_txt=Entry(F2,width=10,textvariable=self.gel,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Body_lbl=Label(F2,text="Body Loshan:",font=("times new roman",15,"bold"),bg="Black",fg="lightgrey").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Body_txt=Entry(F2,width=10,textvariable=self.loshan,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #===============Grocery fram===============
        F3=LabelFrame(self.root,text="Grocery",bd=7,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg="Black")
        F3.place(x=330,y=180,width=325,height=380)

        Rice_lbl=Label(F3,text="Rice:",font=("times new roman",15,"bold"),bg="Black",fg="lightgrey").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Rice_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Food_oil_lbl=Label(F3,text="Food oil:",font=("times new roman",15,"bold"),bg="Black",fg="lightgrey").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Food_oil_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        
        Daal_lbl=Label(F3,text="Daal:",font=("times new roman",15,"bold"),bg="Black",fg="lightgrey").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Daal_txt=Entry(F3,width=10,textvariable=self.daal,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Wheat_lbl=Label(F3,text="Wheat:",font=("times new roman",15,"bold"),bg="Black",fg="lightgrey").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Wheat_txt=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Sugar_lbl=Label(F3,text="Sugar:",font=("times new roman",15,"bold"),bg="Black",fg="lightgrey").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Sugar_txt=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Tea_lbl=Label(F3,text="Tea:",font=("times new roman",15,"bold"),bg="Black",fg="lightgrey").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Tea_txt=Entry(F3,width=10,textvariable=self.tea,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


        #===============Coldrink fram===============
        F4=LabelFrame(self.root,text="Coldrink",bd=7,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg="Black")
        F4.place(x=655,y=180,width=325,height=380)

        Maza_lbl=Label(F4,text="Maza:",font=("times new roman",15,"bold"),bg="Black",fg="lightgrey").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Maza_txt=Entry(F4,width=10,textvariable=self.maza,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Cock_lbl=Label(F4,text="Cock:",font=("times new roman",15,"bold"),bg="Black",fg="lightgrey").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Cock_txt=Entry(F4,width=10,textvariable=self.cock,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        
        Frooti_lbl=Label(F4,text="Frooti:",font=("times new roman",15,"bold"),bg="Black",fg="lightgrey").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Frooti_txt=Entry(F4,width=10,textvariable=self.frooti,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Thumps_up_lbl=Label(F4,text="Thumps up:",font=("times new roman",15,"bold"),bg="Black",fg="lightgrey").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Thumps_up_txt=Entry(F4,width=10,textvariable=self.thumbsup,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Limca_lbl=Label(F4,text="Limca:",font=("times new roman",15,"bold"),bg="Black",fg="lightgrey").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Limca_txt=Entry(F4,width=10,textvariable=self.limca,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Sprite_lbl=Label(F4,text="Sprite:",font=("times new roman",15,"bold"),bg="Black",fg="lightgrey").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Sprite_txt=Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",15,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #===============Bill area fram===============
        F5=Frame(self.root,bd=7,relief=GROOVE)
        F5.place(x=1000,y=180,width=345,height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.textarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #===============menu fram=============
        F6=LabelFrame(self.root,text="Bill Menu",bd=7,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg="Black")
        F6.place(x=0,y=560,relwidth=1,height=140)

        m1_lbl=Label(F6,text="Total Cosmetic Cost:",font=("times new roman",12,"bold")).grid(row=0,column=0,padx=20,pady=5,sticky="w")
        m1_txt=Entry(F6,width=20,textvariable=self.cosmetic_price,font=("times new roman",12,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl=Label(F6,text="Total Glocery Cost:",font=("times new roman",12,"bold")).grid(row=1,column=0,padx=20,pady=5,sticky="w")
        m2_txt=Entry(F6,width=20,textvariable=self.glocery_price,font=("times new roman",12,"bold"),bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl=Label(F6,text="Total Cold drink Cost:",font=("times new roman",12,"bold")).grid(row=2,column=0,padx=20,pady=5,sticky="w")
        m3_txt=Entry(F6,width=20,textvariable=self.cold_drink_price,font=("times new roman",12,"bold"),bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        c1_lbl=Label(F6,text=" Cosmetic Taxes:",font=("times new roman",12,"bold")).grid(row=0,column=2,padx=20,pady=5,sticky="w")
        c1_txt=Entry(F6,width=20,textvariable=self.cosmetic_tax,font=("times new roman",12,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2_lbl=Label(F6,text="Glocery Taxes:",font=("times new roman",12,"bold")).grid(row=1,column=2,padx=20,pady=5,sticky="w")
        c2_txt=Entry(F6,width=20,textvariable=self.glocery_tax,font=("times new roman",12,"bold"),bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3_lbl=Label(F6,text="Cold drink Taxes:",font=("times new roman",12,"bold")).grid(row=2,column=2,padx=20,pady=5,sticky="w")
        c3_txt=Entry(F6,width=20,textvariable=self.cold_drink_tax,font=("times new roman",12,"bold"),bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        #===============Button fram=============
        btn_f=Frame(F6,bd=7,relief=GROOVE)
        btn_f.place(x=750,y=0,width=580,height=105)

        total_button=Button(btn_f,command=self.total, text="Total",font=("times new roman",18,"bold"),bd=7,relief=SUNKEN,bg="blue",fg="white").grid(row=0,column=0,padx=20,pady=5)

        GBill_button=Button(btn_f,command=self.bill_area,text="Genrate Bill",font=("times new roman",18,"bold"),bd=7,relief=SUNKEN,bg="blue",fg="white").grid(row=0,column=1,padx=20,pady=5)

        clr_button=Button(btn_f,text="Clear",command=self.clear_data,font=("times new roman",18,"bold"),bd=7,relief=SUNKEN,bg="blue",fg="white").grid(row=0,column=2,padx=20,pady=5)

        exit_button=Button(btn_f,text="Exit",command=self.exit_app,font=("times new roman",18,"bold"),bd=7,relief=SUNKEN,bg="blue",fg="white").grid(row=0,column=3,padx=20,pady=5)
        self.welcome_bill()
           
    def total(self):
        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*120
        self.c_fw_p=self.face_wash.get()*60
        self.c_hs_p=self.shampu.get()*180
        self.c_hg_p=self.gel.get()*140
        self.c_bl_p=self.loshan.get()*180

        self.g_r_p=self.rice.get()*100
        self.g_fl_p=self.food_oil.get()*220
        self.g_d_p=self.daal.get()*180
        self.g_w_p=self.wheat.get()*180
        self.g_s_p=self.sugar.get()*45
        self.g_t_p=self.tea.get()*180

        self.cl_m_p=self.maza.get()*40
        self.cl_c_p=self.cock.get()*40
        self.cl_f_p=self.frooti.get()*60
        self.cl_t_p=self.thumbsup.get()*50
        self.cl_l_p=self.limca.get()*40
        self.cl_s_p=self.sprite.get()*80 

        self.total_cosmetic_price=float (
                                   (self.c_s_p)+
                                   (self.c_fc_p)+
                                   (self.c_fw_p)+
                                   (self.c_hs_p)+
                                   (self.c_hg_p)+
                                   (self.c_bl_p)
                                   )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.t_cos_tax=(self.total_cosmetic_price*0.05)
        self.cosmetic_tax.set("Rs. "+str(self.t_cos_tax))

        self.total_glocery_price= float(
                                   (self.g_r_p)+
                                   (self.g_fl_p)+
                                   (self.g_d_p)+
                                   (self.g_w_p)+
                                   (self.g_s_p)+
                                   (self.g_t_p)
                                   )
        self.glocery_price.set("Rs. "+str(self.total_glocery_price))
        self.t_glo_tax=(self.total_glocery_price*0.05)
        self.glocery_tax.set("Rs. "+str(self.t_glo_tax))

        self.total_cold_drink_price= float(
                                   (self.cl_m_p)+
                                   (self.cl_c_p)+
                                   (self.cl_f_p)+
                                   (self.cl_t_p)+
                                   (self.cl_l_p)+
                                   (self.cl_s_p)
                                   )
        self.cold_drink_price.set("Rs. "+str(self.total_cold_drink_price))
        self.t_cold_tax=(self.total_cold_drink_price*0.05)
        self.cold_drink_tax.set("Rs. "+str(self.t_cold_tax))

        self.Total_Bill=float(
            self.total_cosmetic_price+
            self.total_glocery_price+
            self.total_cold_drink_price+
            self.t_cos_tax+
            self.t_glo_tax+
            self.t_cold_tax
                         )
        
    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\twelcome Shop")
        self.textarea.insert(END,f"\n Bill No:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Coustmer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\n=====================================")
        self.textarea.insert(END,f"\n product \t\tqty \t\tAmount")
        self.textarea.insert(END,f"\n=====================================")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("error","customer details must fill")
        elif self.cosmetic_price.get()=="Rs.0.0" and self.glocery_price.get()=="Rs.0.0" and self.cold_drink_price.get()=="Rs.0.0":
            messagebox.showerror("error","product details must fill")
        else:
            self.welcome_bill()
            #=====cosmetics=====
            if self.soap.get()!=0:
                self.textarea.insert(END,f"\n Bath Soap \t\t{self.soap.get()} \t\t{self.c_s_p}")
            if self.face_cream.get()!=0:
                self.textarea.insert(END,f"\n Face Cream \t\t{self.face_cream.get()} \t\t{self.c_fc_p}")
            if self.face_wash.get()!=0:
                self.textarea.insert(END,f"\n Face Wash \t\t{self.face_wash.get()} \t\t{self.c_fw_p}")
            if self.shampu.get()!=0:
                self.textarea.insert(END,f"\n Hair Shampu\t\t{self.shampu.get()} \t\t{self.c_hs_p}")                                                                                
            if self.gel.get()!=0:
                self.textarea.insert(END,f"\n Hair Gel \t\t{self.gel.get()} \t\t{self.c_hg_p}")
            if self.loshan.get()!=0:
                self.textarea.insert(END,f"\n Loshan \t\t{self.loshan.get()} \t\t{self.c_bl_p}")

                #=====glocery=====
            if self.rice.get()!=0:
                self.textarea.insert(END,f"\n Rice \t\t{self.rice.get()} \t\t{self.g_r_p}")
            if self.food_oil.get()!=0:
                self.textarea.insert(END,f"\n Food oil \t\t{self.food_oil.get()} \t\t{self.g_fl_p}")
            if self.daal.get()!=0:
                self.textarea.insert(END,f"\n Daal \t\t{self.daal.get()} \t\t{self.g_d_p}")
            if self.wheat.get()!=0:
                self.textarea.insert(END,f"\n Wheat \t\t{self.wheat.get()} \t\t{self.g_w_p}")                                                                                
            if self.sugar.get()!=0:
                self.textarea.insert(END,f"\n Sugar \t\t{self.sugar.get()} \t\t{self.g_s_p}")
            if self.tea.get()!=0:
                self.textarea.insert(END,f"\n Tea \t\t{self.tea.get()} \t\t{self.g_t_p}")

                #=====cold drink=====
            
            if self.maza.get()!=0:
                self.textarea.insert(END,f"\n Maza \t\t{self.maza.get()} \t\t{self.cl_m_p}")
            if self.cock.get()!=0:
                self.textarea.insert(END,f"\n Cock \t\t{self.cock.get()} \t\t{self.cl_c_p}")
            if self.frooti.get()!=0:
                self.textarea.insert(END,f"\n Frooti \t\t{self.frooti.get()} \t\t{self.cl_f_p}")
            if self.thumbsup.get()!=0:
                self.textarea.insert(END,f"\n thumps up\t\t{self.thumbsup.get()} \t\t{self.cl_t_p}")                                                                                
            if self.limca.get()!=0:
                self.textarea.insert(END,f"\n Limca \t\t{self.limca.get()} \t\t{self.cl_l_p}")
            if self.sprite.get()!=0:
                self.textarea.insert(END,f"\n Sprite \t\t{self.sprite.get()} \t\t{self.cl_s_p}")

            self.textarea.insert(END,f"\n-------------------------------------")
            if self.cosmetic_tax.get()!="Rs.0.0 ":
                self.textarea.insert(END,f"\n cosmetic tax \t\t\t  {self.cosmetic_tax.get()}")
            if self.glocery_tax.get()!="Rs.0.0 ":
                self.textarea.insert(END,f"\n glocery tax \t\t\t  {self.glocery_tax.get()}")
            if self.cold_drink_tax.get()!="Rs.0.0 ":
                self.textarea.insert(END,f"\n cold drink tax \t\t\t  {self.cold_drink_tax.get()}")

            self.textarea.insert(END,f"\n-------------------------------------")
            self.textarea.insert(END,f"\n Total Bill \t\t\t Rs. {self.Total_Bill} ")    
            self.textarea.insert(END,f"\n-------------------------------------")

            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("save bill","do you save bill?")
        if op>0:

            self.bill_data=self.textarea.get("1.0",END)
            f1=open("C:/Users/Shailesh/Billing application/bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("saved",f"bill no:{self.bill_no.get()} succesfully")

        else:
            return

    def find_bill(self):
        present="no"
        for i in os.listdir("C:/Users/Shailesh/Billing application/bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open("C:/Users/Shailesh/Billing application/bills/{i}","r")
                self.textarea.delete("1.0",END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("error","invalid bill no.")


    def clear_data(self):
        op=messagebox.askyesno("Clear","do you clear data")
        if op>0:
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.shampu.set(0)
            self.gel.set(0)
            self.loshan.set(0)

            #--------grocery-------------------------
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)

            #--------cold drink-------------------------
            self.maza.set(0)
            self.cock.set(0)
            self.frooti.set(0)
            self.thumbsup.set(0)
            self.limca.set(0)
            self.sprite.set(0)

            #---------total product price and taxes
            self.cosmetic_price.set("")
            self.glocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetic_tax.set("")
            self.glocery_tax.set("")
            self.cold_drink_tax.set("")

            #------costumer--------
            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            
            self.welcome_bill()

    def exit_app(self):
        op=messagebox.askyesno("Exit","do you exit")
        if op>0:
            self.root.destroy()
             
root=Tk()
obj=Bill_app(root)
root.mainloop()