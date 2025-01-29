import tkinter as tk
from CTkListbox import *
from customtkinter import *
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime

class Window:
    def __init__(self, controller, title):
        self.controller = controller
        self.app = CTk()
        self.title= title
        
        
        ctk.set_appearance_mode("Light")
        ctk.set_default_color_theme("blue")
        
        window_width = 600
        window_height = 350
        screen_width = self.app.winfo_screenwidth()
        screen_height = self.app.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.app.geometry(f"{window_width}x{window_height}+{x}+{y}")  # 600x350+420+275

        self.app.title(title)  # Set the title
        self.app.config(bg="lavender")  # Set the background color
        self.app.resizable(False, False)
        
        
        
        

        
    def runWindow(self):
        self.app.mainloop()
        
    def destroyWindow(self):
        self.app.destroy()
        
    def changeTitle(self, newTitle):
        self.app.title(newTitle)
        
    
class TopLevelWindow(ctk.CTkToplevel):
    def __init__(self, parent, title: str, geometry="300x150+550+360"):
        super().__init__(parent)
        
        # Configure window
        self.title(title)
        self.geometry(geometry)
        # self.resizable(False, False)
        
        
    def destroyTopLevel(self):
        self.destroy()
        


    
class LoginWindow(Window):
    def __init__(self,controller):
        super().__init__(controller, "Login Page")
        self.app.geometry("400x200+520+350")
        
        usernameLabel = ctk.CTkLabel(
            master=self.app,
            text="Username:",
            font=("Arial", 16),
            text_color="black",
            bg_color='lavender'
        )
        usernameLabel.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        
        self.usernameEntry = ctk.CTkEntry(
            master=self.app,
            placeholder_text="Enter your username",
            placeholder_text_color='grey',
            width=170,
            height=27,
            fg_color='azure1',
            border_color='black',
            corner_radius=7,
            border_width=1
        )
        self.usernameEntry.grid(row=0, column=1, padx=20, pady=10, sticky="s")

        
        passwordLabel = ctk.CTkLabel(
            master=self.app,
            text="Password:",
            font=("Arial", 16),
            text_color="black",
            bg_color='lavender'
        )
        
        passwordLabel.grid(row=1, column=0, padx=10, pady=10, sticky="n")
        
        self.passwordEntry = ctk.CTkEntry(
            master=self.app,
            placeholder_text="Enter your password",
            placeholder_text_color='grey',
            width=170,
            height=27,
            fg_color='azure1',
            border_color='black',
            corner_radius=7,
            border_width=1,
            show="*"
        )
        self.passwordEntry.grid(row=1, column=1, padx=20, pady=10, sticky="s")
        
        
        loginButton = CTkButton(
            master=self.app,
            text="Login",
            command=self.loginFunc,
            fg_color="red",  # Foreground color
            hover_color="black"  # Hover effect
        )
        loginButton.place(x=135, y=150)

        
        self.runWindow()
        
    
    def loginFunc(self):
        """
         after pressing login button send username and password to controller for check.
        """
        insertedUsername= self.usernameEntry.get()
        insertedPassword= self.passwordEntry.get()
        self.controller.checkLogin(self, insertedUsername, insertedPassword)
        
        
    def invalidLogin(self):
        messagebox.showwarning("Error", "username or password is incorrect.")
        
        
        
           
        
