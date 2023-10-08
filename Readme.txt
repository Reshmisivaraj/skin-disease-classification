set up your own flask env.
and install necessary lib. 

there will be some runtime errors while clicking on predict button on webpage.
which is happening due to lack of optimization of the trained model.
keep the image size =<200,200.

I have used the trained model(model.h5) which i got from github.
these seems to be some erros in you model causing some errors.
*****   there are still some errors like " index out of range " for some images you provided while using in this model ****
 

for running the application. open a project terminal in vscode or pycharm
execute: 
           " python app.py"
the site will be live on default: http://localhost:5000

i think modifying the trained model and making some necessary changes in the flask code ( app.py) will fix the issue.

contact me if any changes is needed in the UI. current one is simple image upload page or you can find any templates in codepen or other sites.

DONT MIND app_test.py ( i used it to test image upload detection)