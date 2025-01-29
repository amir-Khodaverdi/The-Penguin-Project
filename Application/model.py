from pathlib import Path
import pickle
import bcrypt
from datetime import datetime

 

class DataHandler:
    def __init__(self):
        pass
    
    script_dir = Path(__file__).parent
    usersFilePath = script_dir / 'users.pkl'
    requestsFilePath = script_dir / 'requests.pkl'
    subjects_StatusFilePath = script_dir / 'subjects_Status.pkl'    # [[subjects],[status]]
    surveysFilePath = script_dir / 'surveys.pkl'


    @staticmethod
    def loadUsers() -> list["User"]:
        """
        returns list of Manager, Client and Employee objects from file.\n
        contains all users.\n
        returs empty list if file not exist.
        """
        try:
            with DataHandler.usersFilePath.open("rb") as file:
                loadedUsers = pickle.load(file)
            return loadedUsers
        except FileNotFoundError:
            # create file if not exist
            with DataHandler.usersFilePath.open("wb") as file: 
                pickle.dump([], file)
            return []

    @staticmethod
    def saveUsers(usersList):
        """
        saves list of users in the file.
        """
        with DataHandler.usersFilePath.open("wb") as file: 
            pickle.dump(usersList, file)
            
            

    @staticmethod
    def loadRequests()-> list["Request"]:
        
        """
        returns list of requests objects from file.\n
        return empty list if file not exist.
        """
        try:
            with DataHandler.requestsFilePath.open("rb") as file:
                loadedRequests = pickle.load(file)
            return loadedRequests
        except FileNotFoundError:
            # create file if not exist
            with DataHandler.requestsFilePath.open("wb") as file: 
                pickle.dump([], file)
            return []
    
    @staticmethod
    def saveRequests(requestsList):
        """
        saves list of requests in the file.
        """
        with DataHandler.requestsFilePath.open("wb") as file: 
            pickle.dump(requestsList, file)
            
            
            
            
            
    @staticmethod
    def loadSubjects_Status():
        """
        returns list of available subjects and status from file.\n
        return empty 2d list if file not exist.
        """
        try:
            with DataHandler.subjects_StatusFilePath.open("rb") as file:
                loadedSS = pickle.load(file)
            return loadedSS
        except FileNotFoundError:
            # create file if not exist
            with DataHandler.subjects_StatusFilePath.open("wb") as file: 
                pickle.dump([], file)
            return [[],[]]
    
    @staticmethod
    def saveSubjects_Status(aubject_StatusList):
        """
        saves list of available subjects and status in the file.
        """
        with DataHandler.subjects_StatusFilePath.open("wb") as file: 
            pickle.dump(aubject_StatusList, file)
    
    
    @staticmethod
    def loadSurveys():
        """
        returns list of surveys from file.\n
        return empty list if file not exist.
        """
        try:
            with DataHandler.surveysFilePath.open("rb") as file:
                loadedSurveys = pickle.load(file)
            return loadedSurveys
        except FileNotFoundError:
            # create file if not exist
            with DataHandler.surveysFilePath.open("wb") as file: 
                pickle.dump([], file)
            return []
    
    @staticmethod
    def saveSurveys(surveysList):
        """
        saves list of available subjects and status in the file.
        """
        with DataHandler.surveysFilePath.open("wb") as file: 
            pickle.dump(surveysList, file)
            
            
            
            
    
    
            
            
    

    
    
    
