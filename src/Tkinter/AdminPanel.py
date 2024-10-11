from tkinter import *
from src.Controllers.UserController import UserController




def admin():
    def status_false(id):
        button_login.configure(text="Уволен", background='grey')
        user.update_status(id)
        update()
    def add_user(login,name,passwd,role):
        user.add(login,passwd,name,role)
        panel_admin.after(1000,update)

    def update():
        panel_admin.destroy()
        admin()



    panel_admin = Tk()
    panel_admin.geometry('1900x800')
    panel_admin.title("Панель администратора")
    title_window = Label(panel_admin,text="Панель администратора", font=("Times New Roman", 24))
    title_window.grid(column = 0, row = 0, columnspan = 12,padx = 400, pady = 10)
    #title_window.pack(expand = True, anchor = N,side = TOP)
    title_employee = Label(panel_admin,text="Сотрудники", font=(20))
    title_employee.grid(column = 1, row = 1, padx = 10, pady = 10)
    title_employee = Label(panel_admin,text="Роли", font=(20))
    title_employee.grid(column = 2, row = 1, padx = 10, pady = 10)
    title_employee = Label(panel_admin,text="Статус", font=(20))
    title_employee.grid(column = 3, row = 1, padx = 10, pady = 10)
    title_employee = Label(panel_admin,text="Смены", font=(20))
    title_employee.grid(column = 4, row = 1, padx = 10, pady = 10)

    user = UserController()
    list_user = user.get()
    count_row = 2
    for row in list_user:
        if row.status:
            login_title = Label(panel_admin, text=  row.login)
            login_title.grid(column = 1, row = count_row, padx = 1, pady = 1)
            role_title = Label(panel_admin, text=row.role_id.role)
            role_title.grid(column = 2, row = count_row, padx = 0, pady = 1)
            status_title = Label(panel_admin, text=row.status)
            status_title.grid(column = 3, row = count_row, padx = 0, pady = 1)
            button_login = Button(panel_admin,
                                  text="Уволить",
                                  height=2,width=8,background='red',foreground='white',
                                  command= lambda id=row.id: status_false(id))
            button_login.grid(column = 5, row = count_row, padx = 0, pady = 1)
        else:
            login_title = Label(panel_admin, text=row.login)
            login_title.grid(column=1, row=count_row, padx=1, pady=1)
            role_title = Label(panel_admin, text=row.role_id.role)
            role_title.grid(column=2, row=count_row, padx=0, pady=1)
            status_title = Label(panel_admin, text=row.status)
            status_title.grid(column=3, row=count_row, padx=0, pady=1)
            button_login = Button(panel_admin,
                                  text="Уволен",height=2,width=8,background='grey',foreground='white')
            button_login.grid(column=5, row=count_row, padx=0, pady=1)

        count_row +=1

    input_login = Entry(panel_admin, width=20)
    name_input_login = Label(panel_admin, text="Введите логин")
    name_input_login.grid(column=6, row=2)
    input_login.grid(column=6, row=3)

    input_name = Entry(panel_admin, width=20)
    name_input_name = Label(panel_admin, text="Введите имя")
    name_input_name.grid(column=6, row=4)
    input_name.grid(column=6, row=5)

    input_password = Entry(panel_admin, width=20)
    name_input_password = Label(panel_admin, text="Введите пароль")
    name_input_password.grid(column=6, row=6)
    input_password.grid(column=6, row=7)

    input_role = Entry(panel_admin, width=20)
    name_input_role = Label(panel_admin, text="Введите роль")
    name_input_role.grid(column=6, row=8)
    input_role.grid(column=6, row=9)

    button_add_user = Button(panel_admin, text="Добавить пользователя", height=2, width=20,
                             background='green', foreground='white',
                             command= lambda: add_user(input_login.get(), input_name.get(), input_password.get(),
                                                         input_role.get()))

    button_add_user.grid(column=6, row=10)









    panel_admin.mainloop()

if __name__ == "__main__":
    admin()