import os
import sublime, sublime_plugin
import subprocess , os

class ComplieCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		#self.view.insert(edit, 0, "Hello, World!")
		

		k=self.view.window().extract_variables()
		#print (k)
		#print (k["project_path"])
		os.chdir(k["project_path"])
								
		path=os.listdir(os.getcwd())
						
		for i in path:
		    if(i.find(".uvproj")>0):
        		Project=i

		Command="UV4 -b {0} -o log.txt".format(Project)
						#print Command
		subprocess.call(Command,stdout=subprocess.PIPE,shell =False )


		self.view.window().open_file(k["project_path"]+"/log.txt")
		filea = open("log.txt","r")
		print (filea.read())
		#os.popen(Command)
						
		#allcontent = sublime.Region(0, self.view.size())
		#print (allcontent)
		#self.view.replace(edit, allcontent, 'Hello, world!')
		#print (self.view.substr(allcontent))

print ("saved")

