####  E-COM
##### This is an application that allow customers to sign up, sign in, view products and purchase products using LIpa na MPESA, Both the Frontend and Backend will be incorporated. The Application is inspired by Online Shopping that are on the rise, such as Jumia, Kilimall etc.
##### This is the Guide in Building the Full Application. 
### Requirements
#### 1. XAMPP - MySQL
#### 2. Visual Studio Code.

#### Part 1
#### Step 1 -  Creating a Database.
#####  Start Xampp and Type localhost/phpmyadmin.
Create a Database(If you do not have one) named **YourClassNameDB** then Click on Create

![screen1](https://user-images.githubusercontent.com/66998462/221429407-c13dfaab-738a-4cb7-b792-5e416bf62580.png)


#### Step 2 -  Creating a Table.
##### Create a table named **products** with 6 Columns, See below
![image](https://user-images.githubusercontent.com/66998462/221430059-663a7e50-b597-4943-94b9-e0eb8af7e78c.png)

![image](https://user-images.githubusercontent.com/66998462/221430082-6702889c-7060-4e13-a969-0845a7e3cbc9.png)


After specifying the table name and columns click on **Create/Go**
Below screen displays, please Enter the column names, Type and Length. Click on Save at the bottom.
![image](https://user-images.githubusercontent.com/66998462/221430207-b53a3226-00ac-4c78-9d19-c192692d776b.png)

Your table is now Created. 

![image](https://user-images.githubusercontent.com/66998462/221430478-86ba8cec-3a51-4e73-930b-552d6479f7ad.png)
Please Note that product_id is set to Primary Key and Auto Increment, Please Refer SQL Book 4 Page 15, 16 on How to set.
http://coding.co.ke/notes/SQL%20Book4.pdf


Now its time to insert some products in our newly create table **products**
Click on SQL and write the query as shown and Click **Go**.
![image](https://user-images.githubusercontent.com/66998462/221430857-39b4df9b-0495-4dd8-ae4a-17617f0f283c.png)


**Query.**
```   
INSERT INTO `products`(`product_name`, `product_desc`, `product_cost`, `product_category`, `product_image_name`) VALUES ('Infinix Hot 13','This is a nice phone for your personal activities','10000','Smartphone','infinix13.jpeg')
```

NB: 
   1 . Please Note that product_id was not inserted as it was an Auto Increment. 
   2 . Please Note that product_image_name is the only the image name that is entered. The image itself wil be Placed in a folder later in this Guide. 

Click on Browse and see the product you just inserted.
![image](https://user-images.githubusercontent.com/66998462/221431098-e51b6c4d-a938-4fdb-ba0c-0e586f6e6bbe.png)

Works?  Similarly Please insert more products using below Query.
```   
INSERT INTO `products`(`product_name`, `product_desc`, `product_cost`, `product_category`, `product_image_name`) VALUES ('Infinix Hot 13','This is a nice phone for your personal activities','10000','Smartphone','infinix13.jpeg')
```

### Step 3
### Introduction Notes
https://coding.co.ke/notes/Flask/Flask_Notes_Introduction.pdf  <br/> <br/>
https://coding.co.ke/notes/Flask/Flask_Routing.pdf

### Flask Application
Create a New Folder named YourClassFlask.
Open this Folder in Your VS Code.
![image](https://user-images.githubusercontent.com/66998462/221795955-f3bf3fef-4f3d-4f62-be89-23cc0f8c6005.png)

Inside YourClassFlask Folder, Create;
1. 1 File named app.py     
2. 2 Folders named templates and static

Your Folder/Files Structure should look as below;
![image](https://user-images.githubusercontent.com/66998462/221796643-7586f54f-f35e-4c0a-a91d-423340e977e3.png)


####Then Download more Files from http://coding.co.ke/notes/files.zip
Extract It and Paste it in Your **static** Folder

In below screen is the Folder/Files structure once (files Folder) is pasted in Static Folder
![image](https://user-images.githubusercontent.com/66998462/221841002-83f198a9-f441-4b84-97cc-8a827d88781a.png)

You are now done with Folder and Files setup. Happy Coding!

### Step 4
Next add below Code to **app.py** File
![image](https://user-images.githubusercontent.com/66998462/221838299-7f08d13d-5671-470b-90f0-906f0dc86a8c.png)

Explantion.
Line 1: Imports Flask Framework Library which allows use to create web applications using Python. <br />
Line 3: Create a Flask Application(Main App)<br />
Line 5:  ```  @app.route('/hello') ```  Create a route that is accessed Via a web browser.<br />
Line 6: Create a Function attached to above route, This function creates the functionality for /hello route. In this case it prints "Hello SokoGarden".<br /><br />
Line 10. Run App.  <br />
```  
    if __name__ == '__main__':
          app.run()
```

Above code  What does the if __name__ == “__main__”: do? Before executing code, Python interpreter reads source file and define few special variables/global variables. <br /> If the python interpreter is running that module (the source file) as the main program, it sets the special __name__ variable to have a value “__main__”.   <br />Then the app can now be Run.

Right click inside app.py and select **Run Python File in Terminal.**
Check the console output it given a Link http://127.0.0.1:5000 where your web application is now Hosted Locally on your computer.

![image](https://user-images.githubusercontent.com/66998462/221841991-2a1f6435-53f4-4e52-ba67-bbab7159b75c.png)

Now to run your web application on the browser. Enter  http://127.0.0.1:5000/hello  on Your browser address bar.
Your app now runs on the Web!.
![image](https://user-images.githubusercontent.com/66998462/221842464-68b55b91-2c32-448b-b6df-8999c6af67b8.png)

More Routes Practice, Try out these addition routes as you run from Browser.
![image](https://user-images.githubusercontent.com/66998462/221869494-8e706e45-c578-4f03-a50f-53e88633148e.png)


### Step 5
Creating Templates.
Before creating templates create a Default root in **app.py** as shown <br />
```
# Default Home route
@app.route('/')
def home():
    return render_template('home.html')
```

in this route it returns a HTML page named **home.html**
Your Final app.py code looks like below screen, Observe Line 14, 15, 16.
![image](https://user-images.githubusercontent.com/66998462/221869846-b34391ea-abd6-43e8-966c-4805140a2cd9.png)


Next we create the **home.html** page inside our **templates** Folder.
Click on templates Folder, add a new File named **home.html**.
Put below code inside.
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Home</title>
        <!--  CSS Supporting FIles  -->
        <link href="../static/files/css/bootstrap.min.css" rel="stylesheet">
        <link rel="stylesheet" href="../static/files/css/lightslider.css">
        <link rel="stylesheet" href="../static/files/css/style.css">
        <!--  JS  Supporting FIles    -->
        <script src="../static/files/js/bootstrap.bundle.min.js"></script>
        <script src="../static/files/js/jquery.js"></script>
        <script src="../static/files/js/lightslider.js"></script>
        <script src="../static/files/js/script.js"></script>
</head>
<body>
    <div class="container-fluid">
          <h1>Hello Soko Garden!</h1>
    </div>
</body>
</html>
```

Now Run your App.
Right click inside **app.py** and the select **Run Python file in Terminal**

Then on Any Browser type  http://127.0.0.1:5000/   on Address Bar.

Your SokoGarden Site is Up!
![image](https://user-images.githubusercontent.com/66998462/221870122-1b14dde5-d2a7-4acf-9515-0b235a7fb508.png)

### Step 6
In home.html Inside container- fluid Class Create a Navbar
Code.
```
<section class="row">
        <div class="col-md-12">
           <nav class="navbar navbar-expand-md navbar-light btn-light p-3">
                   <a href="#" class="navbar-brand">Soko <b class="text-success">Garden</b></a>
                   <button type="button" class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navbarCollapse">
                       <span class="navbar-toggler-icon"></span>
                  </button>

                   <div class="collapse navbar-collapse" id="navbarCollapse">
                        <div class="navbar-nav">
                             <a href="/" class="nav-item nav-link">Home</a>
                             <a href="/" class="nav-item nav-link">Blog</a>
                             <a href="/" class="nav-item nav-link">About US</a>
                        </div>
                       <div class="ms-auto">
                        <!--    TODO Logout-->
                       </div>

                   </div>
           </nav>
        </div>
   </section>
   ```
   
   Now Run your code and access  http://127.0.0.1:5000/ 
   The Navbar is Ready!
   ![image](https://user-images.githubusercontent.com/66998462/221883745-e1d407e4-0da0-4788-a3db-fbf6d286c7ff.png)

