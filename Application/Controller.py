from Model.model import *
from View.view import *
import tkinter as tk
from customtkinter import *
import customtkinter as ctk




class Controller:
    def __init__(self):
        # self.app=CTk()
        self.systemManager=SystemManager()
        # self.loginWindow=LoginWindow(controller=self,app=self.app)
        
        
    
    
    def checkLogin(self, loginWindow, username, password):
        user=self.systemManager.loginCheck(username, password)
        if user:
            loginWindow.destroyWindow()
            
            if user.getRole() == "manager":
                ControllerManager(user)
            elif user.getRole() == "employee":
                ControllerEmployee(user)
            else:
                ControllerClient(user)
        else:
            loginWindow.invalidLogin()






###############################################################################################################################################################

class ControllerManager:
    def __init__(self, manager: Manager):
        self.manager= manager
        self.managerWindow=ManagerWindow(self)
        
        
 #____________________________________________ getter
        
    def getUsers(self) -> list[User]:
        """
        returns list of users.
        """
        return self.manager.viewAllUsers()
    
    def getRequests(self) -> list[Request]:
        """
        returns list of requests.
        """
        return self.manager.viewAllRequests()

    
    def getRequestSubjects(self) -> list[str]:
        """
        returns list of available subjects.
        """
        return self.manager.getRequestSubjects()
        
    def getRequestStatus(self) -> list[str]:
        """
        returns list of available status.
        """
        return self.manager.getRequestStatus()
        
    def getEmployees(self) -> list[Employee]:
        """
        returns list of employees.
        """
        usersList=self.getUsers()
        employeesList=[]
        for user in usersList:
            if user.getRole() == "employee":
                employeesList.append(user)
        return employeesList
    
    def getSurveys(self) -> list[Survey]:
        """
        returns list of Surveys.
        """
        return self.manager.getSurveys()
    
    
    def getMessages(self) -> list[Message]:
        """
        returns list of Messages.
        """
        return self.manager.getMessages()
        
        
 #____________________________________________ adding
    
    
    def addUser(self, username: str, password: str, role:str):
        """
        gets a username, password and role and adds the User.
        """
        self.manager.addUser(username, password, role)
        
    def addSubject(self, newSubject: str):
        """
        gets a new subject and adds to subjects.
        """
        self.manager.addSubject(newSubject)
        
    def addStatus(self, newStatus: str):
        """
        gets a new status and adds to status.
        """
        self.manager.addStatus(newStatus)
        
        
 #____________________________________________ removing
        
    def removeUser(self, user: User):
        """
        gets a User object and removes it.
        """
        self.manager.removeUser(user)
        
    def removeRequest(self, request: Request):
        """
        gets a request and removes it.
        """
        self.manager.removeRequest(request)


 #____________________________________________ changing
    
    def changeRole(self, user: User, newRole: str):
        """
        gets a User object and new role and changes role.
        """
        if user.getRole() != newRole:
            self.manager.changeRole(user, newRole)
        
    def editRequest(self, request, subejct, content, status, endDate):
        """
        gets a request object and  subejct, content, status and endDate, then edits the request attributes.
        """
        self.manager.editRequest(request, subejct, content, status, endDate)
        
    
 #____________________________________________ others
 
 

    def assignRequest(self, request: Request, employee: Employee):
        """
        gets a request and employee object and assigns the request to the employee .
        """
        self.manager.assignRequest(request, employee)
        
    def sendRequestMessage(self, request: Request, content: str):
        """
        gets a Request object and a text, then creates a RequestMessage.\n
        sends message to requester and respondent.
        """
        self.manager.sendRequestMessage(request, content)
        
    def createSurvey(self, question: str, receivers: list[User], viewers: list[User]):
        """
        gets a question, receivers and viewers list and creates a new Survey.
        """
        self.manager.createSurvey(question, receivers, viewers)
        
    def sendAnnouncement(self, content: str, receivers: list[User]):
        """
        gets an announcement content and creates an Announcement object.
        """
        self.manager.sendAnnouncement(content, receivers)
        
        
        
    
        
        
        
                
    