####################################################################################################################################################################################
class SystemManager:
    # usersList=DataHandler.loadUsers()
    # requestsList= DataHandler.loadRequests()
    # requestStatus=DataHandler.loadRequestStatus()
    # requestSubjects=DataHandler.loadRequestSubjects()
    def __init__(self):
        self.__usersList=DataHandler.loadUsers()
        self.__requestsList= DataHandler.loadRequests()
        
        salt = bcrypt.gensalt()
        
        # add a test user (manager)
        
        # tempPass="fff"
        # tempPass=tempPass.encode('utf-8')
        # tempPass=bcrypt.hashpw(tempPass, salt)
        # user1=User("test", tempPass, "manager", None)
        # self.__usersList.append(user1)
        
    
        
    
    def loginCheck(self, username, password):
        """
        checks username and password and returns user object if it's valid.\n
        returns false if not. 
        """
        for user in self.__usersList:
            if user.getUsername() == username:
                password = password.encode('utf-8')
                if bcrypt.checkpw(password, user.getHashPassword()):
                    return user
                
        return False 
    
    
 #____________________________________________ updating files

    @staticmethod
    def updateUsersFile(usersList: list):
        """
        updates the users file with given list.
        """
        DataHandler.saveUsers(usersList)
        
    @staticmethod
    def updateRequestsFile (requestsList: list):
        """
        updates the requests file with given list.
        """
        DataHandler.saveRequests(requestsList)
        
    @staticmethod
    def updateSubjects_StatusFile (subject_statusList: list):
        """
        updates the subject_status file with given list.  
        """
        DataHandler.saveSubjects_Status(subject_statusList)
        
    @staticmethod
    def updateSurveysFile (surveysList: list):
        """
        updates the surveys file with given list.
        """
        DataHandler.saveSurveys(surveysList)
        
    
    

       
 #____________________________________________ adding
 
    @staticmethod
    def addUser(user: "User"):
        """
        gets a user object and adds it to users file.
        """
        userList=DataHandler.loadUsers()
        userList.append(user)
        SystemManager.updateUsersFile(userList)
        
    @staticmethod
    def addRequest(request: "Request"):
        """
        gets a request object and adds it to requests file.
        """
        requestsList=DataHandler.loadRequests()
        requestsList.append(request)
        SystemManager.updateRequestsFile(requestsList)
        
       
    @staticmethod 
    def addSubject(newSubject: str):
        """
        gets a new subject and adds it to subject_status file.
        """
        subject_statusList=DataHandler.loadSubjects_Status()
        subject_statusList[0].append(newSubject)
        SystemManager.updateSubjects_StatusFile(subject_statusList)
        
    @staticmethod
    def addStatus(newStatus: str):
        """
        gets a new status and adds it to subject_status file.
        """
        subject_statusList=DataHandler.loadSubjects_Status()
        subject_statusList[1].append(newStatus)
        SystemManager.updateSubjects_StatusFile(subject_statusList)
        
        
    @staticmethod
    def addSurveys(survey: "Survey"):
        """
        gets a survey object and adds it to surveys file.
        """
        surveysList=DataHandler.loadSurveys()
        surveysList.append(survey)
        SystemManager.updateSurveysFile(surveysList)
        
        
 #____________________________________________ removing
 
    @staticmethod
    def removeUser(user: "User"):
        """
        gets a user object and removes it from users file.
        """
        usersList=DataHandler.loadUsers()
        for usr in usersList:
            if usr.getUsername()==user.getUsername():
                usersList.remove(usr)
        SystemManager.updateUsersFile(usersList)
        
        
    @staticmethod
    def removeRequest(request: "Request"):
        """
        gets a user object and removes it from requests file.
        """
        requestsList=DataHandler.loadRequests()
        for req in requestsList:
            if req.getRequestID()==request.getRequestID():
                requestsList.remove(req)
        SystemManager.updateRequestsFile(requestsList)
        
        
 #____________________________________________ getting
 
    @staticmethod
    def getUsers() -> list["User"]:
        """
        returns list of users.
        """
        return DataHandler.loadUsers()
    
    @staticmethod
    def getRequests() -> list["Request"]:
        """
        returns list of all requests.
        """
        return DataHandler.loadRequests()
    
    @staticmethod
    def getRequestSubjects() -> list[str]:
        """
        returns list of subjects.
        """
        return DataHandler.loadSubjects_Status()[0]
        
    @staticmethod
    def getRequestStatus() -> list[str]:
        """
        returns list of status.
        """
        return DataHandler.loadSubjects_Status()[1]
    
    @staticmethod
    def getSurveys() -> list["Survey"]:
        """
        returns list of surveys.
        """
        return DataHandler.loadSurveys()
    
    @staticmethod
    def getManager() -> "Manager":
        """
        returns manager object.
        """
        for user in SystemManager.getUsers():
            if user.getRole() == "manager":
                return user
            
    
    @staticmethod
    def getNewRequestID() -> int:
        """
        return a new request id for defining new request.
        """
        requestsList=SystemManager.getRequests()
        
        maximumID=100
        for req in requestsList:
            if req.getRequestID()>maximumID:
                maximumID= req.getRequestID()
                
        return (maximumID+1)
    
    @staticmethod
    def getEmployeeRequests(employee: "Employee")-> list["Request"]:
        """
        return list of employee's assigned requests.
        """
        requestList=SystemManager.getRequests()
        assignedRequestList=[]
        for request in requestList:
            if request.getRespondent():    # if request does not have a respondent
                if request.getRespondent().getUsername()==employee.getUsername():
                    assignedRequestList.append(request)
        return assignedRequestList
    
    @staticmethod
    def getClientRequests(client: "Client")-> list["Request"]:
        """
        return list of client's assigned requests.
        """
        requestList=SystemManager.getRequests()
        clientRequestList=[]
        for request in requestList:
            if request.getRequester().getUsername()==client.getUsername():
                clientRequestList.append(request)
        return clientRequestList
    

        
        
        

 #____________________________________________ changing
 
    @staticmethod
    def changeRole(user: "User", newRole: str):
        """
        gets a user object and a new role, then changes the role of user.\n
        all properties of the user like requests and message swill be deleted.
        """
        
        if newRole == "employee":   
            tempUser= Employee(user.getUsername(), user.getHashPassword())
        elif newRole == "client":
            tempUser= Client(user.getUsername(), user.getHashPassword())
            
        SystemManager.removeUser(user)
        SystemManager.addUser(tempUser)
        
    @staticmethod
    def updateUser(updatedUser: "User"):
        """
        gets a user object and updates the old object.
        """
        usersList= SystemManager.getUsers()
        i=0
        for user in usersList:
            if user.getUsername() == updatedUser.getUsername():
                usersList[i] = updatedUser
                SystemManager.updateUsersFile(usersList)
                return
            i+=1
            
    @staticmethod
    def updateRequest(updatedRequest: "Request"):
        """
        gets a request object and updates the old object.
        """
        requestsList= SystemManager.getRequests()
        i=0
        for req in requestsList:
            if req.getRequestID() == updatedRequest.getRequestID():
                requestsList[i] = updatedRequest
                SystemManager.updateRequestsFile(requestsList)
                return
            i+=1
            
    @staticmethod
    def updateSurvey(updatedSurvey: "Survey"):
        """
        gets a Survey object and updates the old object.
        """
        surveysList= SystemManager.getSurveys()
        i=0
        for surv in surveysList:
            if surv.getQuestion() == updatedSurvey.getQuestion():
                surveysList[i] = updatedSurvey
                SystemManager.updateSurveysFile(surveysList)
                return
            i+=1
                
        
        
        
        
                
    @staticmethod        
    def clearUsers():
        DataHandler.saveUsers([])
    
                    
    @staticmethod        
    def clearRequests():
        DataHandler.saveRequests([])
                
                
        
    

