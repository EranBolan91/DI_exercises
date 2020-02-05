
matrix ='''
        7 3
        Tsi
        h%x
        i #
        sM 
        $a 
        #t%
        ir!
        '''

list = matrix.split()

list1 = []
list2 = []
list3 = []

for index,value in enumerate(list):
        lengthChar = len(value)
        round = 0 #This round is for the lists, when i increment 'round' its for the else if to add chr to other list
        for ch in value:
            if ch.isalpha():
                if round == 0:
                    list1.append(ch)
                    round += 1
                elif round == 1:
                    list2.append(ch)
                    round += 1
                elif round == 2:
                    list3.append(ch)
                    round += 1
                else:
                    round +=1
            else:
                round +=1
print(list1)
print(list2)
print(list3)
theMetrix = "".join(list1 + list2 + list3)
print(theMetrix)

