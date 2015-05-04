import os
import sublime, sublime_plugin
import subprocess , os

class CompileCommand(sublime_plugin.TextCommand):
	def run(self,edit):

		k=self.view.window().extract_variables()
		os.chdir(k["project_path"])							
		path=os.listdir(os.getcwd())
						
		for i in path:
		    if(i.find(".uvproj")>0):
        		Project=i

		Command="UV4 -b {0} -o log.txt".format(Project)
		
		subprocess.call(Command,stdout=subprocess.PIPE,shell =False )

		self.view.window().open_file(k["project_path"]+"/log.txt")
		#filea = open("log.txt","r")
		#print (filea.read())
print ("saved")

