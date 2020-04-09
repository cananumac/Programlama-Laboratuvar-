def get_words():
    my_list=[]
    f=open('input_hw_2.csv','r+')
    contents= f.readlines()
    #print(contents)
    for line in contents:
        #print(line)
        word= line.rsplit("-",2)
        my_list.append(word[1])     
    f.close()
    return my_list

def my_bubble_sort(my_list):
    n=len(my_list)
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if not (my_list[j]<my_list[j+1]):
                temp=my_list[j]
                my_list[j]=my_list[j+1]
                my_list[j+1]=temp
    return my_list

def my_frequency_with_list_tuples(list_1):
    frequency_list=[]
    for i in range(len(list_1)):
        s=False
        for j in range(len(frequency_list)):
            if(list_1[i]== frequency_list[j][0]):
                frequency_list[j][1]=frequency_list[j][1]+1
                s=True
        if(s==False):
            frequency_list.append([list_1[i],1])
    return frequency_list

my_list=get_words()
my_list_2=my_frequency_with_list_tuples(my_list)
my_bubble_sort(my_list_2)
print(my_list_2)
def get_numbers():
    my_list=[]
    n=len(my_list_2)
    for i in range(n):
        my_list.append(my_list_2[i][1])
    return my_list

def my_median(my_list):
    my_bubble_sort(my_list)
    #print(my_list)
    n=len(my_list)
    if n%2==1:
        middle=int(n/2)
        median=my_list[middle]
        print("Medyan: ",median)
    else:
        middle_1=my_list[int(n/2)]
        middle_2=my_list[int(n/2)-1]
        median=(middle_1+middle_2)/2
        print("Medyan: ",median)

def my_mean(my_list):
    s,t=0,0
    for item in my_list:
        s=s+1
        t=t+item
    mean_= t/s
    print("Ortalama: ",mean_)

my_list_3=get_numbers()
my_bubble_sort(my_list_3)
print(my_list_3)
my_median(my_list_3)
my_mean(my_list_3)