class ManagerWindow(Window):
    def __init__(self, controllerManager):
        super().__init__(controllerManager, "Manager Homepage")
        
        self.app.grid_columnconfigure(0, weight=1)  # Column 0 (left)
        self.app.grid_columnconfigure(0, weight=1)  # Column 1 (right)
        self.app.grid_rowconfigure(0, weight=1)     # Row 0 (full height)


        self.buttonsFrame=ctk.CTkFrame(master=self.app, bg_color="lavender", fg_color="lavender", width=100)
        self.buttonsFrame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.workspacesFrame=ctk.CTkFrame(self.app, bg_color="lavender", fg_color="mintcream")
        self.workspacesFrame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        
        usersButton=CTkButton(self.buttonsFrame, 
        text="Users",
        fg_color="red", 
        hover_color="black",
        width=100,
        command=self.usersFunc
        )
        usersButton.grid(row=0, column=0, padx=10, pady=10)
        
        requestsButton=CTkButton(self.buttonsFrame,
        text="Requests",
        fg_color="red", 
        hover_color="black",
        width=100,
        command=lambda: self.requestsFunc(self.controller.getRequests())
        )
        requestsButton.grid(row=0, column=1, padx=10, pady=10)
        
        reportsButton=CTkButton(self.buttonsFrame,
        text="Reports",
        fg_color="red", 
        hover_color="black",
        width=100,
        command=self.reportsFunc
        )
        reportsButton.grid(row=1, column=0, padx=10, pady=10)
        
        surveyButton=CTkButton(self.buttonsFrame,
        text="Surveys",
        fg_color="red", 
        hover_color="black",
        width=100,
        command= self.surveyFunc
        )
        surveyButton.grid(row=1, column=1, padx=10, pady=10)
        
        messagesButton=CTkButton(self.buttonsFrame,
        text="Messages",
        fg_color="red", 
        hover_color="black",
        width=100,
        command= self.messagesFunc
        )
        messagesButton.place(x= 70, y=105)
        
        sendAnnouncementButton=CTkButton(self.buttonsFrame,
        text="Send announcement",
        fg_color="red", 
        hover_color="black",
        command= self.announcementFunc
        )
        sendAnnouncementButton.place(x= 50, y=150)
        
        newSubjectStatusButton=CTkButton(self.buttonsFrame,
        text="New subject/status",
        fg_color="red", 
        hover_color="black",
        command= self.newSSFunc
        )
        newSubjectStatusButton.place(x= 50, y=195)
        
        LogoutButton=CTkButton(self.buttonsFrame,
        text="Logout", 
        command= lambda: self.app.destroy(),
        fg_color="grey", 
        hover_color="black"
        )
        LogoutButton.place(x=45, y=250)
        self.runWindow()       
        
 ############################################################################################################################################################################
        
    def usersFunc(self):
        """
        shows list of users(beside manager) and user management buttons.
        """
        self.changeTitle("Users")
        usersList= self.controller.getUsers()
        tempList=[]    # contains all users beside the managers
        
        usersFrame=ctk.CTkFrame(master=self.app, bg_color="lavender", fg_color="lavender", width=100)
        usersFrame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        
        listbox = CTkListbox(self.workspacesFrame, hover_color='grey', highlight_color='royalblue3')
        listbox.pack(fill="both", expand=True, padx=10, pady=10)
        
        i=0
        for user in usersList:
            if user.getRole() != "manager":
                temp= user.getUsername() +"  |  "+ user.getRole()
                listbox.insert(i, temp)
                tempList.append(user)
                i+=1
        
        
    
        
        def addUser():
            addUserTopLevel=TopLevelWindow(self.app, "Add user", geometry="300x200+560+360")
            usernameLabel = ctk.CTkLabel(
            master=addUserTopLevel,
            text="Username:",
            font=("Arial", 16),
            text_color="black"
            )
            usernameLabel.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
            
            usernameEntry = ctk.CTkEntry(
                master=addUserTopLevel,
                placeholder_text="Enter username",
                placeholder_text_color='grey',
                width=170,
                height=27,
                fg_color='azure1',
                border_color='black',
                corner_radius=7,
                border_width=1
            )
            usernameEntry.grid(row=0, column=1, padx=20, pady=10, sticky="s")

            
            passwordLabel = ctk.CTkLabel(
                master=addUserTopLevel,
                text="Password:",
                font=("Arial", 16),
                text_color="black"
            )
            
            passwordLabel.grid(row=1, column=0, padx=10, pady=10, sticky="n")
            
            passwordEntry = ctk.CTkEntry(
                master=addUserTopLevel,
                placeholder_text="Enter password",
                placeholder_text_color='grey',
                width=170,
                height=27,
                fg_color='azure1',
                border_color='black',
                corner_radius=7,
                border_width=1
            )
            passwordEntry.grid(row=1, column=1, padx=20, pady=10, sticky="s")
            
            
            roleLabel = ctk.CTkLabel(
                master=addUserTopLevel,
                text="Role:",
                font=("Arial", 16),
                text_color="black"
            )
            
            roleLabel.place(x=12, y=105)
            
            radioVar = ctk.StringVar(value=None)  # Default selected option
            radio_button1 = ctk.CTkRadioButton(
                master=addUserTopLevel,
                text="Employee",
                variable=radioVar,
                value="employee"
            ).place(x=105, y=110)
            radio_button2 = ctk.CTkRadioButton(
                master=addUserTopLevel,
                text="Client",
                variable=radioVar,
                value="client"
            ).place(x=215, y=110)
            
            
            
            def addFunc():
                if radioVar.get():
                    self.controller.addUser(usernameEntry.get(), passwordEntry.get(), radioVar.get())
                    addUserTopLevel.destroy()
                    backFunc()
                    
                
            addButton = CTkButton(
                master=addUserTopLevel,
                text="Add",
                command=addFunc,
                fg_color="red",  # Foreground color
                hover_color="black"  # Hover effect
            )
            addButton.place(x=85, y=160)
        
        
        
        
        
        def removeUser():            
            if listbox.get():
                self.controller.removeUser(tempList[listbox.curselection()])
                backFunc()
            
            
        
            
            
        
        def changeRoleFunc():
            """
            shows a toplevel psge with user info and roles radio buttons.
            """
            if listbox.get():
                changeRoleToplevel=TopLevelWindow(self.app, "Change role")
                # changeRoleToplevel=CTkToplevel(self.app)
                # changeRoleToplevel.title("Change role")
                # changeRoleToplevel.geometry("300x150+560+360")
                CTkLabel(changeRoleToplevel, text=listbox.get()).place(x=100, y=5)
                CTkLabel(changeRoleToplevel, text="New Role:").place(x=10, y=45)
                
                
                radioVar = ctk.StringVar(value=None)  # Default selected option
                radio_button1 = ctk.CTkRadioButton(
                    master=changeRoleToplevel,
                    text="Employee",
                    variable=radioVar,
                    value="employee"
                ).place(x=90, y=50)
                radio_button2 = ctk.CTkRadioButton(
                    master=changeRoleToplevel,
                    text="Client",
                    variable=radioVar,
                    value="client"
                ).place(x=195, y=50)
                
                
                def change():
                    if radioVar.get():
                        self.controller.changeRole(tempList[listbox.curselection()], radioVar.get())
                        changeRoleToplevel.destroy()
                        backFunc()
                    
                    
                CTkButton(changeRoleToplevel, text="Change", command=change).place(x=80, y=100)
                        
        
        
        
        def backFunc():
            usersFrame.destroy()
            listbox.destroy()
            self.changeTitle("Manager Homepage")
        
        
        
        
        
        
        addUserButton=CTkButton(usersFrame,
        text="Add user", 
        command= addUser,
        fg_color="red", 
        hover_color="black",
        width=100
        )
        addUserButton.grid(row=0, column= 0, sticky="sw", padx=5, pady=10)
        
        remvoveUserButton=CTkButton(usersFrame,
        text="Remove user", 
        command= removeUser,
        fg_color="red", 
        hover_color="black",
        width=100
        )
        remvoveUserButton.grid(row=0, column= 1, sticky="sw", padx=5, pady=10)
        
        changeRoleButton=CTkButton(usersFrame,
        text="Change role", 
        command= changeRoleFunc,
        fg_color="red", 
        hover_color="black"
        )
        changeRoleButton.place(x=45, y=70)
        
        backButton=CTkButton(usersFrame,
        text="Main menu", 
        command= backFunc,
        fg_color="grey", 
        hover_color="black"
        )
        backButton.place(x=45, y=250)
        
            
            
        
        

    def requestsFunc(self, requestsList):
        self.changeTitle("Requests")
        reqestsFrame=ctk.CTkFrame(master=self.app, bg_color="lavender", fg_color="lavender", width=100)
        reqestsFrame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        
        requestsListbox = CTkListbox(self.workspacesFrame, hover_color='grey', highlight_color='royalblue3')
        requestsListbox.pack(fill="both", expand=True, padx=10, pady=10)
        
        i=0
        for request in requestsList:
            temp= str(request.getRequestID()) +"  |  "+ request.getSubject() +"  |  "+ request.getStatus()
            requestsListbox.insert(i, temp)
            i+=1
            
        def viewRequestFunc():
            
            if requestsListbox.get():
                currentRequest=requestsList[requestsListbox.curselection()]
                viewRequestTopLevel =TopLevelWindow(self.app, f"Request {currentRequest.getRequestID()}", geometry="360x310+530+305")
                
                requesterLabel=CTkLabel(viewRequestTopLevel, text="requester:")
                requesterLabel.grid(row=0, column=0, padx=10, pady=0)
                requesterLabel2=CTkLabel(viewRequestTopLevel, text=currentRequest.getRequester().getUsername())
                requesterLabel2.grid(row=0, column=1, padx=10, pady=10)
                
                
                subjectLabel=CTkLabel(viewRequestTopLevel, text="subject:").grid(row=1, column=0, padx=10, pady=10)
                subjectCombobox = CTkComboBox(master=viewRequestTopLevel, values=self.controller.getRequestSubjects(), state="readonly")
                subjectCombobox.grid(row=1, column=1, padx=10, pady=10)
                subjectCombobox.set(currentRequest.getSubject())
                
                
                contentLabel=CTkLabel(viewRequestTopLevel, text="Content:").grid(row=2, column=0, padx=10, pady=10)
                contentTextbox=CTkTextbox(viewRequestTopLevel, width=160,height=60)
                contentTextbox.grid(row=2, column=1)
                contentTextbox.insert("1.0", currentRequest.getContent())
                
                statusLabel=CTkLabel(viewRequestTopLevel, text="Status:").grid(row=3, column=0, padx=10, pady=10)
                statusCombobox = CTkComboBox(master=viewRequestTopLevel, values=self.controller.getRequestStatus(), state="readonly")
                statusCombobox.grid(row=3, column=1, padx=10, pady=10)
                statusCombobox.set(currentRequest.getStatus())
                
                creatingDateLabel=CTkLabel(viewRequestTopLevel, text="Creating Date:").grid(row=4, column=0, sticky="e")
                creatingDateLabel2=CTkLabel(viewRequestTopLevel, text=currentRequest.getCreatedDate().strftime("%Y-%m-%d %H:%M")).grid(row=4, column=1)
                
                endDateLabel=CTkLabel(viewRequestTopLevel, text="End Date:").grid(row=5, column=0)
                
                endDateEntry=DateEntry(viewRequestTopLevel, width=12, background="darkblue", foreground="white", borderwidth=2, date_pattern="yyyy-mm-dd")
                endDateEntry.grid(row=5, column=1, padx=10, pady=10)
                endDateEntry.set_date(currentRequest.getEndDate())
                
                respondentLabel=CTkLabel(viewRequestTopLevel, text="Respondent:")
                respondentLabel.grid(row=6, column=0)
                respondentLabel2=CTkLabel(viewRequestTopLevel, text="None")
                respondentLabel2.grid(row=6, column=1)
                         
                
                
                
                def editRequestFunc():
                    tempSubject= subjectCombobox.get()
                    tempContent=contentTextbox.get("1.0", "end-1c")
                    tempStatus= statusCombobox.get()
                    tempEndDate= endDateEntry.get_date()
                    self.controller.editRequest(currentRequest, tempSubject, tempContent, tempStatus, tempEndDate)
                    viewRequestTopLevel.destroy()
                    backFunc()
                
                
                
                
                def requestHistoryFunc():
                    requestHistoryToplevel =TopLevelWindow(viewRequestTopLevel, "History", geometry="600x230+420+340") # 
                    historyList=currentRequest.getChangesHistory()
                    historyListbox = CTkListbox(requestHistoryToplevel, hover_color='grey', highlight_color='royalblue3')
                    historyListbox.pack(fill="both", expand=True, padx=10, pady=10)
                    
                    i=0
                    for history in historyList:
                        historyListbox.insert(i, history)
                        i+=1
                
                
                
                def setRespondentFunc():
                    setRespondentToplevel =TopLevelWindow(viewRequestTopLevel, "Respondent", geometry="350x200+460+350")
                    employeesList=self.controller.getEmployees()
                    
                    
                  
                    def setFunc():
                        request=currentRequest
                        employee=employeesList[employeesListbox.curselection()]
                        self.controller.assignRequest(request, employee)
                        setRespondentToplevel.destroyTopLevel()
                        viewRequestTopLevel.destroyTopLevel()
                        backFunc()
                        
                    
                    employeesListbox = CTkListbox(setRespondentToplevel, hover_color='grey', highlight_color='royalblue3')
                    employeesListbox.pack(fill="both", expand=True, padx=10, pady=10)
                    setButton=CTkButton(
                        setRespondentToplevel,
                        text="set",
                        fg_color="red", 
                        hover_color="black",
                        command= setFunc
                        )
                    setButton.pack(pady=10)
                    
                    i=0
                    for employee in employeesList:
                        employeesListbox.insert(i, employee.getUsername())
                        i+=1
           
                editRequestButton=CTkButton(viewRequestTopLevel,
                        text="Edit",
                        fg_color="red", 
                        hover_color="black",
                        width=80,
                        command= editRequestFunc
                        )
                editRequestButton.grid(row=1, column=2, padx=20)
                 
                requestHistoryButton=CTkButton(viewRequestTopLevel,
                        text="History",
                        fg_color="red", 
                        hover_color="black",
                        width=80,
                        command= requestHistoryFunc
                        )
                requestHistoryButton.grid(row=2, column=2, padx=20)
                
                setRespondentButton=CTkButton(viewRequestTopLevel,
                        text="Respondet",
                        fg_color="red", 
                        hover_color="black",
                        width=80,
                        command= setRespondentFunc
                        )
                setRespondentButton.grid(row=3, column=2, padx=20)
                
                if currentRequest.getRespondent():
                    setRespondentButton.destroy()
                    respondentLabel2.configure(text=currentRequest.getRespondent().getUsername())       
                
        
        
 
        def removeRequestFunc():
            if requestsListbox.get():
                self.controller.removeRequest(requestsList[requestsListbox.curselection()])
                backFunc()
                
                
        def searchRequestFunc():
            searchRequestTopLevel= TopLevelWindow(self.app,title= "Search", geometry="380x180+530+315")
            selected_option = ctk.StringVar(value="")  
            
            
            subjectLabel=CTkLabel(searchRequestTopLevel, text="subject:").grid(row=0, column=0, padx=10, pady=10)
            subjectCombobox = CTkComboBox(master=searchRequestTopLevel, values=self.controller.getRequestSubjects(), width=120, state="readonly")
            subjectCombobox.grid(row=0, column=1, padx=10, pady=10)
            subjectCombobox.set("All")
            
            statusLabel=CTkLabel(searchRequestTopLevel, text="Status:").grid(row=1, column=0, padx=10, pady=10)
            statusCombobox = CTkComboBox(master=searchRequestTopLevel, values=self.controller.getRequestStatus(), width=120, state="readonly")
            statusCombobox.grid(row=1, column=1, padx=10, pady=10)
            statusCombobox.set("All")
            
            submitDateLabel=CTkLabel(searchRequestTopLevel, text="submited from").grid(row=2, column=0)
            submitDateEntry=DateEntry(searchRequestTopLevel, width=8, background="darkblue", foreground="white", borderwidth=2, date_pattern="yyyy-mm-dd")
            submitDateEntry.grid(row=2, column=1, padx=10, pady=10)
            submitDateEntry.set_date("2023-01-01")
            submitDateLabel2=CTkLabel(searchRequestTopLevel, text="to", width=5).grid(row=2, column=2)
            submitDateEntry2=DateEntry(searchRequestTopLevel, width=8, background="darkblue", foreground="white", borderwidth=2, date_pattern="yyyy-mm-dd")
            submitDateEntry2.grid(row=2, column=3, padx=10, pady=10)
            
            
            endDateLabel=CTkLabel(searchRequestTopLevel, text="Ends from").grid(row=3, column=0)
            endDateEntry=DateEntry(searchRequestTopLevel, width=9, background="darkblue", foreground="white", borderwidth=2, date_pattern="yyyy-mm-dd")
            endDateEntry.grid(row=3, column=1, padx=0, pady=10)
            endDateEntry.set_date("2023-01-01")
            endDateLabel2=CTkLabel(searchRequestTopLevel, text="to").grid(row=3, column=2)
            endDateEntry2=DateEntry(searchRequestTopLevel, width=9, background="darkblue", foreground="white", borderwidth=2, date_pattern="yyyy-mm-dd")
            endDateEntry2.grid(row=3, column=3, padx=0, pady=10)
            
            
            def searchFunc():
                results=self.controller.getRequests()
                status=statusCombobox.get()
                subject=subjectCombobox.get()
                submitDate=submitDateEntry.get_date()
                submitDate2=submitDateEntry2.get_date()
                endDate=endDateEntry.get_date()
                endDate2=endDateEntry2.get_date()
                
                
                if status!="All":
                    results = [req for req in results if req.getStatus() == status]
                if subject!="All":
                    results = [req for req in results if req.getSubject() == subject]
                    
                results = [req for req in results if (submitDate <= req.getCreatedDate().date() <= submitDate2)]
                results = [req for req in results if req not in [req2 for req2 in results if req2.getEndDate() and (endDate >= req2.getEndDate() or req2.getEndDate() >= endDate2)] ]


                searchRequestTopLevel.destroy()
                backFunc()
                self.requestsFunc(results)
            
            searchButton=CTkButton(searchRequestTopLevel,
            text="Done",
            command= searchFunc,
            fg_color="red", 
            hover_color="black",
            width=100
            )
            searchButton.place(x=270, y=20)
        
                
        def sendRequestMesssageFunc():
            if requestsListbox.get():
                currentRequest=requestsList[requestsListbox.curselection()]
                sendMessageTopLevel =TopLevelWindow(self.app,title= "Send message", geometry="320x160+530+315")
                contentLabel= CTkLabel(sendMessageTopLevel, text="your message:", font=("Arial", 15))
                contentLabel.grid(row=0, column= 0, padx=10, pady=10)
                
                contentTextbox= CTkTextbox(sendMessageTopLevel, width=180, height=80)
                contentTextbox.grid(row=0, column= 1, padx=10, pady=10)
                
                def sendFunc():
                    tempContent= contentTextbox.get("1.0", "end-1c")
                    self.controller.sendRequestMessage(currentRequest, tempContent)
                    sendMessageTopLevel.destroy()
                sendButton= CTkButton(sendMessageTopLevel,
                text="Send",
                command= sendFunc,
                fg_color="red", 
                hover_color="black",
                width=100
                )
                sendButton.place(x=115, y=115)
                
        

                
        
    
        def backFunc():
            reqestsFrame.destroy()
            requestsListbox.destroy()
            self.changeTitle("Manager Homepage")
            
            
            
            
        viewRequestButton=CTkButton(reqestsFrame,
        text="View",
        command= viewRequestFunc,
        fg_color="red", 
        hover_color="black",
        width=100
        )
        viewRequestButton.grid(row=0, column=0)
        
        
        removeRequestButton=CTkButton(reqestsFrame,
        text="Remove",
        command= removeRequestFunc,
        fg_color="red", 
        hover_color="black",
        width=100
        )
        removeRequestButton.grid(row=0, column=1, padx=10)
        
        searchRequestButton=CTkButton(reqestsFrame,
        text="Search",
        command= searchRequestFunc,
        fg_color="red", 
        hover_color="black",
        width=100
        )
        searchRequestButton.grid(row=1, column=0, padx=10, pady=10)
        
        sendRequestMesssageButton=CTkButton(reqestsFrame,
        text="send message",
        command= sendRequestMesssageFunc,
        fg_color="red", 
        hover_color="black",
        width=100
        )
        sendRequestMesssageButton.grid(row=1, column=1, padx=10, pady=10)
        
        
        backButton=CTkButton(reqestsFrame,
        text="Main menu", 
        command= backFunc,
        fg_color="grey", 
        hover_color="black"
        )
        backButton.place(x=45, y=250)
        
        
    
    
    
    
    def reportsFunc(self):
        self.changeTitle("Reports")
        requestsList=self.controller.getRequests()
        reportsFrame=ctk.CTkFrame(master=self.app, bg_color="lavender", fg_color="lavender", width=100)
        reportsFrame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        
        requestsListbox = CTkListbox(self.workspacesFrame, hover_color='grey', highlight_color='royalblue3', multiple_selection=True)
        requestsListbox.pack(fill="both", expand=True, padx=10, pady=10)
        
        i=0
        for request in requestsList:
            temp= str(request.getRequestID()) +"  |  "+ request.getSubject() +"  |  "+ request.getStatus()
            requestsListbox.insert(i, temp)
            i+=1
            
        
            
        def temporalReportFunc():
            if requestsListbox.curselection():
                temporalReportsFrame=ctk.CTkFrame(master=self.app, bg_color="lavender", fg_color="lavender", width=100)
                temporalReportsFrame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
                
                resultReportFrame=ctk.CTkFrame(self.app, bg_color="lavender", fg_color="mintcream")
                resultReportFrame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
            
                selectedRequests= requestsListbox.curselection()
                selectedRequests= [requestsList[i] for i in selectedRequests]
                
                resultReportListbox = CTkListbox(resultReportFrame, hover_color='grey', highlight_color='royalblue3', multiple_selection=True)
                resultReportListbox.pack(fill="both", expand=True, padx=10, pady=10)
                
                
                
                i=0
                for request in selectedRequests:
                    if request.getEndDate():
                        temp= str(request.getRequestID()) +"  |  "+ str(request.getCreatedDate().strftime("%Y-%m-%d %H:%M")) +"  |  "+ str(request.getEndDate())
                    else:
                        temp= str(request.getRequestID()) +"  |  "+ str(request.getCreatedDate().strftime("%Y-%m-%d %H:%M")) +"  |  "+ "No end date"
                    
                    resultReportListbox.insert(i, temp)
                    i+=1
                    
                    
                    
                def backFunc2():
                    temporalReportsFrame.destroy()
                    resultReportFrame.destroy()
                    
                backButton2=CTkButton(temporalReportsFrame,
                text="Back", 
                command= backFunc2,
                fg_color="grey", 
                hover_color="black"
                )
                backButton2.place(x=45, y=250)
            
            
        temporalReportButton=CTkButton(reportsFrame,
        text="Temporal aggregate report",
        command= temporalReportFunc,
        fg_color="red", 
        hover_color="black"
        )
        temporalReportButton.grid(row=0, column=0, padx=10, pady=10)
        
        
        
        
        
        
        def qualitiveReportFunc():
            if requestsListbox.curselection():
                qualitiveReportsFrame=ctk.CTkFrame(master=self.app, bg_color="lavender", fg_color="lavender", width=100)
                qualitiveReportsFrame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
                
                resultReportFrame=ctk.CTkFrame(self.app, bg_color="lavender", fg_color="mintcream")
                resultReportFrame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
                
                selectedRequests= requestsListbox.curselection()
                selectedRequests= [requestsList[i] for i in selectedRequests]
                
                resultReportListbox = CTkListbox(resultReportFrame, hover_color='grey', highlight_color='royalblue3', multiple_selection=True)
                resultReportListbox.pack(fill="both", expand=True, padx=10, pady=10)
                
                
                
                i=0
                for request in selectedRequests:
                    if request.getResponseRate():
                        temp= str(request.getRequestID()) + "  |  " + str(request.getResponseRate()) +"/10"
                    else:
                        temp= str(request.getRequestID()) + "  |  " + "No rating"
                    
                    resultReportListbox.insert(i, temp)
                    i+=1
                    
                    
                    
                def backFunc2():
                    qualitiveReportsFrame.destroy()
                    resultReportFrame.destroy()
                    
                backButton2=CTkButton(qualitiveReportsFrame,
                text="Back", 
                command= backFunc2,
                fg_color="grey", 
                hover_color="black"
                )
                backButton2.place(x=45, y=250)
            
            
        qualitiveReportButton=CTkButton(reportsFrame,
        text="Qualitative aggregate report",
        command= qualitiveReportFunc,
        fg_color="red", 
        hover_color="black"
        )
        qualitiveReportButton.grid(row=1, column=0, padx=20, pady=10)
        
        
        
        def backFunc():
            reportsFrame.destroy()
            requestsListbox.destroy()
            self.changeTitle("Manager Homepage")
        
        
        backButton=CTkButton(reportsFrame,
        text="Main menu", 
        command= backFunc,
        fg_color="grey", 
        hover_color="black"
        )
        backButton.place(x=45, y=250)
        
        
    
    
    
    
    def surveyFunc(self):
        self.changeTitle("Survey")
        surveysList= self.controller.getSurveys()
        surveyFrame=ctk.CTkFrame(master=self.app, bg_color="lavender", fg_color="lavender", width=100)
        surveyFrame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        
        surveysListbox = CTkListbox(self.workspacesFrame, hover_color='grey', highlight_color='royalblue3')
        surveysListbox.pack(fill="both", expand=True, padx=10, pady=10)
        
        i=0
        for survey in surveysList:
            temp= survey.getQuestion()
            surveysListbox.insert(i, temp)
            i+=1
        
        
        
        def viewAnswersFunc():
            if surveysListbox.get():
                currentSurvey=surveysList[surveysListbox.curselection()]
                viewAnswersTopLevel= TopLevelWindow(surveyFrame, "Answers")
                
                answersListbox=CTkListbox(viewAnswersTopLevel, hover_color='grey', highlight_color='royalblue3')
                answersListbox.pack(fill="both", expand=True, padx=10, pady=10)
                i=0
                for answer in currentSurvey.getAnswers():
                    temp= f"{answer[0]}: \"{answer[1]}\""
                    answersListbox.insert(i, temp)
                    i+=1
                
            
        
        def newSurveyFunc():
            newSurvayTopLevel=TopLevelWindow(surveyFrame, "New survey", geometry="370x250+530+310")
            usersList=self.controller.getUsers()
            usersList=[i for i in usersList if i.getRole()!="manager"]
            
            
            questionLabel=CTkLabel(newSurvayTopLevel, text="Question:", )
            questionLabel.place(x=40, y=8)
            
            questionEntry=CTkEntry(newSurvayTopLevel, placeholder_text="Survey question",placeholder_text_color='grey',width=200)
            questionEntry.place(x=110, y=8)
            
            targetsLabel=CTkLabel(newSurvayTopLevel, text="Who can answer:", )
            targetsLabel.place(x=11, y=60)
            targetsListbox=CTkListbox(newSurvayTopLevel, hover_color='grey', highlight_color='royalblue3', multiple_selection=True)
            targetsListbox.place(x=7, y=85)
            
            viewersLabel=CTkLabel(newSurvayTopLevel, text="Who can see results:", )
            viewersLabel.place(x=190, y=60)
            viewersListbox=CTkListbox(newSurvayTopLevel, hover_color='grey', highlight_color='royalblue3', multiple_selection=True)
            viewersListbox.place(x=188, y=85)
            
            i=0
            for user in usersList:
                targetsListbox.insert(i, user.getUsername())
                viewersListbox.insert(i, user.getUsername())
                i+=1
            
            
            def createFunc():
                targetUsersList=[usersList[i] for i in targetsListbox.curselection()]
                viewersList=[usersList[j] for j in viewersListbox.curselection()]
                
                surveyQuestion= questionEntry.get()
                self.controller.createSurvey(surveyQuestion, targetUsersList, viewersList)
                newSurvayTopLevel.destroy()
                backFunc()
                
            
            
            createButton = CTkButton(
            master=newSurvayTopLevel,
            text="Create",
            command=createFunc,
            fg_color="red",  # Foreground color
            hover_color="black"  # Hover effect
            )
            createButton.place(x=120, y=215)
            
            
            
            
        
        
        viewAnswersButton=CTkButton(surveyFrame, 
        text="View answers",
        fg_color="red", 
        hover_color="black",
        width=100,
        command=viewAnswersFunc
        )
        viewAnswersButton.grid(row=0, column=0, padx=70, pady=30)
        
        
        newSurveyButton=CTkButton(surveyFrame, 
        text="new Survey",
        fg_color="red", 
        hover_color="black",
        width=100,
        command=newSurveyFunc
        )
        newSurveyButton.grid(row=1, column=0, padx=60, pady=10)
        
        
        def backFunc():
            surveyFrame.destroy()
            surveysListbox.destroy()
            self.changeTitle("Manager Homepage")
        
        
        backButton=CTkButton(surveyFrame,
        text="Main menu", 
        command= backFunc,
        fg_color="grey", 
        hover_color="black"
        )
        backButton.place(x=45, y=250)
    
    
    
    
    
    
    def messagesFunc(self):
        self.changeTitle("Messages")
        messageslist= self.controller.getMessages()
        
        messagesFrame=CTkFrame(master=self.app, bg_color="lavender", fg_color="lavender", width=100)
        messagesFrame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        
        messagesListBox= CTkListbox(self.workspacesFrame, hover_color='grey', highlight_color='royalblue3')
        messagesListBox.pack(fill="both", expand=True, padx=10, pady=10)
        
        i=0
        for mess in messageslist:
            if mess.getType() == "requestMessage":
                temp= f"Request {mess.getRequest().getRequestID()} | {mess.getSender().getUsername()}: {mess.getContent()[:15].splitlines()[0]}..."
            else:
                temp= f"Manager: {mess.getContent()[:25].splitlines()[0]}..."
            messagesListBox.insert(i, temp)
            i+=1
        
        
        
        def viewMessageFunc():
            if messagesListBox.get():
                currentMessage= messageslist[messagesListBox.curselection()]
                
                viewMessageTopLevel = TopLevelWindow(messagesFrame, currentMessage.getSender().getUsername())
                
                messageLabel= CTkLabel(viewMessageTopLevel, text=currentMessage.getContent())
                messageLabel.place(x=50, y=10)
        
        viewMessageButton=CTkButton(messagesFrame, 
        text="View",
        fg_color="red", 
        hover_color="black",
        width=100,
        command=viewMessageFunc
        )
        viewMessageButton.grid(row=0, column=0, padx=70, pady=30)
        
        
        
        def backFunc():
            messagesFrame.destroy()
            messagesListBox.destroy()
            self.changeTitle("Manager Homepage")
        
        
        backButton=CTkButton(messagesFrame,
        text="Main menu", 
        command= backFunc,
        fg_color="grey", 
        hover_color="black"
        )
        backButton.place(x=45, y=250)
        
        
        
        
    
    def announcementFunc(self):
        self.changeTitle("Announcement")
        annoucementFrame= CTkFrame(master=self.app, bg_color="lavender", fg_color="lavender", width=100)
        annoucementFrame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        
        annoucementTextbox= CTkTextbox(self.workspacesFrame, width=270, height=100, fg_color="lightgrey")
        annoucementTextbox.place(x=20, y=20)
        
        receiversLabel= CTkLabel(self.workspacesFrame, text="receivers")
        receiversLabel.place(x=125, y=133)
        receiversListBox=CTkListbox(self.workspacesFrame, hover_color='grey', highlight_color='royalblue3', multiple_selection=True)
        receiversListBox.place(x=65, y=160)
        
        
        usersList=[i for i in self.controller.getUsers() if i.getRole()!="manager"]
        
        i=0
        for user in usersList:
            receiversListBox.insert(i, user.getUsername())
            i+=1
            
        
        def sendFunc():
            annoucementContent= annoucementTextbox.get("1.0", "end-1c")
            receivers= [usersList[i] for i in receiversListBox.curselection()]
            self.controller.sendAnnouncement(annoucementContent, receivers)
            
            backFunc()
        
        sendButton=CTkButton(self.workspacesFrame,
        text="Send",
        command= sendFunc,
        fg_color="red", 
        hover_color="black"
        )
        sendButton.place(x=85, y=290)
        
        
        
        def backFunc():
            annoucementFrame.destroy()
            annoucementTextbox.destroy()
            sendButton.destroy()
            receiversLabel.destroy()
            receiversListBox.destroy()
            self.changeTitle("Manager Homepage")
        
        
        backButton=CTkButton(annoucementFrame,
        text="Main menu", 
        command= backFunc,
        fg_color="grey", 
        hover_color="black"
        )
        backButton.place(x=45, y=250)
    
    
    
    
    def newSSFunc(self):
        self.changeTitle("New Subject/Status")
        newSSFrame=ctk.CTkFrame(master=self.app, bg_color="lavender", fg_color="lavender", width=100)
        newSSFrame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        
        newSSEntry=CTkEntry(
            master=self.workspacesFrame,
            placeholder_text="Enter new subject/status",
            placeholder_text_color='grey',
            width=170,
            height=27,
            fg_color='azure1',
            border_color='black',
            corner_radius=7,
            border_width=1
        )
        newSSEntry.grid(row=0, column=0, padx=70, pady=20)
        self.app.update_idletasks()
        
        
        
        def addSubjectFunc():
            if newSSEntry.get():
                self.controller.addSubject(newSSEntry.get())
                backFunc()
        
        addSubjectButton=CTkButton(self.workspacesFrame,
        text="New subject",
        command= addSubjectFunc,
        fg_color="red", 
        hover_color="black"
        )
        addSubjectButton.grid(row=1, column=0, padx=10, pady=10)
        
        def addStatusFunc():
            if newSSEntry.get():
                self.controller.addStatus(newSSEntry.get())
                backFunc()
        
        addStatusButton=CTkButton(self.workspacesFrame,
        text="New status",
        command= addStatusFunc,
        fg_color="red", 
        hover_color="black"
        )
        addStatusButton.grid(row=2, column=0, padx=10, pady=10)
        
        
        
        
        def backFunc():
            newSSFrame.destroy()
            newSSEntry.destroy()
            addSubjectButton.destroy()
            addStatusButton.destroy()
            self.changeTitle("Manager Homepage")
            
            
        backButton=CTkButton(newSSFrame,
        text="Main menu", 
        command= backFunc,
        fg_color="grey", 
        hover_color="black"
        )
        backButton.place(x=45, y=250)
        
        
        
    
    
    
    
