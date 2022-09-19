
#gracies hours used for testing the time handeling functionality 
from asyncio.windows_events import NULL
from datetime import datetime
from operator import indexOf

def get_hours(dataSet):
    DataContainer = dataSet
    #print(dataSet[0]) 
    #loop throug posible hours 
    k=0
    for i in DataContainer:
        #checks if collen is present indecating value is a time
        if ":" in str(i):
            #removes the am/pm and the ":" to make the times in to intagers
            if "pm" in str(i):
                temp = i
                temp=(temp).replace(':','')
                temp=(temp).replace('pm','')
                temp=int(temp)+1200
                DataContainer[k]=temp
            if "am" in str(i):
                temp = i
                temp=(temp).replace(':','')
                temp=(temp).replace('am','')
                temp=int(temp)
                DataContainer[k]=temp
        k+=1
    #print(DataContainer)
    return DataContainer
def see_if_open(dataSet):
    #get the curent time
    now = datetime.now()
    current_time = now.strftime("%H%M")
    open = False
    k=0
    for i in dataSet:
        if 0 is not i and not (isinstance(i, str)):
            k+=1
            if k%2==1 and i<int(current_time) and i>int(dataSet[k]):
                    open=True                  
    return open
def check_meal(dataSet):   
    temp=get_hours(dataSet)
        #get the curent time
    now = datetime.now()
    current_time = now.strftime("%H%M")
    k=0
    j=0
    for i in temp:

        if 0 is not i and not (isinstance(i, str)):
            k+=1
            if k%2==1 and i<int(current_time) and i>int(temp[k]):
                index_of_hours = j
        j+=1 
    
    return index_of_hours
def check_status(testData):
    temp = get_hours(testData)
    return see_if_open(temp)
    