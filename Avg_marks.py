# Students = [['Annie',85,90,75],
#             ['Bonnie',82,98,80],
#             ['Carol',83,86,91],
#             ['Doris',89,90,76]
# ]
#
# Each_test_total  = []
#
# num_tests = len(Students[0])-1
# Num_students = len(Students)
#
# for test_index in range(num_tests):
#     Each_test_total.append(0)
# print(Each_test_total)
# Each_test_average =[]
#
# for students_index in range(Num_students):
#     for test_index in range(num_tests):
#         Each_test_total[test_index]+=Students[students_index][test_index+1]
# print(Each_test_total)
#
# for test_index in range(num_tests):
#     Each_test_average.append(Each_test_total[test_index] / len(Students))
# print(Each_test_average)
#
# for test_index in range(num_tests):
#     print("The average test"+str(test_index+1)+' is '+str(Each_test_average[test_index])

# Data = [['Amarnath',35,75,45,84,91],
#         ['Chintu',85,74,95,65,48],
#         ['Love',45,90,75,65,85],
#         ['Hero',55,45,74,65,35],
#         ['Mine',25,35,45,50,51]]
#
# total = len(Data)
# Test = len(Data[0])-1
# Result = []
# for x in range(total):
#     Result.append(x)
# for i in range(total):
#     for j in range(Test):
#         Result[i]+=Data[i][j+1]
# print(Result)
# for x in range(len(Result)):
#     Result.append(round(Result[x]/len(Data),2))
# print(Result)




# Votes   = ["Boby",'Carle','Boby','Rahul','Raja','Boby','Raja','Boby','Anand','Anand','Classi','Classi','Raja',"Hero",'Rahul','Classi']
# Canditate = []
# votes = []
#
# for dat in Votes:
#     if dat not in Canditate:
#         Canditate.append(dat)
#
#     else:
#         Canditate_index = Canditate.index(dat)
#         print(Canditate_index)
#         votes[Canditate_index] = votes[Canditate_index]+1
#
# Max = 0
# Max_can = []
# for i in range(len(votes)):
#     if votes[i]>Max:
#         Max_can=votes[i]
#         candidate = Canditate[i]
#         Max_can.append(candidate)
#     elif votes[i]==Max:
#         candidate = Canditate[i]
#         Max_can.append((candidate))
# print("Highest votes goes to :")
# print(Max_can,sep='\n')
# print("Each person has "+str(Max_can)+'Votes')
#