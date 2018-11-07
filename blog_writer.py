import os
import datetime

f_name = "coilgun.html"

#block = """\t\t\t\t<h3>11/07/18 - Burnt Out The Thyristor</h3>
#\t\t\t\t<p>Kinda sucks, but I still have 3 more</p>
#"""
#
#
#
#with open(f_name,"r") as f_old, open(f_name+"~","w") as f_new:
#    for line in f_old:
#        f_new.write(line)
#        if "<!-- INSERT -->" in line:
#            f_new.write(block)
#            
#os.remove(f_name)
#os.rename(f_name+"~",f_name)


class SiteEdit:
        
    ## Initialize with the site you want to edit.
    ## Functions will allow for editing.
    ## f - filename
    ##
    def __init__(self):
        self.filename = ""
        self.post_title = ""
        self.post_body = ""
        
    
    def main(self):
    
        choice = 0
        loop_flag = True

        print("Welcome to SiteEdit")
        print("Created by GRNCheetah")
        
        while (loop_flag):
            
            print("\nWhat would you like to do?")
            print("\t1) Add blog post")
            print("\t0) Exit\n")
            choice = input("--> ")
            
            if choice == "1":
                self.addPost()
            else:
                print("Goodbye!")
                loop_flag = False
                
    
    ## Will gather, format, and update the html document provided
    ## with a new blog post.
    def addPost(self):
        check = ""
        block = self.getPost()
        
        if self.filename == "coilgun.html":
            check = "<div id=sidebody>"
        
        if check != "":
            with open(self.filename,"r") as f_old, open(self.filename+"~","w") as f_new:
                for line in f_old:
                    f_new.write(line)
                    if check in line:
                        f_new.write(block)
            os.remove(self.filename)
            os.rename(self.filename+"~",self.filename)
            print("[+] File successfully updated!")
            
        else:
            print("[-]Filename was invalid")
        
    ## Do not call on it's own, it will be called
    ## from functions.
    ## self.post_title and self.post_body should have data.
    def formatPost(self):
        curr_time = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        return("\t\t\t<div class=blogpost>\n\t\t\t\t<h3>%s - %s</h3>\n\t\t\t\t<p>%s</p>\n\t\t\t</div>\n" % (curr_time, self.post_title, self.post_body))
        
    ## No point in calling on it's own atm, so just leave it
    ## to be used in addPost()
    ## Will return an html formatted piece of code with the body
    ## and title of the blog post.
    def getPost(self):
        self.filename = input("Full filename to change: ")
        # Make sure the file is good before failing later
        while (not(os.path.isfile(self.filename))):
            print("[-]Filename was invalid")
            self.filename = input("Try again: ")
        self.post_title = input("Enter post title: ")
        self.post_body = input("Enter post body: ")
        
        return(self.formatPost())
        
    
    
    
    
    
if __name__ == "__main__":
    site = SiteEdit()
    site.main()

    
    
    
    
    
    
    
    
    