####################################################################################################################################################################################
class User:
    def __init__(self, username: str, hashPassword: str, role: str):
        self.__username= username
        self.__hashPassword= hashPassword
        self.role= role
        self.messages = [Message]
        self.answeringSurveys= []    # [Survey, bool]   first item of each element is survey and the second one is bool for answered(True if answered)
        # self.viewingSurveys= [Survey]
        
    
    
 
    
    
 #____________________________________________ setter
    def setRole(self, newRole):
        self.role= newRole
        
 #____________________________________________ getter
    def getUsername(self) -> str:
        return self.__username
    
    def getHashPassword(self) -> str:
        return self.__hashPassword
    
    def getRole(self) -> str:
        return self.role
    
    def getUsername(self) -> str:
        return self.__username
    
    def getHashPassword(self) -> str:
        return self.__hashPassword
    
    def getRole(self) -> str:
        return self.role
    
    def getMessages(self)-> list["Message"]:
        tempList = [i for i in self.messages if (type(i) is ManagerAnnouncement) or (type(i) is RequestMessage)]
        return tempList
    
    def getRequestSubjects(self) -> list[str]:
        """
        returns list of available subjects .
        """
        return SystemManager.getRequestSubjects()
    
    def getRequestStatus(self) -> list[str]:
        """
        returns list of available status .
        """
        return SystemManager.getRequestStatus()
    
    def getAnsweringSurveys(self):
        """
        returns list of answering surveys .\n
        [Survey, bool]
        """
        return self.answeringSurveys
    
    def getViewingSurveys(self)-> list["Survey"]:
        """
        returns list of viewing surveys .
        """
        SurveysList= SystemManager.getSurveys()
        viewingSurveysList=[]
        for surv in SurveysList:
            for usr in surv.getViewers():
                if self.getUsername()==usr.getUsername():
                    viewingSurveysList.append(surv)
                    
        return viewingSurveysList
        
 #____________________________________________ adding
    def addMessage(self, message: "Message"):
        """
        gets a message object and adds it to messages list.\n
        updates the user object in users file.
        """
        self.messages.append(message)
        SystemManager.updateUser(self)
        
    def addAnsweringSurveys(self, survey: "Survey"):
        """
        gets a survey object and adds it to answering surveys list.\n
        updates the user object in users file.
        """
        self.answeringSurveys.append([survey, False])
        SystemManager.updateUser(self)
        
    def addViewingSurveys(self, survey: "Survey"):
        """
        gets a survey object and adds it to viewing surveys list.\n
        updates the user object in users file.
        """
        self.viewingSurveys.append(survey)
        SystemManager.updateUser(self)
        
 #____________________________________________ others

    def sendRequestMessage(self, request: "Request", content: str):
        """
        gets a Request object and a text, then creates a RequestMessage.\n
        sends message to manager, respondent and requester.
        """
        newMessage= RequestMessage(content=content,sender= self, request= request)
    

    def answerSurvey(self, survey: "Survey", answer:str):
        """
        gets a Survey obejct and answer, then adds answer and username to survey.
        """
        survey.addAnswer(self.getUsername(), answer)
        for surv in self.answeringSurveys:
            if survey.getQuestion()==surv[0].getQuestion():
                surv[1]=True
        SystemManager.updateUser(self)
        
    
        
    
        
        