class ControllerEmployee:
    def __init__(self, employee: Employee):
        self.employee= employee
        self.employeeWindow=EmployeeWindow(self)
        
        
 #____________________________________________ getter

    def getAssignedRequests(self):
        """
        return a list of employye's assigned requests.
        """
        return self.employee.getAssignedRequests()
    
    
    def getAllRequests(self):
        """
        return a list of all requests.
        """
        return self.employee.getAllRequests()
    
    def getMessages(self) -> list[Message]:
        """
        returns list of employee's Messages.
        """
        return self.employee.getMessages()
    
    def getRequestSubjects(self) -> list[str]:
        """
        returns list of available subjects.
        """
        return self.employee.getRequestSubjects()
        
    def getRequestStatus(self) -> list[str]:
        """
        returns list of available status.
        """
        return self.employee.getRequestStatus()
    
    def getAnsweringSurveys(self)-> list:
        """
        returns list of answering surveys .\n
        [Survey, bool]
        """
        return self.employee.getAnsweringSurveys()
    
    def getViewingSurveys(self)-> list[Survey]:
        """
        returns list of viewing surveys .
        """
        return self.employee.getViewingSurveys()
    
    
    
 #____________________________________________ update

    def updateRequest(self, request: Request, newStatus: str, newEndDate):
        """
        gets a request, new status and new end-date and updates the request status.
        """
        self.employee.updateRequest(request, newStatus, newEndDate)
        
 #____________________________________________ others

    def sendRequestMessage(self, request: Request, content: str):
        """
        gets a Request object and a text, then creates a RequestMessage.\n
        sends message to requester and respondent.
        """
        self.employee.sendRequestMessage(request, content)
        
        
    def answerSurvey(self, survey: Survey, answer:str):
        """
        gets a Survey obejct and answer, then adds answer and username to survey.
        """
        self.employee.answerSurvey(survey, answer)
        
        
    
        
      
        
    
class ControllerClient:
    def __init__(self, client: Client):
        self.client= client
        self.clientWindow=ClientWindow(self)
        
 #____________________________________________ getter

    def getAllRequests(self):
        """
        return a list of all requests.
        """
        return self.client.getAllRequests()
    
    def getMyRequests(self):
        """
        return  list of client's requests.
        """
        return self.client.getMyRequests()
    
    
    def getRequestSubjects(self) -> list[str]:
        """
        returns list of available subjects.
        """
        return self.client.getRequestSubjects()
        
    def getRequestStatus(self) -> list[str]:
        """
        returns list of available status.
        """
        return self.client.getRequestStatus()
    
    def getMessages(self) -> list[Message]:
        """
        returns list of employee's Messages.
        """
        return self.client.getMessages()
    
    def getAnsweringSurveys(self)-> list:
        """
        returns list of answering surveys .\n
        [Survey, bool]
        """
        return self.client.getAnsweringSurveys()
    
    def getViewingSurveys(self)-> list[Survey]:
        """
        returns list of viewing surveys .
        """
        return self.client.getViewingSurveys()
    
        
 #____________________________________________ other
 
    def sendRequestMessage(self, request: Request, content: str):
        """
        gets a Request object and a text, then creates a RequestMessage.\n
        sends message to requester and respondent.
        """
        self.client.sendRequestMessage(request, content)
        
        
    def answerSurvey(self, survey: Survey, answer:str):
        """
        gets a Survey obejct and answer, then adds answer and username to survey.
        """
        self.client.answerSurvey(survey, answer)
        
        
    def createRequest(self, subject:str , content: str):
        self.client.createRequest(subject, content)
        
        
    def setResponseRate(self, request: Request, rating: int):
        """
        gets a request and rating and set it for the request
        """
        self.client.rateResponse(request= request, rating= int(rating))
        
 

    
    
    
        


if __name__ == "__main__":
    

    # app loop
    
    while True:
        controller=Controller()
        loginWindow=LoginWindow(controller=controller)
        
        
        
    
    # add manager part: username = aaa, password= aaa
    
    
    # salt = bcrypt.gensalt()
    # tempPass="aaa"
    # tempPass=tempPass.encode('utf-8')
    # tempPass=bcrypt.hashpw(tempPass, salt)
    # user1=Manager("aaa", tempPass)
    # SystemManager.addUser(user1)  
    
    
    
    
    
    
    
    
    
    