class EmployeeWindow(Window):
    def __init__(self, ControllerEmployee):
        super().__init__(ControllerEmployee, "Employee Homepage")
        
        self.app.grid_columnconfigure(0, weight=1)  # Column 0 (left)
        self.app.grid_columnconfigure(0, weight=1)  # Column 1 (right)
        self.app.grid_rowconfigure(0, weight=1)     # Row 0 (full height)


        self.buttonsFrame=ctk.CTkFrame(master=self.app, bg_color="lavender", fg_color="lavender", width=100)
        self.buttonsFrame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.workspacesFrame=ctk.CTkFrame(self.app, bg_color="lavender", fg_color="mintcream")
        self.workspacesFrame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
        
        
        assignedRequestsButton=CTkButton(self.buttonsFrame, 
        text="Assigned requests",
        fg_color="red", 
        hover_color="black",
        width=100,
        command=self.assignedRequestsFunc
        )
        assignedRequestsButton.place(x=53, y=10)
        
        CTkLabel(self.buttonsFrame, text=None, height=40).grid(row=0,column=1, pady=4)
        
        allRequestsButton=CTkButton(self.buttonsFrame, 
        text="All requests",
        fg_color="red", 
        hover_color="black",
        width=100,
        command=lambda: self.allRequestsFunc(self.controller.getAllRequests())
        )
        allRequestsButton.grid(row=1, column=0, padx=10, pady=10)
        
        messagesButton=CTkButton(self.buttonsFrame, 
        text="Messages",
        fg_color="red", 
        hover_color="black",
        width=100,
        command=self.messagesFunc
        )
        messagesButton.grid(row=1, column=1, padx=10, pady=10)
        
        surveysButton=CTkButton(self.buttonsFrame, 
        text="Surveys",
        fg_color="red", 
        hover_color="black",
        width=100,
        command=self.surveysFunc
        )
        surveysButton.grid(row=2, column=0, padx=10, pady=10)
        
        LogoutButton=CTkButton(self.buttonsFrame,
        text="Logout", 
        command= lambda: self.app.destroy(),
        fg_color="grey", 
        hover_color="black"
        )
        LogoutButton.place(x=45, y=250)
        self.runWindow()   
        
        
        
        
        
        
        
        self.runWindow()
 ############################################################################################################################################################################
        
        
    def assignedRequestsFunc(self):
        self.changeTitle("Assigned Requests")
        reqestsFrame=ctk.CTkFrame(master=self.app, bg_color="lavender", fg_color="lavender", width=100)
        reqestsFrame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
            
        requestsListbox = CTkListbox(self.workspacesFrame, hover_color='grey', highlight_color='royalblue3')
        requestsListbox.pack(fill="both", expand=True, padx=10, pady=10)
        
        requestsList=self.controller.getAssignedRequests()
            
        i=0
        for request in requestsList:
            temp= str(request.getRequestID()) +"  |  "+ request.getSubject() +"  |  "+ request.getStatus()
            requestsListbox.insert(i, temp)
            i+=1
            
        def viewRequestFunc():
            if requestsListbox.get():
                currentRequest=requestsList[requestsListbox.curselection()]
                viewRequestTopLevel =TopLevelWindow(self.app, f"Request {currentRequest.getRequestID()}", geometry="360x310+530+305")
                
                requesterLabel=CTkLabel(viewRequestTopLevel, text="requester:")
                requesterLabel.grid(row=0, column=0, padx=10, pady=0)
                requesterLabel2=CTkLabel(viewRequestTopLevel, text=currentRequest.getRequester().getUsername())
                requesterLabel2.grid(row=0, column=1, padx=10, pady=10)
                
                    
                subjectLabel=CTkLabel(viewRequestTopLevel, text="subject:").grid(row=1, column=0, padx=10, pady=10)
                subjectCombobox = CTkComboBox(master=viewRequestTopLevel, values=[], state="readonly")
                subjectCombobox.grid(row=1, column=1, padx=10, pady=10)
                subjectCombobox.set(currentRequest.getSubject())
                subjectCombobox.configure(state="disabled")
                    
                    
                contentLabel=CTkLabel(viewRequestTopLevel, text="Content:").grid(row=2, column=0, padx=10, pady=10)
                contentTextbox=CTkTextbox(viewRequestTopLevel, width=160,height=60)
                contentTextbox.grid(row=2, column=1)
                contentTextbox.insert("1.0", currentRequest.getContent())
                contentTextbox.configure(state="disabled")
                    
                statusLabel=CTkLabel(viewRequestTopLevel, text="Status:").grid(row=3, column=0, padx=10, pady=10)
                statusCombobox = CTkComboBox(master=viewRequestTopLevel, values=self.controller.getRequestStatus(), state="readonly")
                statusCombobox.grid(row=3, column=1, padx=10, pady=10)
                statusCombobox.set(currentRequest.getStatus())
                
                    
                creatingDateLabel=CTkLabel(viewRequestTopLevel, text="Creating Date:").grid(row=4, column=0, sticky="e")
                creatingDateLabel2=CTkLabel(viewRequestTopLevel, text=currentRequest.getCreatedDate().strftime("%Y-%m-%d %H:%M")).grid(row=4, column=1)
                    
                endDateLabel=CTkLabel(viewRequestTopLevel, text="End Date:").grid(row=5, column=0)
                    
                endDateEntry=DateEntry(viewRequestTopLevel, width=12, background="darkblue", foreground="white", borderwidth=2, date_pattern="yyyy-mm-dd")
                endDateEntry.grid(row=5, column=1, padx=10, pady=10)
                endDateEntry.set_date(currentRequest.getEndDate())
                
                    
                respondentLabel=CTkLabel(viewRequestTopLevel, text="Respondent:")
                respondentLabel.grid(row=6, column=0)
                respondentLabel2=CTkLabel(viewRequestTopLevel, text="None")
                respondentLabel2.grid(row=6, column=1)
                
                
                
                if currentRequest.getRespondent():
                    respondentLabel2.configure(text=currentRequest.getRespondent().getUsername())
                
                
                
                def updateRequestFunc():
                    tempStatus= statusCombobox.get()
                    tempEndDate= endDateEntry.get_date()
                    self.controller.updateRequest(currentRequest, tempStatus,tempEndDate)
                    viewRequestTopLevel.destroy()
                    backFunc()
                    
                    
                    
                def requestHistoryFunc():
                    requestHistoryToplevel =TopLevelWindow(viewRequestTopLevel, "History", geometry="600x230+420+340") # 
                    historyList=currentRequest.getChangesHistory()
                    historyListbox = CTkListbox(requestHistoryToplevel, hover_color='grey', highlight_color='royalblue3')
                    historyListbox.pack(fill="both", expand=True, padx=10, pady=10)
                    
                    i=0
                    for history in historyList:
                        historyListbox.insert(i, history)
                        i+=1
                
                updateRequestButton=CTkButton(viewRequestTopLevel,
                text="Edit",
                fg_color="red", 
                hover_color="black",
                width=80,
                command= updateRequestFunc
                )
                updateRequestButton.grid(row=1, column=2, padx=20)
                
                requestHistoryButton=CTkButton(viewRequestTopLevel,
                        text="History",
                        fg_color="red", 
                        hover_color="black",
                        width=80,
                        command= requestHistoryFunc
                        )
                requestHistoryButton.grid(row=2, column=2, padx=20)
                
                
        
        
        
        
        def sendRequestMesssageFunc():
            if requestsListbox.get():
                currentRequest=requestsList[requestsListbox.curselection()]
                sendMessageTopLevel =TopLevelWindow(self.app,title= "Send message", geometry="320x160+530+315")
                contentLabel= CTkLabel(sendMessageTopLevel, text="your message:", font=("Arial", 15))
                contentLabel.grid(row=0, column= 0, padx=10, pady=10)
                
                contentTextbox= CTkTextbox(sendMessageTopLevel, width=180, height=80)
                contentTextbox.grid(row=0, column= 1, padx=10, pady=10)
                
                def sendFunc():
                    tempContent= contentTextbox.get("1.0", "end-1c")
                    self.controller.sendRequestMessage(currentRequest, tempContent)
                    sendMessageTopLevel.destroy()
                sendButton= CTkButton(sendMessageTopLevel,
                text="Send",
                command= sendFunc,
                fg_color="red", 
                hover_color="black",
                width=100
                )
                sendButton.place(x=115, y=115)
        
        
        
        def backFunc():
            reqestsFrame.destroy()
            requestsListbox.destroy()
            self.changeTitle("Employee Homepage")
        
  
        viewRequestButton=CTkButton(reqestsFrame,
        text="View",
        command= viewRequestFunc,
        fg_color="red", 
        hover_color="black",
        width=100
        )
        viewRequestButton.grid(row=0, column=0)
        
        sendRequestMesssageButton=CTkButton(reqestsFrame,
        text="send message",
        command= sendRequestMesssageFunc,
        fg_color="red", 
        hover_color="black",
        width=100
        )
        sendRequestMesssageButton.grid(row=0, column=1, padx=10, pady=10)
        
        
        backButton=CTkButton(reqestsFrame,
        text="Main menu", 
        command= backFunc,
        fg_color="grey", 
        hover_color="black"
        )
        backButton.place(x=45, y=250)
    
    
    
    
    def allRequestsFunc(self, requestsList):
        self.changeTitle("All Requests")
        reqestsFrame=ctk.CTkFrame(master=self.app, bg_color="lavender", fg_color="lavender", width=100)
        reqestsFrame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
            
        requestsListbox = CTkListbox(self.workspacesFrame, hover_color='grey', highlight_color='royalblue3')
        requestsListbox.pack(fill="both", expand=True, padx=10, pady=10)
        
            
        i=0
        for request in requestsList:
            temp= str(request.getRequestID()) +"  |  "+ request.getSubject() +"  |  "+ request.getStatus()
            requestsListbox.insert(i, temp)
            i+=1
            
        def viewRequestFunc():
            if requestsListbox.get():
                currentRequest=requestsList[requestsListbox.curselection()]
                viewRequestTopLevel =TopLevelWindow(self.app, f"Request {currentRequest.getRequestID()}", geometry="360x310+530+305")
            
            
            requesterLabel=CTkLabel(viewRequestTopLevel, text="requester:")
            requesterLabel.grid(row=0, column=0, padx=10, pady=0)
            requesterLabel2=CTkLabel(viewRequestTopLevel, text=currentRequest.getRequester().getUsername())
            requesterLabel2.grid(row=0, column=1, padx=10, pady=10)
            
                
            subjectLabel=CTkLabel(viewRequestTopLevel, text="subject:").grid(row=1, column=0, padx=10, pady=10)
            subjectCombobox = CTkComboBox(master=viewRequestTopLevel, values=[], state="readonly")
            subjectCombobox.grid(row=1, column=1, padx=10, pady=10)
            subjectCombobox.set(currentRequest.getSubject())
            subjectCombobox.configure(state="disabled")
                
                
            contentLabel=CTkLabel(viewRequestTopLevel, text="Content:").grid(row=2, column=0, padx=10, pady=10)
            contentTextbox=CTkTextbox(viewRequestTopLevel, width=160,height=60)
            contentTextbox.grid(row=2, column=1)
            contentTextbox.insert("1.0", currentRequest.getContent())
            contentTextbox.configure(state="disabled")
                
            statusLabel=CTkLabel(viewRequestTopLevel, text="Status:").grid(row=3, column=0, padx=10, pady=10)
            statusCombobox = CTkComboBox(master=viewRequestTopLevel, values=[], state="readonly")
            statusCombobox.grid(row=3, column=1, padx=10, pady=10)
            statusCombobox.set(currentRequest.getStatus())
            statusCombobox.configure(state="disabled")
            
            
                
            creatingDateLabel=CTkLabel(viewRequestTopLevel, text="Creating Date:").grid(row=4, column=0, sticky="e")
            creatingDateLabel2=CTkLabel(viewRequestTopLevel, text=currentRequest.getCreatedDate().strftime("%Y-%m-%d %H:%M")).grid(row=4, column=1)
                
            endDateLabel=CTkLabel(viewRequestTopLevel, text="End Date:").grid(row=5, column=0)
                
            endDateEntry=DateEntry(viewRequestTopLevel, width=12, background="darkblue", foreground="white", borderwidth=2, date_pattern="yyyy-mm-dd")
            endDateEntry.grid(row=5, column=1, padx=10, pady=10)
            endDateEntry.set_date(currentRequest.getEndDate())
            endDateEntry.configure(state="disabled")
                
            respondentLabel=CTkLabel(viewRequestTopLevel, text="Respondent:")
            respondentLabel.grid(row=6, column=0)
            respondentLabel2=CTkLabel(viewRequestTopLevel, text="None")
            respondentLabel2.grid(row=6, column=1)
            
            
            
            if currentRequest.getRespondent():
                respondentLabel2.configure(text=currentRequest.getRespondent().getUsername())
                
                
                
                
        
        def searchRequestFunc():
            searchRequestTopLevel= TopLevelWindow(self.app,title= "Search", geometry="380x180+530+315")
            selected_option = ctk.StringVar(value="")  
            
            
            subjectLabel=CTkLabel(searchRequestTopLevel, text="subject:").grid(row=0, column=0, padx=10, pady=10)
            subjectCombobox = CTkComboBox(master=searchRequestTopLevel, values=self.controller.getRequestSubjects(), width=120, state="readonly")
            subjectCombobox.grid(row=0, column=1, padx=10, pady=10)
            subjectCombobox.set("All")
            
            statusLabel=CTkLabel(searchRequestTopLevel, text="Status:").grid(row=1, column=0, padx=10, pady=10)
            statusCombobox = CTkComboBox(master=searchRequestTopLevel, values=self.controller.getRequestStatus(), width=120, state="readonly")
            statusCombobox.grid(row=1, column=1, padx=10, pady=10)
            statusCombobox.set("All")
            
            submitDateLabel=CTkLabel(searchRequestTopLevel, text="submited from").grid(row=2, column=0)
            submitDateEntry=DateEntry(searchRequestTopLevel, width=8, background="darkblue", foreground="white", borderwidth=2, date_pattern="yyyy-mm-dd")
            submitDateEntry.grid(row=2, column=1, padx=10, pady=10)
            submitDateEntry.set_date("2023-01-01")
            submitDateLabel2=CTkLabel(searchRequestTopLevel, text="to", width=5).grid(row=2, column=2)
            submitDateEntry2=DateEntry(searchRequestTopLevel, width=8, background="darkblue", foreground="white", borderwidth=2, date_pattern="yyyy-mm-dd")
            submitDateEntry2.grid(row=2, column=3, padx=10, pady=10)
            
            
            endDateLabel=CTkLabel(searchRequestTopLevel, text="Ends from").grid(row=3, column=0)
            endDateEntry=DateEntry(searchRequestTopLevel, width=9, background="darkblue", foreground="white", borderwidth=2, date_pattern="yyyy-mm-dd")
            endDateEntry.grid(row=3, column=1, padx=0, pady=10)
            endDateEntry.set_date("2023-01-01")
            endDateLabel2=CTkLabel(searchRequestTopLevel, text="to").grid(row=3, column=2)
            endDateEntry2=DateEntry(searchRequestTopLevel, width=9, background="darkblue", foreground="white", borderwidth=2, date_pattern="yyyy-mm-dd")
            endDateEntry2.grid(row=3, column=3, padx=0, pady=10)
            
            
            def searchFunc():
                results=self.controller.getAllRequests()
                status=statusCombobox.get()
                subject=subjectCombobox.get()
                submitDate=submitDateEntry.get_date()
                submitDate2=submitDateEntry2.get_date()
                endDate=endDateEntry.get_date()
                endDate2=endDateEntry2.get_date()
                
                
                if status!="All":
                    results = [req for req in results if req.getStatus() == status]
                if subject!="All":
                    results = [req for req in results if req.getSubject() == subject]
                    
                results = [req for req in results if (submitDate <= req.getCreatedDate().date() <= submitDate2)]
                results = [req for req in results if req not in [req2 for req2 in results if req2.getEndDate() and (endDate >= req2.getEndDate() or req2.getEndDate() >= endDate2)] ]


                searchRequestTopLevel.destroy()
                backFunc()
                self.allRequestsFunc(results)
            
            searchButton=CTkButton(searchRequestTopLevel,
            text="Done",
            command= searchFunc,
            fg_color="red", 
            hover_color="black",
            width=100
            )
            searchButton.place(x=270, y=20)
        
        
        
        
        def backFunc():
            reqestsFrame.destroy()
            requestsListbox.destroy()
            self.changeTitle("Employee Homepage")

        viewRequestButton=CTkButton(reqestsFrame,
        text="View",
        command= viewRequestFunc,
        fg_color="red", 
        hover_color="black",
        width=100
        )
        viewRequestButton.grid(row=0, column=0, padx=50, pady=10)
        
        searchRequestButton=CTkButton(reqestsFrame,
        text="Search",
        command= searchRequestFunc,
        fg_color="red", 
        hover_color="black",
        width=100
        )
        searchRequestButton.grid(row=1, column=0, padx=10, pady=10)
        
        backButton=CTkButton(reqestsFrame,
        text="Main menu", 
        command= backFunc,
        fg_color="grey", 
        hover_color="black"
        )
        backButton.place(x=45, y=250)
    
    
    
    def messagesFunc(self):
        self.changeTitle("Messages")
        messageslist= self.controller.getMessages()
        
        messagesFrame=CTkFrame(master=self.app, bg_color="lavender", fg_color="lavender", width=100)
        messagesFrame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        
        messagesListBox= CTkListbox(self.workspacesFrame, hover_color='grey', highlight_color='royalblue3')
        messagesListBox.pack(fill="both", expand=True, padx=10, pady=10)
        
        i=0
        for mess in messageslist:
            if mess.getType() == "requestMessage":
                temp= f"Request {mess.getRequest().getRequestID()} | {mess.getSender().getUsername()}: {mess.getContent()[:15].splitlines()[0]}..."
            else:
                temp= f"Manager: {mess.getContent()[:25].splitlines()[0]}..."
            messagesListBox.insert(i, temp)
            i+=1
        
        
        
        def viewMessageFunc():
            if messagesListBox.get():
                currentMessage= messageslist[messagesListBox.curselection()]
                
                viewMessageTopLevel = TopLevelWindow(messagesFrame, currentMessage.getSender().getUsername())
                
                messageLabel= CTkLabel(viewMessageTopLevel, text=currentMessage.getContent())
                messageLabel.place(x=50, y=10)
                
                
        def backFunc():
            messagesFrame.destroy()
            messagesListBox.destroy()
            self.changeTitle("Manager Homepage")
            
            
        
        viewMessageButton=CTkButton(messagesFrame, 
        text="View",
        fg_color="red", 
        hover_color="black",
        width=100,
        command=viewMessageFunc
        )
        viewMessageButton.grid(row=0, column=0, padx=70, pady=30)
        
        backButton=CTkButton(messagesFrame,
        text="Main menu", 
        command= backFunc,
        fg_color="grey", 
        hover_color="black"
        )
        backButton.place(x=45, y=250)
    
    
    def surveysFunc(self):
        self.changeTitle("Surveys")
        surveysFrame=ctk.CTkFrame(master=self.app, bg_color="lavender", fg_color="lavender", width=100)
        surveysFrame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        
        
        def answeringSurveysFunc():
            SurveysFrame=ctk.CTkFrame(master=self.app, bg_color="lavender", fg_color="lavender", width=100)
            SurveysFrame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
            answerinSurveysListbox = CTkListbox(self.workspacesFrame, hover_color='grey', highlight_color='royalblue3')
            answerinSurveysListbox.pack(fill="both", expand=True, padx=10, pady=10)
            
            surveysList=[i[0] for i in self.controller.getAnsweringSurveys() if i[1]==False]  #surveys not answered yet

            j=0
            for survey in surveysList:
                temp= survey.getQuestion()
                answerinSurveysListbox.insert(j, temp)
                j+=1
                
            def viewSurveyFunc():
                if answerinSurveysListbox.get():
                    currentSurvey=surveysList[answerinSurveysListbox.curselection()]
                    answerSurveyTopLevel =TopLevelWindow(self.app,title= "Answer survey", geometry="320x175+530+315")
                    CTkLabel(answerSurveyTopLevel, text=None).grid(row=0, column= 0, pady=10)
                    questionLabel=CTkLabel(answerSurveyTopLevel, text=f"Question: {currentSurvey.getQuestion()}")
                    questionLabel.place(x=15, y=7)
                    answerLabel= CTkLabel(answerSurveyTopLevel, text="your answer:")
                    answerLabel.grid(row=1, column= 0, padx=10, pady=10)
                    
                    answerTextbox= CTkTextbox(answerSurveyTopLevel, width=180, height=80)
                    answerTextbox.grid(row=1, column= 1, padx=10, pady=10)
                    
                    def sendFunc():
                        tempAnswer= answerTextbox.get("1.0", "end-1c")
                        self.controller.answerSurvey(currentSurvey, tempAnswer)
                        answerSurveyTopLevel.destroy()
                        SurveysFrame.destroy()
                        answerinSurveysListbox.destroy()
                    sendButton= CTkButton(answerSurveyTopLevel,
                    text="Send",
                    command= sendFunc,
                    fg_color="red", 
                    hover_color="black",
                    width=100
                    )
                    sendButton.place(x=115, y=145)
                    
                    
            
            
            def backFunc2():
                SurveysFrame.destroy()
                answerinSurveysListbox.destroy()
                
                
            viewSurveyButton=CTkButton(SurveysFrame, 
            text="Answer",
            fg_color="red", 
            hover_color="black",
            width=100,
            command=viewSurveyFunc
            )
            viewSurveyButton.place(x=50, y=20)
            back2Button=CTkButton(SurveysFrame, 
            text="back",
            fg_color="grey", 
            hover_color="black",
            command=backFunc2
            )
            back2Button.place(x=45, y=250)
            
    

        
        def viewingSurveysFunc():
            SurveysFrame=ctk.CTkFrame(master=self.app, bg_color="lavender", fg_color="lavender", width=100)
            SurveysFrame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
            viewingSurveysListbox = CTkListbox(self.workspacesFrame, hover_color='grey', highlight_color='royalblue3')
            viewingSurveysListbox.pack(fill="both", expand=True, padx=10, pady=10)
            
            viewingSurveysList=self.controller.getViewingSurveys()
            
            j=0
            for survey in viewingSurveysList:
                temp= survey.getQuestion()
                viewingSurveysListbox.insert(j, temp)
                j+=1
                
                
                
                
            def viewResultFunc():
                if viewingSurveysListbox.get():
                    currentSurvey=viewingSurveysList[viewingSurveysListbox.curselection()]
                    viewAnswersTopLevel= TopLevelWindow(SurveysFrame, "Answers")
                    
                    answersListbox=CTkListbox(viewAnswersTopLevel, hover_color='grey', highlight_color='royalblue3')
                    answersListbox.pack(fill="both", expand=True, padx=10, pady=10)
                    
                    # print(123, currentSurvey.getAnswers())
                    i=0
                    for answer in currentSurvey.getAnswers():
                        temp= f"{answer[0]}: \"{answer[1]}\""
                        answersListbox.insert(i, temp)
                        i+=1
                
            def backFunc2():
                SurveysFrame.destroy()
                viewingSurveysListbox.destroy()
            
            
            viewResultsButton=CTkButton(SurveysFrame, 
            text="View Results",
            fg_color="red", 
            hover_color="black",
            width=100,
            command=viewResultFunc
            )
            viewResultsButton.place(x=50, y=20)
            
            back3Button=CTkButton(SurveysFrame, 
            text="back",
            fg_color="grey", 
            hover_color="black",
            command=backFunc2
            )
            back3Button.place(x=45, y=250)
        
        
        
        
        def backFunc():
            surveysFrame.destroy()
        
        answeringSurveysButton=CTkButton(surveysFrame, 
        text="Answer surveys",
        fg_color="red", 
        hover_color="black",
        width=100,
        command=answeringSurveysFunc
        )
        answeringSurveysButton.grid(row=0, column=0, padx=50, pady=15)
        
        viewingSurveysButton=CTkButton(surveysFrame, 
        text="View survey results",
        fg_color="red", 
        hover_color="black",
        width=100,
        command=viewingSurveysFunc
        )
        viewingSurveysButton.grid(row=1, column=0, padx=50, pady=15)
        
        backButton=CTkButton(surveysFrame,
        text="Main menu", 
        command= backFunc,
        fg_color="grey", 
        hover_color="black"
        )
        backButton.place(x=45, y=250)
        
        
        
        
        
     
     
