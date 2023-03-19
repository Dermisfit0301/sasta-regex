#Sasta Regex
from flask import Flask,request,render_template
import re

sastaregex= Flask(__name__)

#===============================================================================================================



@sastaregex.route('/', methods=['GET','POST'])
def home_page():
    if request.method=='POST':
        target= request.form.get('Kisme dhundu bata?')
        regex=request.form.get('mujhe regular expression bata?')
        lst=re.findall(target,regex)
        print(lst)

    return render_template('index.html')
    


if __name__=='__main__':
    sastaregex.run()