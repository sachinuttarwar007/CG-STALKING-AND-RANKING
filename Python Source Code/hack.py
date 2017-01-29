import urllib.request
import operator
from bs4 import BeautifulSoup
list_of_students=[]
for x in range(1,40):

	if(x<10):
		rollno='0'+str(x)
	else:
		rollno=str(x)
	print('Checking now for 16AR100'+rollno)
	link='https://erp.iitkgp.ernet.in/StudentPerformance/view_performance.jsp?rollno=16AR100'+rollno
	try:
		resulttext=urllib.request.urlopen(link).read()
	except:
		continue
	
	soup=BeautifulSoup(resulttext,'html.parser')
	jb=soup.find_all('td')

	for i in range(0,1000):
		try:
			elem=jb[i].string
		except:
			continue
		if(elem==None):
			continue
		else:
			if('Name' in elem):
				name_of_student =jb[i+1].string
				print(jb[i+1].string)
			if('Additional Credit Taken' in elem):
				cg_of_student =jb[i-1].string
				print(jb[i-1].string)
				dicta={'name':name_of_student,'cg':cg_of_student}
				list_of_students.append(dicta);
				break
list_of_students.sort(key=operator.itemgetter('cg'),reverse=True)
target = open('results.csv', 'w')
target.write('Rank,Name,CGPA\n')
for j in range(0,len(list_of_students)):
	this_dict=list_of_students[j]
	k=str(j+1)+','+this_dict['name']+','+this_dict['cg']+'\n'
	target.write(k)
target.close()


		

