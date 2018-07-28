import os,requests

os.system("cls||clear")
print
print ("""
	|=============================|
	|      Coded By J0K3R00T      |
	|         Finder Shell        |
	|          27/07/2018         |
	|=============================|

	""")

url = raw_input('Url ==> ')
print
shell = ('c99.php' ,'gaza.php','wso.php' ,'shell.php' ,'andela.php' ,'mass.php','Angel.php','C100.php','b374k.php','Upload.php','Aspx.php','ASPXspy2.php','PHPJackal.php','1n73ction.php','Webadmin.php','Mysql.php','AluCa.php','R57.php','Pouya.php','Web.php','Zehir4.php','Za.php','x2300.php','Kacak.php','CWShel.php','Klasvayv.php','R00t.php','Saud.php','SyRiAn.php','Sosyete.php','Tryag.php','Ekin0.php',)

for x in shell:
	find = url + x
	r = requests.get(find)
	if r.status_code == 200:
		print "Shell Encontrada ==> " + find
	else:
		if r.status_code != 200:
			print "Shell Erro ==> " + find