####################################################################################################################################################################################
class Manager(User):
    def __init__(self, username: str, hashPassword: str):
        super().__init__(username, hashPassword, "manager")
        
        
 #____________________________________________ getting
    def viewAllUsers(self) -> list[User]:
        """
        returns list of all users.
        """
        return SystemManager.getUsers()
    
    def viewAllRequests(self) -> list["Request"]:
        """
        returns list of all requests.
        """
        return SystemManager.getRequests()
    
    
    def getSurveys(self) -> list["Survey"]:
        """
        returns list of surves .
        """
        return SystemManager.getSurveys()
    
    
    
 #____________________________________________ adding
    def addUser(self, username: str, password: str, role:str):
        """
        gets a username, password and role and adds the User object.
        """
        salt = bcrypt.gensalt()
        password=password.encode('utf-8')
        hashPassword=bcrypt.hashpw(password, salt)
        newUser=None
        if role == "employee":
            newUser=Employee(username, hashPassword)
        else:
            newUser=Client(username, hashPassword)
            
        SystemManager.addUser(newUser)
        
    def addSubject(self,newSubject: str):
        """
        gets a new subject and adds to subjects.
        """
        SystemManager.addSubject(newSubject)
        
    def addStatus(self, newStatus: str):
        """
        gets a new status and adds to status.
        """
        SystemManager.addStatus(newStatus)
        
    
        
        
        
        
 #____________________________________________ removing
    def removeUser(self, user: User):
        """
        gets a User object and removes it.
        """
        SystemManager.removeUser(user)
        
    def removeRequest(self, request: "Request"):
        """
        gets a Request object and removes it from request file.
        """
        SystemManager.removeRequest(request)
        # client =request.getRequester()
        # client.removeRequest(request)
        # SystemManager.updateUser(client)
        # if request.getRespondent():
        #     employee=request.getRespondent()
        #     employee.removeAssignedRequest(request)
        #     SystemManager.updateUser(employee)
        
        
        
        
        
 #____________________________________________ changing
    def changeRole(self, user: User, newRole: str):
        """
        gets a User object and new role and changes role.
        """
        SystemManager.changeRole(user, newRole)
        
        
    def editRequest(self, request:"Request", subject: str, content: str, status: str, endDate):
        """
        gets a request object and  subejct, content, status and endDate, then edits the request attributes.
        """
        if subject != request.getSubject():
            request.setSubject(self, subject)
        if content != request.getContent():
            request.setContent(self, content)
        if status != request.getStatus():
            request.setStatus(self, status)
        if endDate != request.getEndDate():
            request.setEndDate(self, endDate)
        
        SystemManager.updateRequest(request)
        
        
        
        
        
 #____________________________________________ others
    def createSurvey(self, question: str, receivers: list[User], viewers: list[User]):
        """
        gets a question, receivers and viewers list and creates a new Survey and adds it to file.
        """
        newSurvey= Survey(question, receivers, viewers)
        SystemManager.addSurveys(newSurvey)
        
        
    def assignRequest(self, request: "Request", employee: "Employee"):
        """
        gets a request and employee object and assigns the request to the employee ./n
        updates employee and request objects in files.
        """
        request.setRespondent(self, employee)
        # employee.assignNewRequest(request)
        SystemManager.updateRequest(request)
        # SystemManager.updateUser(employee)
        
        
    def sendAnnouncement(self, content: str, receivers: list[User]):
        """
        gets an announcement content and creates an Announcement object.
        """
        newAnnouncement= ManagerAnnouncement(content, receivers)
        self.addMessage(newAnnouncement)
        
        
        
        
    
        
    

