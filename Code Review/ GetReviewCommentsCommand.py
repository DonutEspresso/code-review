import os
import re
import sublime_plugin
import sublime
import subprocess
import time

SETTINGS_FILE = "Base File.sublime-settings"

class GetReviewCommentsCommand(sublime_plugin.WindowCommand):

    lines_per_comment = 7
    author = ''
    reviewer = ''

    def run(self):
        self.reset()
        view = self.window.active_view()
        settings = view.settings()
        filename = str(view.file_name().rsplit('/', 1)[1])
        comments = self.readFile(str(view.file_name()))
        self.outputComments(filename, comments)

    def reset(self):
        self.comments = []
        self.author = ''
        self.reviewer = ''

    def readFile(self, filename):
        comment = []
        comments = []
        isReading = False
        basePath = filename[0:filename.rfind("/")+1]

        with open(filename) as f:
            lines = f.readlines()

            for idx, line in enumerate(lines):

                if ("/*" in line or "//" in line or "/**"):
                    isReading = True
                elif ("*/" in line or "**/"):
                    isReading = False
                else:
                    isReading = False       


                if (isReading):
                    if ("@author" in line):
                        self.author = line.strip().rsplit(' ').pop()
                    if ("@reviewer" in line):
                        self.reviewer = line.strip().rsplit(' ').pop()
                
                    if ("REVIEW:" in line):
                        for x in range(0, self.lines_per_comment):
                            comment.append(str(idx+x) + "    " + lines[idx+x].strip())
                        comments.append(comment)
                        comment = []
        
        return comments


    def outputComments(self, filename, comments):
        #sublime.active_window().run_command("show_panel", {"panel": "console", "toggle": True})
        outputStr = ""
        outputStr += "//----------------------------------------------------------------------------------------------\n"
        outputStr += "//    Code Review: " + filename + "\n"
        outputStr += "//    " + str(len(comments)) + " review comments\n"
        outputStr += "//    \n"
        outputStr += "//    @author " + self.author + "\n"
        outputStr += "//    @reviewer " + self.reviewer + "\n"
        outputStr += "//----------------------------------------------------------------------------------------------"

        for comment in comments:
            outputStr += "\n\n\n"
            for line in comment:
                outputStr += line + "\n"


        #print(line.replace("\n", ""))
        newView = sublime.active_window().new_file()
        newView.set_name("CR: " + filename)        
        newEdit = newView.begin_edit()
        newView.insert(newEdit, 0, outputStr) 
        newView.end_edit(newEdit)            