class ClientWindow(Window):
    def __init__(self, controller):
        super().__init__(controller, "Client Homepage")
        
        self.app.grid_columnconfigure(0, weight=1)  # Column 0 (left)
        self.app.grid_columnconfigure(0, weight=1)  # Column 1 (right)
        self.app.grid_rowconfigure(0, weight=1)     # Row 0 (full height)


        self.buttonsFrame=ctk.CTkFrame(master=self.app, bg_color="lavender", fg_color="lavender", width=100)
        self.buttonsFrame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.workspacesFrame=ctk.CTkFrame(self.app, bg_color="lavender", fg_color="mintcream")
        self.workspacesFrame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
        
        
        yourRequestsButton=CTkButton(self.buttonsFrame, 
        text="Your requests",
        fg_color="red", 
        hover_color="black",
        width=100,
        command=self.yourRequestsFunc
        )
        yourRequestsButton.place(x=53, y=10)
        
        CTkLabel(self.buttonsFrame, text=None, height=40).grid(row=0,column=1, pady=4)
        
        allRequestsButton=CTkButton(self.buttonsFrame, 
        text="All requests",
        fg_color="red", 
        hover_color="black",
        width=100,
        command=lambda: self.allRequestsFunc(self.controller.getAllRequests())
        )
        allRequestsButton.grid(row=1, column=0, padx=10, pady=10)
        
        messagesButton=CTkButton(self.buttonsFrame, 
        text="Messages",
        fg_color="red", 
        hover_color="black",
        width=100,
        command=self.messagesFunc
        )
        messagesButton.grid(row=1, column=1, padx=10, pady=10)
        
        newRequestButton=CTkButton(self.buttonsFrame, 
        text="New request",
        fg_color="red", 
        hover_color="black",
        width=100,
        command=self.newRequestFunc
        )
        newRequestButton.grid(row=2, column=0, padx=10, pady=10)
        
        surveysButton=CTkButton(self.buttonsFrame, 
        text="Surveys",
        fg_color="red", 
        hover_color="black",
        width=100,
        command=self.surveysFunc
        )
        surveysButton.grid(row=2, column=1, padx=10, pady=10)
        
        LogoutButton=CTkButton(self.buttonsFrame,
        text="Logout", 
        command= lambda: self.app.destroy(),
        fg_color="grey", 
        hover_color="black"
        )
        LogoutButton.place(x=45, y=250)
        self.runWindow()   
  
        self.runWindow()
 ############################################################################################################################################################################
  
    def yourRequestsFunc(self):
        self.changeTitle("Your Requests")
        reqestsFrame=ctk.CTkFrame(master=self.app, bg_color="lavender", fg_color="lavender", width=100)
        reqestsFrame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
            
        requestsListbox = CTkListbox(self.workspacesFrame, hover_color='grey', highlight_color='royalblue3')
        requestsListbox.pack(fill="both", expand=True, padx=10, pady=10)
        
        requestsList=self.controller.getMyRequests()
            
        i=0
        for request in requestsList:
            temp= str(request.getRequestID()) +"  |  "+ request.getSubject() +"  |  "+ request.getStatus()
            requestsListbox.insert(i, temp)
            i+=1
            
        def viewRequestFunc():
            if requestsListbox.get():
                currentRequest=requestsList[requestsListbox.curselection()]
                viewRequestTopLevel =TopLevelWindow(self.app, f"Request {currentRequest.getRequestID()}", geometry="360x310+530+305")
                
                requesterLabel=CTkLabel(viewRequestTopLevel, text="requester:")
                requesterLabel.grid(row=0, column=0, padx=10, pady=0)
                requesterLabel2=CTkLabel(viewRequestTopLevel, text=currentRequest.getRequester().getUsername())
                requesterLabel2.grid(row=0, column=1, padx=10, pady=10)
                
                    
                subjectLabel=CTkLabel(viewRequestTopLevel, text="subject:").grid(row=1, column=0, padx=10, pady=10)
                subjectCombobox = CTkComboBox(master=viewRequestTopLevel, values=[], state="readonly")
                subjectCombobox.grid(row=1, column=1, padx=10, pady=10)
                subjectCombobox.set(currentRequest.getSubject())
                subjectCombobox.configure(state="disabled")
                    
                    
                contentLabel=CTkLabel(viewRequestTopLevel, text="Content:").grid(row=2, column=0, padx=10, pady=10)
                contentTextbox=CTkTextbox(viewRequestTopLevel, width=160,height=60)
                contentTextbox.grid(row=2, column=1)
                contentTextbox.insert("1.0", currentRequest.getContent())
                contentTextbox.configure(state="disabled")
                    
                statusLabel=CTkLabel(viewRequestTopLevel, text="Status:").grid(row=3, column=0, padx=10, pady=10)
                statusCombobox = CTkComboBox(master=viewRequestTopLevel, values=self.controller.getRequestStatus(), state="readonly")
                statusCombobox.grid(row=3, column=1, padx=10, pady=10)
                statusCombobox.set(currentRequest.getStatus())
                statusCombobox.configure(state="disabled")
                
                    
                creatingDateLabel=CTkLabel(viewRequestTopLevel, text="Creating Date:").grid(row=4, column=0, sticky="e")
                creatingDateLabel2=CTkLabel(viewRequestTopLevel, text=currentRequest.getCreatedDate().strftime("%Y-%m-%d %H:%M")).grid(row=4, column=1)
                    
                endDateLabel=CTkLabel(viewRequestTopLevel, text="End Date:").grid(row=5, column=0)
                    
                endDateEntry=DateEntry(viewRequestTopLevel, width=12, background="darkblue", foreground="white", borderwidth=2, date_pattern="yyyy-mm-dd")
                endDateEntry.grid(row=5, column=1, padx=10, pady=10)
                endDateEntry.set_date(currentRequest.getEndDate())
                endDateEntry.configure(state="disabled")
                
                    
                respondentLabel=CTkLabel(viewRequestTopLevel, text="Respondent:")
                respondentLabel.grid(row=6, column=0)
                respondentLabel2=CTkLabel(viewRequestTopLevel, text="None")
                respondentLabel2.grid(row=6, column=1)
                
                
                
                if currentRequest.getRespondent():
                    respondentLabel2.configure(text=currentRequest.getRespondent().getUsername())
                
         
                def requestHistoryFunc():
                    requestHistoryToplevel =TopLevelWindow(viewRequestTopLevel, "History", geometry="600x230+420+340") # 
                    historyList=currentRequest.getChangesHistory()
                    historyListbox = CTkListbox(requestHistoryToplevel, hover_color='grey', highlight_color='royalblue3')
                    historyListbox.pack(fill="both", expand=True, padx=10, pady=10)
                    
                    i=0
                    for history in historyList:
                        historyListbox.insert(i, history)
                        i+=1
                
                
                requestHistoryButton=CTkButton(viewRequestTopLevel,
                        text="History",
                        fg_color="red", 
                        hover_color="black",
                        width=80,
                        command= requestHistoryFunc
                        )
                requestHistoryButton.grid(row=1, column=2, padx=20)
                
                
                
                
                
                # getting client rating
                if not currentRequest.getResponseRate():
                    ratingWindow= TopLevelWindow(viewRequestTopLevel, "Rating", geometry="260x100+580+380")
                    

                    # Output label
                    output_label = CTkLabel(ratingWindow, text="Your Rating: 0", font=("Arial", 14))
                    output_label.pack(pady=5)

                    def update_label(value):
                        output_label.configure(text=f"Your Rating: {int(float(value))}")
                    
                    slider = CTkSlider(ratingWindow, from_=1, to=10, number_of_steps=9, command=update_label)
                    slider.pack(pady=5)
                    slider.set(0)
                    
                    def setRatingFunc():
                        if slider.get()!=0:
                            self.controller.setResponseRate(currentRequest, slider.get())
                            ratingWindow.destroy()
                            
                    rateButton= CTkButton(ratingWindow,
                        text="Rate",
                        fg_color="red", 
                        hover_color="black",
                        width=80,
                        command= setRatingFunc
                        )
                    rateButton.pack(pady= 5)
                
                
        
        
        
        
        def sendRequestMesssageFunc():
            if requestsListbox.get():
                currentRequest=requestsList[requestsListbox.curselection()]
                sendMessageTopLevel =TopLevelWindow(self.app,title= "Send message", geometry="320x160+530+315")
                contentLabel= CTkLabel(sendMessageTopLevel, text="your message:", font=("Arial", 15))
                contentLabel.grid(row=0, column= 0, padx=10, pady=10)
                
                contentTextbox= CTkTextbox(sendMessageTopLevel, width=180, height=80)
                contentTextbox.grid(row=0, column= 1, padx=10, pady=10)
                
                def sendFunc():
                    tempContent= contentTextbox.get("1.0", "end-1c")
                    self.controller.sendRequestMessage(currentRequest, tempContent)
                    sendMessageTopLevel.destroy()
                sendButton= CTkButton(sendMessageTopLevel,
                text="Send",
                command= sendFunc,
                fg_color="red", 
                hover_color="black",
                width=100
                )
                sendButton.place(x=115, y=115)
        
        
        
        def backFunc():
            reqestsFrame.destroy()
            requestsListbox.destroy()
            self.changeTitle("Client Homepage")
        
  
        viewRequestButton=CTkButton(reqestsFrame,
        text="View",
        command= viewRequestFunc,
        fg_color="red", 
        hover_color="black",
        width=100
        )
        viewRequestButton.grid(row=0, column=0)
        
        sendRequestMesssageButton=CTkButton(reqestsFrame,
        text="send message",
        command= sendRequestMesssageFunc,
        fg_color="red", 
        hover_color="black",
        width=100
        )
        sendRequestMesssageButton.grid(row=0, column=1, padx=10, pady=10)
        
        
        backButton=CTkButton(reqestsFrame,
        text="Main menu", 
        command= backFunc,
        fg_color="grey", 
        hover_color="black"
        )
        backButton.place(x=45, y=250)
    
    
    def allRequestsFunc(self, requestsList):
        self.changeTitle("All Requests")
        reqestsFrame=ctk.CTkFrame(master=self.app, bg_color="lavender", fg_color="lavender", width=100)
        reqestsFrame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
            
        requestsListbox = CTkListbox(self.workspacesFrame, hover_color='grey', highlight_color='royalblue3')
        requestsListbox.pack(fill="both", expand=True, padx=10, pady=10)
        
            
        i=0
        for request in requestsList:
            temp= str(request.getRequestID()) +"  |  "+ request.getSubject() +"  |  "+ request.getStatus()
            requestsListbox.insert(i, temp)
            i+=1
            
        def viewRequestFunc():
            if requestsListbox.get():
                currentRequest=requestsList[requestsListbox.curselection()]
                viewRequestTopLevel =TopLevelWindow(self.app, f"Request {currentRequest.getRequestID()}", geometry="360x310+530+305")
            
            
            requesterLabel=CTkLabel(viewRequestTopLevel, text="requester:")
            requesterLabel.grid(row=0, column=0, padx=10, pady=0)
            requesterLabel2=CTkLabel(viewRequestTopLevel, text=currentRequest.getRequester().getUsername())
            requesterLabel2.grid(row=0, column=1, padx=10, pady=10)
            
                
            subjectLabel=CTkLabel(viewRequestTopLevel, text="subject:").grid(row=1, column=0, padx=10, pady=10)
            subjectCombobox = CTkComboBox(master=viewRequestTopLevel, values=[], state="readonly")
            subjectCombobox.grid(row=1, column=1, padx=10, pady=10)
            subjectCombobox.set(currentRequest.getSubject())
            subjectCombobox.configure(state="disabled")
                
                
            contentLabel=CTkLabel(viewRequestTopLevel, text="Content:").grid(row=2, column=0, padx=10, pady=10)
            contentTextbox=CTkTextbox(viewRequestTopLevel, width=160,height=60)
            contentTextbox.grid(row=2, column=1)
            contentTextbox.insert("1.0", currentRequest.getContent())
            contentTextbox.configure(state="disabled")
                
            statusLabel=CTkLabel(viewRequestTopLevel, text="Status:").grid(row=3, column=0, padx=10, pady=10)
            statusCombobox = CTkComboBox(master=viewRequestTopLevel, values=[], state="readonly")
            statusCombobox.grid(row=3, column=1, padx=10, pady=10)
            statusCombobox.set(currentRequest.getStatus())
            statusCombobox.configure(state="disabled")
            
            
                
            creatingDateLabel=CTkLabel(viewRequestTopLevel, text="Creating Date:").grid(row=4, column=0, sticky="e")
            creatingDateLabel2=CTkLabel(viewRequestTopLevel, text=currentRequest.getCreatedDate().strftime("%Y-%m-%d %H:%M")).grid(row=4, column=1)
                
            endDateLabel=CTkLabel(viewRequestTopLevel, text="End Date:").grid(row=5, column=0)
                
            endDateEntry=DateEntry(viewRequestTopLevel, width=12, background="darkblue", foreground="white", borderwidth=2, date_pattern="yyyy-mm-dd")
            endDateEntry.grid(row=5, column=1, padx=10, pady=10)
            endDateEntry.set_date(currentRequest.getEndDate())
            endDateEntry.configure(state="disabled")
                
            respondentLabel=CTkLabel(viewRequestTopLevel, text="Respondent:")
            respondentLabel.grid(row=6, column=0)
            respondentLabel2=CTkLabel(viewRequestTopLevel, text="None")
            respondentLabel2.grid(row=6, column=1)
            
            
            
            if currentRequest.getRespondent():
                respondentLabel2.configure(text=currentRequest.getRespondent().getUsername())
                
                
                
                
        
        def searchRequestFunc():
            searchRequestTopLevel= TopLevelWindow(self.app,title= "Search", geometry="380x180+530+315")
            selected_option = ctk.StringVar(value="")  
            
            
            subjectLabel=CTkLabel(searchRequestTopLevel, text="subject:").grid(row=0, column=0, padx=10, pady=10)
            subjectCombobox = CTkComboBox(master=searchRequestTopLevel, values=self.controller.getRequestSubjects(), width=120, state="readonly")
            subjectCombobox.grid(row=0, column=1, padx=10, pady=10)
            subjectCombobox.set("All")
            
            statusLabel=CTkLabel(searchRequestTopLevel, text="Status:").grid(row=1, column=0, padx=10, pady=10)
            statusCombobox = CTkComboBox(master=searchRequestTopLevel, values=self.controller.getRequestStatus(), width=120, state="readonly")
            statusCombobox.grid(row=1, column=1, padx=10, pady=10)
            statusCombobox.set("All")
            
            submitDateLabel=CTkLabel(searchRequestTopLevel, text="submited from").grid(row=2, column=0)
            submitDateEntry=DateEntry(searchRequestTopLevel, width=8, background="darkblue", foreground="white", borderwidth=2, date_pattern="yyyy-mm-dd")
            submitDateEntry.grid(row=2, column=1, padx=10, pady=10)
            submitDateEntry.set_date("2023-01-01")
            submitDateLabel2=CTkLabel(searchRequestTopLevel, text="to", width=5).grid(row=2, column=2)
            submitDateEntry2=DateEntry(searchRequestTopLevel, width=8, background="darkblue", foreground="white", borderwidth=2, date_pattern="yyyy-mm-dd")
            submitDateEntry2.grid(row=2, column=3, padx=10, pady=10)
            
            
            endDateLabel=CTkLabel(searchRequestTopLevel, text="Ends from").grid(row=3, column=0)
            endDateEntry=DateEntry(searchRequestTopLevel, width=9, background="darkblue", foreground="white", borderwidth=2, date_pattern="yyyy-mm-dd")
            endDateEntry.grid(row=3, column=1, padx=0, pady=10)
            endDateEntry.set_date("2023-01-01")
            endDateLabel2=CTkLabel(searchRequestTopLevel, text="to").grid(row=3, column=2)
            endDateEntry2=DateEntry(searchRequestTopLevel, width=9, background="darkblue", foreground="white", borderwidth=2, date_pattern="yyyy-mm-dd")
            endDateEntry2.grid(row=3, column=3, padx=0, pady=10)
            
            
            def searchFunc():
                results=self.controller.getAllRequests()
                status=statusCombobox.get()
                subject=subjectCombobox.get()
                submitDate=submitDateEntry.get_date()
                submitDate2=submitDateEntry2.get_date()
                endDate=endDateEntry.get_date()
                endDate2=endDateEntry2.get_date()
                
                
                if status!="All":
                    results = [req for req in results if req.getStatus() == status]
                if subject!="All":
                    results = [req for req in results if req.getSubject() == subject]
                    
                results = [req for req in results if (submitDate <= req.getCreatedDate().date() <= submitDate2)]
                results = [req for req in results if req not in [req2 for req2 in results if req2.getEndDate() and (endDate >= req2.getEndDate() or req2.getEndDate() >= endDate2)] ]


                searchRequestTopLevel.destroy()
                backFunc()
                self.allRequestsFunc(results)
            
            searchButton=CTkButton(searchRequestTopLevel,
            text="Done",
            command= searchFunc,
            fg_color="red", 
            hover_color="black",
            width=100
            )
            searchButton.place(x=270, y=20)
        
        
        
        
        def backFunc():
            reqestsFrame.destroy()
            requestsListbox.destroy()
            self.changeTitle("Client Homepage")

        viewRequestButton=CTkButton(reqestsFrame,
        text="View",
        command= viewRequestFunc,
        fg_color="red", 
        hover_color="black",
        width=100
        )
        viewRequestButton.grid(row=0, column=0, padx=50, pady=10)
        
        searchRequestButton=CTkButton(reqestsFrame,
        text="Search",
        command= searchRequestFunc,
        fg_color="red", 
        hover_color="black",
        width=100
        )
        searchRequestButton.grid(row=1, column=0, padx=10, pady=10)
        
        backButton=CTkButton(reqestsFrame,
        text="Main menu", 
        command= backFunc,
        fg_color="grey", 
        hover_color="black"
        )
        backButton.place(x=45, y=250)
    
    
    
    def messagesFunc(self):
        self.changeTitle("Messages")
        messageslist= self.controller.getMessages()
        
        messagesFrame=CTkFrame(master=self.app, bg_color="lavender", fg_color="lavender", width=100)
        messagesFrame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        
        messagesListBox= CTkListbox(self.workspacesFrame, hover_color='grey', highlight_color='royalblue3')
        messagesListBox.pack(fill="both", expand=True, padx=10, pady=10)
        
        i=0
        for mess in messageslist:
            if mess.getType() == "requestMessage":
                temp= f"Request {mess.getRequest().getRequestID()} | {mess.getSender().getUsername()}: {mess.getContent()[:15].splitlines()[0]}..."
            else:
                temp= f"Manager: {mess.getContent()[:25].splitlines()[0]}..."
            messagesListBox.insert(i, temp)
            i+=1
        
        
        
        def viewMessageFunc():
            if messagesListBox.get():
                currentMessage= messageslist[messagesListBox.curselection()]
                
                viewMessageTopLevel = TopLevelWindow(messagesFrame, currentMessage.getSender().getUsername())
                
                messageLabel= CTkLabel(viewMessageTopLevel, text=currentMessage.getContent())
                messageLabel.place(x=50, y=10)
                
                
        def backFunc():
            messagesFrame.destroy()
            messagesListBox.destroy()
            self.changeTitle("Client Homepage")
            
            
        
        viewMessageButton=CTkButton(messagesFrame, 
        text="View",
        fg_color="red", 
        hover_color="black",
        width=100,
        command=viewMessageFunc
        )
        viewMessageButton.grid(row=0, column=0, padx=70, pady=30)
        
        backButton=CTkButton(messagesFrame,
        text="Main menu", 
        command= backFunc,
        fg_color="grey", 
        hover_color="black"
        )
        backButton.place(x=45, y=250)
    
    
    def newRequestFunc(self):
        self.changeTitle("Submit Request")
        newRequestFrame= CTkFrame(master=self.app, bg_color="lavender", fg_color="lavender", width=100)
        newRequestFrame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        
        subjectLabel= CTkLabel(self.workspacesFrame, text="Subject:")
        subjectLabel.place(x=10, y=10)
        subjectCombobox = CTkComboBox(master=self.workspacesFrame, values=self.controller.getRequestSubjects(), state="readonly")
        subjectCombobox.place(x=80, y=10)
        
        contentLabel= CTkLabel(self.workspacesFrame, text="Content:")
        contentLabel.place(x=10, y=60)
        contentTextbox= CTkTextbox(self.workspacesFrame, width=270, height=100, fg_color="lightgrey")
        contentTextbox.place(x=20, y=90)
        
        
        
        def sendFunc():
            subject=subjectCombobox.get()
            Content= contentTextbox.get("1.0", "end-1c")
            self.controller.createRequest(subject, Content)
            backFunc()
        
        sendButton=CTkButton(self.workspacesFrame,
        text="Submit",
        command= sendFunc,
        fg_color="red", 
        hover_color="black"
        )
        sendButton.place(x=85, y=290)
        
        
        
        def backFunc():
            newRequestFrame.destroy()
            subjectLabel.destroy()
            subjectCombobox.destroy()
            contentLabel.destroy()
            contentTextbox.destroy()
            self.changeTitle("Manager Homepage")
        
        
        backButton=CTkButton(newRequestFrame,
        text="Main menu", 
        command= backFunc,
        fg_color="grey", 
        hover_color="black"
        )
        backButton.place(x=45, y=250)
    
    
    def surveysFunc(self):
        self.changeTitle("Surveys")
        surveysFrame=ctk.CTkFrame(master=self.app, bg_color="lavender", fg_color="lavender", width=100)
        surveysFrame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        
        
        def answeringSurveysFunc():
            SurveysFrame=ctk.CTkFrame(master=self.app, bg_color="lavender", fg_color="lavender", width=100)
            SurveysFrame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
            answerinSurveysListbox = CTkListbox(self.workspacesFrame, hover_color='grey', highlight_color='royalblue3')
            answerinSurveysListbox.pack(fill="both", expand=True, padx=10, pady=10)
            
            surveysList=[i[0] for i in self.controller.getAnsweringSurveys() if i[1]==False]  #surveys not answered yet

            j=0
            for survey in surveysList:
                temp= survey.getQuestion()
                answerinSurveysListbox.insert(j, temp)
                j+=1
                
            def viewSurveyFunc():
                if answerinSurveysListbox.get():
                    currentSurvey=surveysList[answerinSurveysListbox.curselection()]
                    answerSurveyTopLevel =TopLevelWindow(self.app,title= "Answer survey", geometry="320x175+530+315")
                    CTkLabel(answerSurveyTopLevel, text=None).grid(row=0, column= 0, pady=10)
                    questionLabel=CTkLabel(answerSurveyTopLevel, text=f"Question: {currentSurvey.getQuestion()}")
                    questionLabel.place(x=15, y=7)
                    answerLabel= CTkLabel(answerSurveyTopLevel, text="your answer:")
                    answerLabel.grid(row=1, column= 0, padx=10, pady=10)
                    
                    answerTextbox= CTkTextbox(answerSurveyTopLevel, width=180, height=80)
                    answerTextbox.grid(row=1, column= 1, padx=10, pady=10)
                    
                    def sendFunc():
                        tempAnswer= answerTextbox.get("1.0", "end-1c")
                        self.controller.answerSurvey(currentSurvey, tempAnswer)
                        answerSurveyTopLevel.destroy()
                        SurveysFrame.destroy()
                        answerinSurveysListbox.destroy()
                    sendButton= CTkButton(answerSurveyTopLevel,
                    text="Send",
                    command= sendFunc,
                    fg_color="red", 
                    hover_color="black",
                    width=100
                    )
                    sendButton.place(x=115, y=145)
                    
                    
            
            
            def backFunc2():
                SurveysFrame.destroy()
                answerinSurveysListbox.destroy()
                
                
            viewSurveyButton=CTkButton(SurveysFrame, 
            text="Answer",
            fg_color="red", 
            hover_color="black",
            width=100,
            command=viewSurveyFunc
            )
            viewSurveyButton.place(x=50, y=20)
            back2Button=CTkButton(SurveysFrame, 
            text="back",
            fg_color="grey", 
            hover_color="black",
            command=backFunc2
            )
            back2Button.place(x=45, y=250)
            
            
            
            
        
        
        
        
        def viewingSurveysFunc():
            SurveysFrame=ctk.CTkFrame(master=self.app, bg_color="lavender", fg_color="lavender", width=100)
            SurveysFrame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
            viewingSurveysListbox = CTkListbox(self.workspacesFrame, hover_color='grey', highlight_color='royalblue3')
            viewingSurveysListbox.pack(fill="both", expand=True, padx=10, pady=10)
            
            viewingSurveysList=self.controller.getViewingSurveys()
            
            j=0
            for survey in viewingSurveysList:
                temp= survey.getQuestion()
                viewingSurveysListbox.insert(j, temp)
                j+=1
                
                
                
                
            def viewResultFunc():
                if viewingSurveysListbox.get():
                    currentSurvey=viewingSurveysList[viewingSurveysListbox.curselection()]
                    viewAnswersTopLevel= TopLevelWindow(SurveysFrame, "Answers")
                    
                    answersListbox=CTkListbox(viewAnswersTopLevel, hover_color='grey', highlight_color='royalblue3')
                    answersListbox.pack(fill="both", expand=True, padx=10, pady=10)
                    
                    # print(123, currentSurvey.getAnswers())
                    i=0
                    for answer in currentSurvey.getAnswers():
                        temp= f"{answer[0]}: \"{answer[1]}\""
                        answersListbox.insert(i, temp)
                        i+=1
                
            def backFunc2():
                SurveysFrame.destroy()
                viewingSurveysListbox.destroy()
            
            
            viewResultsButton=CTkButton(SurveysFrame, 
            text="View Results",
            fg_color="red", 
            hover_color="black",
            width=100,
            command=viewResultFunc
            )
            viewResultsButton.place(x=50, y=20)
            
            back3Button=CTkButton(SurveysFrame, 
            text="back",
            fg_color="grey", 
            hover_color="black",
            command=backFunc2
            )
            back3Button.place(x=45, y=250)
        
        
        
        
        def backFunc():
            surveysFrame.destroy()
        
        answeringSurveysButton=CTkButton(surveysFrame, 
        text="Answer surveys",
        fg_color="red", 
        hover_color="black",
        width=100,
        command=answeringSurveysFunc
        )
        answeringSurveysButton.grid(row=0, column=0, padx=50, pady=15)
        
        viewingSurveysButton=CTkButton(surveysFrame, 
        text="View survey results",
        fg_color="red", 
        hover_color="black",
        width=100,
        command=viewingSurveysFunc
        )
        viewingSurveysButton.grid(row=1, column=0, padx=50, pady=15)
        
        backButton=CTkButton(surveysFrame,
        text="Main menu", 
        command= backFunc,
        fg_color="grey", 
        hover_color="black"
        )
        backButton.place(x=45, y=250)
         
        
    
    
    
if __name__ == "__main__":
    pass