#################################################################################################################################################################################### 
class Employee(User):
    def __init__(self, username: str, hashPassword: str):
        super().__init__(username, hashPassword, "employee")
        
        # self.assignedRequestsList=[Request]
        
        
    def getAssignedRequests(self)-> list["Request"]:
        """
        return a list of employye's assigned requests from requests file.
        """
        return SystemManager.getEmployeeRequests(self)
    
    
    def getAllRequests(self)-> list["Request"]:
        """
        return a list of all requests from requests file.
        """
        return SystemManager.getRequests()
    
    
    
    
    
    def updateRequest(self, request: "Request", newStatus: str, newEndDate):
        """
        gets a request, new status and new end-date, then updates the request status.
        """
        if newStatus != request.getStatus():
            request.setStatus(self, newStatus)
        if newEndDate != request.getEndDate():
            request.setEndDate(self, newEndDate)
        SystemManager.updateRequest(request)
        
        

    
    


####################################################################################################################################################################################  
class Client(User):
    def __init__(self, username, hashPassword):
        super().__init__(username, hashPassword, "client")
        
        
    
 
    def createRequest(self, subject: str, content: str):
        """
        gets a subject and request content, then creaetes a request.
        """
        newRequest=Request(subject, content, self)
        SystemManager.addRequest(newRequest)
        return 
        
        
    def removeRequest(self, request: "Request"):
        """
        gets a request and removes it from client's  requests list.
        """
        for req in self.requestsList:
            if req.getRequestID() == request.getRequestID():
                self.requestsList.remove(req)
                return
            
            
    def getAllRequests(self)-> list["Request"]:
        """
        return a list of all requests from requests file.
        """
        return SystemManager.getRequests()
    
    
    def getMyRequests(self)-> list["Request"]:
        """
        return  list of client's requests.
        """
        return SystemManager.getClientRequests(self)
    
    def rateResponse(self, request: "Request", rating: int):
        """
        gets a request object and a number and rates the responding of the request.
        """
        request.setResponseRate(rating= rating)
        SystemManager.updateRequest(request)
        
        
        
        
        
