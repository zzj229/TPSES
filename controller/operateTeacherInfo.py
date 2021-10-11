from model.readAllTeacherInfo import readALLTeacherInfo,getTeacherInfo
import os

class operateTeacherInfo:
    def __init__(self):
        self.list=[]
        #self.id=0
    def getTeacherInfo(self):
        self.list=readALLTeacherInfo()
        specTeacherInfo=[]
        lspecTeacherInfo=[]

        for i in range(len(self.list)):
            specTeacherInfo.append(self.list[i].get('id'))
            specTeacherInfo.append(self.list[i].get('name'))
            specTeacherInfo.append(self.list[i].get('college'))
            specTeacherInfo.append(self.list[i].get('title'))
            specTeacherInfo.append(self.list[i].get('performance'))
            specTeacherInfo.append(self.list[i].get('time'))
            lspecTeacherInfo.append(specTeacherInfo)
            specTeacherInfo=[]

        return lspecTeacherInfo
# getTeacherInfo()返回一个[[]],每一个小列表装着四个信息,id,name,college,title

    def getTeacherInfoDict(self,id):
        fileList=os.listdir('resources/jsons')
        dict={}
        for item in fileList:
            if id+'.json'==item:
                dict=getTeacherInfo(id)
        return dict

    def getTeacherIDList(self):
        fileList=os.listdir('resources/jsons')
        list=[]
        for item in fileList:
            list.append(item.split('.',1)[0])
        return list

    def searchTeaherInfo(self,keyword):
        teachers=self.list
        findedTeacher=[]
        searchedTeacherData=[]
        for i in range(len(teachers)):
            if keyword == teachers[i].get('id') or keyword == teachers[i].get('name'):
                findedTeacher.append(teachers[i])   #findedteacher中的元素还是一个字典
        for i in range(len(findedTeacher)):    #将一个字典中的元素全部放在一个新列表中
            tempArray=[]
            tempArray.append(findedTeacher[i].get('id'))
            tempArray.append(findedTeacher[i].get('name'))
            tempArray.append(findedTeacher[i].get('college'))
            tempArray.append(findedTeacher[i].get('title'))
            searchedTeacherData.append(tempArray)   #列表内部嵌套一个列表
        return searchedTeacherData

    def getTeacherByAttribute(self,dict,data):

        teachers = readALLTeacherInfo()
        finalTeacherList=[]
        print(dict)
        if dict['college']=='全部' and dict['title']=='全部':
            for item in teachers:
                teachersList = []
                teachersList.append(item['id'])
                teachersList.append(item['name'])
                teachersList.append(item['college'])
                teachersList.append(item['title'])
                finalTeacherList.append(teachersList)
            return finalTeacherList
        elif dict['college']=='全部':
            for item in teachers:
                if item['title']==dict['title']:
                    teachersList=[]
                    teachersList.append(item['id'])
                    teachersList.append(item['name'])
                    teachersList.append(item['college'])
                    teachersList.append(item['title'])
                    finalTeacherList.append(teachersList)
            return finalTeacherList
        elif dict['title']=='全部':
            for item in teachers:
                if item['college']==dict['college']:
                    teachersList=[]
                    teachersList.append(item['id'])
                    teachersList.append(item['name'])
                    teachersList.append(item['college'])
                    teachersList.append(item['title'])
                    finalTeacherList.append(teachersList)
            return finalTeacherList
        else:
            print('1')
            for item in teachers:
                if item['college']==dict['college'] and item['title']==dict['title']:
                    print('1')
                    teachersList = []
                    teachersList.append(item['id'])
                    teachersList.append(item['name'])
                    teachersList.append(item['college'])
                    teachersList.append(item['title'])
                    print(teachersList)
                    finalTeacherList.append(teachersList)
            return finalTeacherList









