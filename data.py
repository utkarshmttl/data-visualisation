from bs4 import BeautifulSoup
import urllib.request as ur
from datetime import date, timedelta
import re

d1 = date(2017, 1, 1)  # start date
d2 = date(2017, 12, 31)  # end date

delta = d2 - d1         # timedelta
print(delta)

for i in range(delta.days + 1):
    print((d1 + timedelta(days=i)).strftime("%Y%m%d"))
    link = "https://www.timeanddate.com/scripts/cityajax.php?n=india/new-delhi&mode=historic&hd="+(d1 + timedelta(days=i)).strftime("%Y%m%d")+"&month="+(d1 + timedelta(days=i)).strftime("%-m")+"&year=2017"
    f = ur.urlopen(link)
    html = f.read()
    soup = BeautifulSoup(html,"lxml")

    for elem in soup(text=re.compile(r'(°C|\d\d\.\d\d)')):
        print(elem.parent)

    # print(soup)
    print("done ",i)


# for i, link in enumerate(links):
# 	print(i)
# 	# if i <= 175: #mid script execution
# 	# 	continue
# 	json_object = {}
	# f = ur.urlopen(link)
	# html = f.read()
	# soup = BeautifulSoup(html,"lxml")
#
# 	# Removing repeats BEGIN
# 	explanations = soup.find_all(attrs={'class': 'explanation'})
# 	for explanation in explanations[1:]:
# 		if(explanation.contents == explanations[0].contents):
# 			print(explanation.content)
# 			print("*******YES DECOMPOSED************")
# 			print(explanations[0].content)
# 			explanation.decompose()
#
#
# 	# Removing repeats END
#
# 	json_object["question_id"] = int(soup.find(attrs={'class': 'identifier'}).contents[0][8:])
#
# 	# Changing images to base 64 BEGIN
# 	images = soup.find_all("img")
# 	if len(images) > 0:
# 		for image in images:
# 			image['src'] = "data:image/png;base64, " + get_as_base64("https://app.efficientlearning.com/pv5/v8/5/" + image.get('src')[6:])
#
# 	# Changing images to base 64 END
#
# 	# Changing MathML to base 64 BEGIN
# 	equations = soup.find_all("math")
# 	if len(equations) > 0:
# 		for equation in equations:
# 			toPngString = "<math>"
# 			for content in equation.contents:
# 				if content != '\n':
# 					toPngString = toPngString + str(content)
# 			toPngString = toPngString + "</math>"
# 			toPngString = toPngString.replace('\n','')
# 			result = subprocess.run(['node', 'mathjaxtest.js', toPngString], stdout=subprocess.PIPE)
#
# 			mathReplacement = '<img src="' + result.stdout.decode("utf-8") + '"></img>'
# 			mathReplacement = BeautifulSoup(mathReplacement, "lxml")
# 			equation.replaceWith(mathReplacement.img)
# 	# Changing MathML to base 64 END
#
# 	# print(soup.prettify())
#
# 	question_query = ""
# 	for content in soup.find(attrs={'class': 'query'}).contents:
# 		if content != '\n':
# 			question_query = question_query + str(content)
# 	json_object["query"] = question_query.replace("'","''")
#
# 	solution = ""
# 	for explain in soup.find_all(attrs={'class': 'explanation'}):
# 		for content in explain.contents:
# 			if content != '\n':
# 				solution = solution + str(content)
# 	json_object["solution"] = solution.replace("'","''")
#
# 	# print("********query*********")
# 	# print(json_object["query"])
#
# 	# print("********solution*********")
# 	# print(json_object["solution"])
# 	conn = sqlite3.connect('og.db')
# 	print('INSERT INTO or REPLACE questions (ID,query,solution) VALUES ('+ str(json_object["question_id"]) +', \''+str(json_object["query"])+'\', \'' + str(json_object["solution"]) +'\')')
# 	conn.execute('INSERT or REPLACE INTO questions (ID,query,solution) VALUES ('+ str(json_object["question_id"]) +', \''+str(json_object["query"])+'\', \'' + str(json_object["solution"]) +'\')')
# 	#conn.execute('INSERT INTO questions (ID,query,solution) VALUES ('+ str(json_object["question_id"]) +', '+str(json_object["query"])+', ' + str(json_object["solution"]) +')');
# 	conn.commit()
# 	conn.close()
# 	print("DONE ", i);
#
# 	print('\n')