####################################################################################################################################################################################  
class Request:
    def __init__(self, subject: str, content: str, requester: Client):
        self.requestID = SystemManager.getNewRequestID()
        self.subject = subject
        self.content = content
        self.status = "Assigning respondent"
        self.requester = requester
        self.respondent = None
        self.createdDate=datetime.now()
        self.endDate = None
        self.responseRate = None
        self.changesHistory = []
        

 #____________________________________________ setter       
 
 
    def setSubject(self, user: Manager, newSubject: str):
        """
        gets a manager object and new subject, then updates the subject./n
        adds the record to request changes history.
        """
        self.changesHistory.append(f"{user.getUsername()}({user.getRole()}) changed subject from {self.subject} to {newSubject}. [{datetime.now().strftime("%Y-%m-%d %H:%M")}]")
        self.subject= newSubject
    
    
    def setContent(self, user: Manager, newContent: str):
        """
        gets a manager object and new content, then updates the content./n
        adds the record to request changes history.
        """
        self.changesHistory.append(f"{user.getUsername()}({user.getRole()}) changed content from {self.content} to {newContent}. [{datetime.now().strftime("%Y-%m-%d %H:%M")}]")
        self.content= newContent
        
    def setStatus(self, user: Manager | Employee, newStatus: str):
        """
        gets a manager or employee object and new status, then updates the status./n
        adds the record to request changes history.
        """
        self.changesHistory.append(f"{user.getUsername()}({user.getRole()}) changed status from {self.status} to {newStatus}. [{datetime.now().strftime("%Y-%m-%d %H:%M")}]")
        self.status= newStatus

    def setEndDate(self, user: Manager, newEndDate: str):
        """
        gets a manager or employee object and new endDate, then updates the end-date./n
        adds the record to request changes history.
        """
        self.changesHistory.append(f"{user.getUsername()}({user.getRole()}) changed end-date from {self.endDate} to {newEndDate}. [{datetime.now().strftime("%Y-%m-%d %H:%M")}]")
        self.endDate= newEndDate
        
    def setRespondent(self, user: Manager, employee: Employee):
        """
        gets a manager and employee object, then assignes the respondent./n
        adds the record to request changes history.
        """
        self.changesHistory.append(f"{user.getUsername()}({user.getRole()}) assigned the request to {employee.getUsername()}. [{datetime.now().strftime("%Y-%m-%d %H:%M")}]")
        self.respondent= employee
        
    def setResponseRate(self, rating: int):
        """
        gets a rating and set it for the request
        """
        self.responseRate= rating
        
  
 #____________________________________________ getter

    def getRequestID(self):
        return self.requestID
    
    def getSubject(self):
        return self.subject
    
    def getContent(self):
        return self.content
    
    def getStatus(self):
        return self.status
    
    def getRequester(self):
        return self.requester
    
    def getRespondent(self):
        return self.respondent
    
    def getCreatedDate(self):
        return self.createdDate
    
    def getEndDate(self):
        return self.endDate
    
    def getChangesHistory(self):
        return self.changesHistory
    
    def getResponseRate(self):
        return self.responseRate
        
    
   
    
    
####################################################################################################################################################################################
class Message:
    def __init__(self, content: str, sender: User, receivers: list[User], messageType: str):
        """
        sends the message(self) to all receivers.
        """
        self.content= content
        self.sender= sender
        self.receiversList= receivers
        self.type= messageType
        
        
        
    def addReceiver(self, receiver: User):
        """
        gets a User and adds it to receivers list object.\n
        adds the message to the receiver object.
        """
        self.receiversList.append(receiver)
        receiver.addMessage(self)
        
    def getContent(self):
        return self.content
    
    def getSender(self):
        return self.sender
    
    def getType(self):
        return self.type
    
  
class RequestMessage(Message):
    def __init__(self, content: str, sender: User, request: Request):
        """
        sends this message(self) to manager, requester and respondent.
        """
        super().__init__(content= content,sender= sender,receivers= [SystemManager.getManager(), request.getRequester(), request.getRespondent()],messageType= "requestMessage" ) 
        self.request= request
        for user in self.receiversList:
            if user:   # if there is no respondent yet
                user.addMessage(self)
        
        
    def getRequest(self)-> Request:
        return self.request
        
        
class ManagerAnnouncement(Message):
    def __init__(self, content: str, receivers: list[User]):
        super().__init__(content, SystemManager.getManager(), receivers, "announcement")  
        for user in self.receiversList:
            if user:
                user.addMessage(self)



class Survey:
    def __init__(self, question: str, receivers: list[User], viewers: list[User]):
        """
        sends this survey(self) to users in receivers and viewers list.
        """
        self.question= question
        self.receivers= receivers
        self.viewers= viewers
        self.answers= []  # [ [username, answer], [username, answer] ]  
        
        
        for user in receivers:
            user.addAnsweringSurveys(self)
            
        
        
        
    def addAnswer(self, username: str, answer: str):
        self.answers.append([username, answer])
        SystemManager.updateSurvey(self)
        
        
    def getQuestion(self)-> str:
        return self.question
    
    def getAnswers(self)-> list:
        return self.answers
    
    def getViewers(self)-> list[User]:
        return self.viewers
        
    
 




        
if __name__ == "__main__":
    pass
    