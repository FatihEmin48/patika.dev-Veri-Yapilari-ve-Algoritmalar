#[22,27,16,2,18,6] -> Insertion Sort

#Yukarı verilen dizinin sort türüne göre aşamalarını yazınız.
#[16, 22, 27, 2, 18, 6]
#[2, 16, 22, 27, 18, 6]
#[2, 16, 18, 22, 27, 6]
#[2, 6, 16, 18, 22, 27]

#Big-O gösterimini yazınız.
#Time Complexity: Average case: Aradığımız sayının ortada olması,Worst case: Aradığımız sayının sonda olması, Best case: Aradığımız sayının dizinin en başında olması.
#Best case: n
#Average  case: n^2
#Worst case: n^2

#Dizi sıralandıktan sonra 18 sayısı hangi case kapsamına girer? Yazınız.


#[7,3,5,8,2,9,4,15,6] dizisinin Insertion Sort'a göre ilk 4 adımını yazınız.
#[3,7,5,8,2,9,4,15,6]
#[3,5,7,8,2,9,4,15,6]
#[3,5,7,8,2,9,4,15,6]
#[2,3,5,7,8,9,4,15,6]


def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
              
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1        
       
        array[j + 1] = key


nums = [7,3,5,8,2,9,4,15,6]
insertionSort(nums)
print(nums)