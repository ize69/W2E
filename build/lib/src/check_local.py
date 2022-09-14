
#gracies hours used for testing the time handeling functionality 
from asyncio.windows_events import NULL
from datetime import datetime

testData = ["Gracie's", 0, '7:30am', '10:00am', '11:00am', '4:30pm', '4:30pm', '8:00pm', 0, 0, 0, 0]
def get_hours(dataSet):
    DataContainer = dataSet
    print(dataSet[0]) 
    #loop throug posible hours 
    k=0
    for i in dataSet:
        #checks if collen is present indecating value is a time
        if ":" in str(i):
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
    print(DataContainer)
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
def check_status(testData):
    return see_if_open(get_hours(testData))
    
