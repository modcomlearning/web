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
Inside templates Folder create a File named **navbar.html**
Write this code inside navbar.html
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
   
   Next Inside templates Create a File named **carousel.html**
   Inside this File add below code to create a carousel - sliding image.
   ```
    <section class="row">
        <div class="col-md-12">
            <div id="myCarousel" class="carousel slide" data-bs-ride="carousel" data-pause="false">
                     <!-- Wrapper for carousel items -->
                    <div class="carousel-inner">
                        <div class="carousel-item active">
                            <img src="../static/files/slide1.jpg" class="d-block w-100" alt="Slide 1" height="400">
                            <div class="carousel-caption d-none d-md-block">
                                <h5>First slide label</h5>
                                <p>Some placeholder content for the first slide.</p>
                            </div>
                        </div>
                        <div class="carousel-item">
                            <img src="../static/files/slide2.jpg" class="d-block w-100" alt="Slide 2" height="400">
                            <div class="carousel-caption d-none d-md-block">
                                <h5>First slide label</h5>
                                <p>Some placeholder content for the first slide.</p>
                            </div>
                        </div>
                    </div>
                    <!-- Controls -->
                     <!-- Carousel controls -->
                    <a class="carousel-control-prev" href="#myCarousel" data-bs-slide="prev">
                        <span class="carousel-control-prev-icon"></span>
                    </a>
                    <a class="carousel-control-next" href="#myCarousel" data-bs-slide="next">
                        <span class="carousel-control-next-icon"></span>
                    </a>
            </div>
        </div>
   </section>
   ```
   
   
   Then in **home.html** file inside container-fluid write below code.
   
  
   ```
   <div class="container-fluid">
          {% include 'navbar.html' %}
          <br>
          {% include 'carousel.html' %}
    </div>
   ```
  
   Above code is using Jinja2 Templating Engine that helps html to include other Files i.e navbar.html and carousel.html
   
   Your Final Code for **home.html** looks Like below;
    
    
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
                {% include 'navbar.html' %}
                <br>
                {% include 'carousel.html' %}
          </div>
      </body>
      </html>
      ```

   Now Run your code and access  http://127.0.0.1:5000/ 
   The Navbar and Carousel is Ready!
   ![image](https://user-images.githubusercontent.com/66998462/222125335-4912a000-e175-4f81-ba17-9c08623a9d89.png)

   
   ## Step 7
   In this section we will learn Fetching data From MySQL.
   Before proceeding You need the following <br/> 
   1. Your XAMPP Server Must be running
   2. You have database and
   3. You have a products table with a number of products.

   If you do not have above Please **Refer Step 2 in this document**
   
   1. Fetching Records.
   In ** app.py** check the home route, If not Present please create It.
   ```
      # Default Home route
      @app.route('/')
      def home():
          return render_template('home.html')
   
   ```
   
   2. Update the home route to fetch data from the database.
   First install pymysql using **pip3 install pymysql**.
   Below is the improved home route. <br/><br/>
   
   
   # Default Home route
   ```
   import pymysql
   @app.route('/')
   def home():
       # Establish a database connection
       connection = pymysql.connect(host='localhost', user='root', password='',
                                    database='DemoClassDB')
      ** # SQL 1  - Select Products by Smartphone Category**
       sqlSmartphone = "SELECT * FROM products where product_category = 'Smartphone'"
       
       **# Cursor - Used to run/execute above SQL**
       cursorSmartphone = connection.cursor()
       
      ** # Execute SQL**
       cursorSmartphone.execute(sqlSmartphone)
       
      ** # Fetch Rows**
       smartphones = cursorSmartphone.fetchall()

       **# TODO SQL 2  - Smartphones**
       
       # Return smartphones to **home.html**
       return render_template('home.html', smartphones=smartphones)
 
 ```
       
   ## Step 8
   In this section we now update **home.html.**
   At the moment your **home.html** looks like below;
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
          {% include 'navbar.html' %}
          <br>
          {% include 'carousel.html' %}
          
          <!-- CODE HERE -->
          
    </div>
</body>
</html>
```

Below we update above **home.html**,  Update code is added on Line 356. Below is the code snippet to be added.

   ```
    <br>
     <section class="slider p-4">
    <ul  class="cs-hidden autoWidth">
    
     {% for smartphone in smartphones %}
       <li>
         <div class="box">
             <div class="slide-img">
             <img src="../static/images/{{ smartphone[5]}}"  width="50" height="50">
             <div class="overlay">
                 <a href="/single_item/{{ smartphone[0]}}" class="buy-btn">Buy Now</a>
             </div>
             </div>
             <div class="detail-box">
                 {{smartphone[1]}}<br>
                 <b class="text-warning">KES {{smartphone[3]}}</b>
             </div>
             </div>
         </li>
        {% endfor %}
       </ul>
   </section>
  ```
  
  
  
  Your Final **home.html** should look like below code;
  
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
          {% include 'navbar.html' %}
          <br>
          {% include 'carousel.html' %}
          <br>
           <section class="slider p-4">
	    <ul  class="cs-hidden autoWidth">
	        <!-- Below we loop through each smartphone retrieved. -->
		{% for smartphone in smartphones %}
		  <li>
		    <div class="box">
			<div class="slide-img">
			<!-- Below we place the image in the image tag -->
			<img src="../static/photos/{{ smartphone[5]}}"  width="50" height="50">
			<div class="overlay">
			    <!-- This is a Link to Buy Now, The route on href will be used Later in Next Steps -->
			    <a href="/single_item/{{ smartphone[0]}}" class="buy-btn">Buy Now</a>
			</div>
			</div>
			<div class="detail-box">
			    <!-- Below we provide the product name and Cost. -->
			    {{smartphone[1]}}<br>
			    <b class="text-warning">KES {{smartphone[3]}}</b>
			</div>
			</div>
		    </li>
		    <!-- End for Loop -->
		   {% endfor %}
          </ul>
        </section>
    </div>
</body>
</html>
```



Finally we need to upload the images to static Folder, FInd the images on below link<br/>
http://coding.co.ke/files/    Extract photos.zip and Paste the photos Folder in your static Folder <br/>
NB: The images names must be the same withs once inserted in the database on **Step 2 Earlier **

<br/>
Now Run your App. <br/>
Right click inside **app.py** and the select **Run Python file in Terminal** <br/>
Now access  http://127.0.0.1:5000/ From your browser. <br/>


Below is the Output
![image](https://user-images.githubusercontent.com/66998462/222487250-949b654f-ae05-4a09-a3d0-52da2ae3a239.png)



## Step 9
In this step we will create a Page which displays when a product is clicked from Home Page.  From Home.html, each product had an Overlay and a Buy Button, It looked something like, Please refer your home.html. Please check Step 8.
```
<div class="overlay">
    <!-- This is a Link to Buy Now, The route on href will be used Later in Next Steps -->
    <a href="/single_item/{{ smartphone[0]}}" class="buy-btn">Buy Now</a>
</div>
```
We need to provide a route in href = "", <a href="/single/{{ smartphone[0]}}" class="buy-btn">Buy Now</a>, passing along the product ID. Here i use 
{{ smartphone[0]}} since i used it in Step 8.  This means when you click on Buy Now it Navigates to /single route.


Below we create a route named **/single**. Open **app.py** and create below route.
```
# Get Single Item, Note this route has an product_id, It displays a product based on product_id
@app.route('/single/<product_id>')
def single(product_id):
    # Establish a dbase connection
    connection = pymysql.connect(host='localhost', user='root', password='',
                                 database='DemoClassDB')
				 
    # Create SQL  - %s is a placeholder, which will take the actual ID during Query Execution.
    sql1 = "SELECT * FROM products WHERE product_id = %s"

    # Cursor - Used to run/execute above SQL
    cursor1 = connection.cursor()

    # Execute SQL providing product_id - NB: Sql had a placeholder in the Where clause thats why we provide the product_id
    cursor1.execute(sql1, (product_id))

    # Get the product retrieved 
    product = cursor1.fetchone()
    
    # Return the product to single.html
    return render_template('single.html', product=product)
 ```
 
 
Then in **templates Folder** Create a Page named single.html and place Below Code.
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Products</title>
    <!-- Link Bootstrap CSS and JS -->
     <link href="../static/files/css/bootstrap.min.css" rel="stylesheet">
      <script src="../static/files/js/bootstrap.bundle.min.js"></script>
</head>
<body>
     <div class="container-fluid">
     <!-- Include Navbar -->
         {% include 'navbar.html' %}
          <section class="row">
               <div class="col-md-4">
	       <!-- Product variable holds the Current Product , This comes from /single route in app.py  -->
                      <img src="../static/photos/{{product[5]}}" alt="" width="300" height="300"
                      class="img-thumbnail shadow p-4"><br><br>
                      <h3>{{ product[1] }}</h3>
               </div>

              <div class="col-md-8">
                     <p class="text-muted">{{ product[2] }}</p>
                     <h4>KES {{ product[3] }}</h4>
                     <b class="text-danger">Category: {{ product[4] }}</b> <br><br>
              </div>
     </div>
</body>
</html>
```

<br/>
Now Run your App. <br/>
Right click inside **app.py** and the select **Run Python file in Terminal** <br/>
Now access  http://127.0.0.1:5000/ From your browser. <br/>

Output
![image](https://user-images.githubusercontent.com/66998462/223324265-0ff6948a-dcfb-47a1-83c3-7f48e72de067.png)

When You Click on One Product  - Buy Now
![image](https://user-images.githubusercontent.com/66998462/223324142-4ba6f95a-b149-4abe-b0fa-af1c6821f674.png)


## Step 10, This is an Optional Step But It can be done to provide More similar Product to the product displayed in Image above.
We Update the code to also select similar products based on Current product Category.
Update your route to retrieve similar products your **/single** route Looks like below
```
# Get Single Item
@app.route('/single/<product_id>')
def single(product_id):
    # Establish a dbase connection
    connection = pymysql.connect(host='localhost', user='root', password='',
                                 database='DemoClassDB')
    # SQL  - %s is a placeholder
    sql1 = "SELECT * FROM products WHERE product_id = %s"

    # Cursor - Used to run/execute above SQL
    cursor1 = connection.cursor()

    # Execute SQL providing product_id - NB: sql had a placeholder
    cursor1.execute(sql1, (product_id))

    # Get the product retrieved, Please this is one Product. 
    product = cursor1.fetchone()


    # At this Point, we have a product, We can retrieve product category like
    category = product[4]  # Category is at colm 4

    # We now query to Find Others Product in this category, We LImit to only 4
    # ADD THIS
    sql2 = "select * from products where product_category = %s LIMIT 4"
    cursor2 = connection.cursor()
    cursor2.execute(sql2, (category))
    similar = cursor2.fetchall()
    # Now we have similar products

    # We now return the Product and similar Products 
    return render_template('single.html', product=product, similar = similar)
   ```
   
Your **single.html** should be updated to Look as below. We Bind similar products
   
   ```
   <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Products</title>
     <link href="../static/files/css/bootstrap.min.css" rel="stylesheet">
      <script src="../static/files/js/bootstrap.bundle.min.js"></script>
</head>
<body>
     <div class="container-fluid">
         {% include 'navbar.html' %}
          <section class="row">
               <div class="col-md-4">
                      <img src="../static/photos/{{product[5]}}" alt="" width="300" height="300"
                      class="img-thumbnail shadow p-4"><br><br>
                      <h3>{{ product[1] }}</h3>
               </div>

              <div class="col-md-8">
                     <p class="text-muted">{{ product[2] }}</p>
                     <h4>KES {{ product[3] }}</h4>
                     <b class="text-danger">Category: {{ product[4] }}</b> <br><br>
              </div>
              </section>
              <br><br>
	      
              <!-- ADD THIS CODE  -->
              <h4>More Like This</h4>
               <section class="row">
              {%  for item in similar  %}
                   <div class="col-md-3">
                       <img src="../static/photos/{{item[5]}}" alt="" width="200" height="200">
                       <br>
                       <b>{{item[1]}}</b> <br>
                       <p class="text-muted">KES {{item[3]}}</p>
            
        
                       <a href="/single/{{item[0]}}" class="btn btn-warning">Buy Now</a>
                       <br><br>
                   </div>
             {% endfor %}
       </section>
     </div>
</body>
</html>
```

<br/>
Now Run your App. <br/>
Right click inside **app.py** and the select **Run Python file in Terminal** <br/>
Now access  http://127.0.0.1:5000/ From your browser. <br/>

When your Click on One Product From home.html, You get below screen.  NB: Products used here are Dummy Product they dod not represent the Correct Categories
![image](https://user-images.githubusercontent.com/66998462/223324785-08746180-0f1c-4ff8-a6fc-f39408f84a7b.png)



## Step 11
In this Step we will create a sign up Page, this will be sued to Register users to Our Database.
See below on how a User Sign Up and how we will do it.
![image](https://user-images.githubusercontent.com/66998462/223623379-4a679033-7e97-4411-92ae-3539c42ed8f4.png)

1. Start Xampp and access your Database From http://localhost/phpmyadmin
Click on your database and create below table
![image](https://user-images.githubusercontent.com/66998462/223620535-e806fcfa-9ba5-437d-8643-db2f880529ce.png)


Please Refer **Step 2** on how to create a table, Once created it will look something like.
![image](https://user-images.githubusercontent.com/66998462/223620834-5be1a5df-d242-42ab-a68e-3d9caf17a39e.png)

This Table will be used to store our users. NB: Please observe the table name and column names and Note them.
![image](https://user-images.githubusercontent.com/66998462/223624064-8f6303a3-ccf4-4f9e-b466-278ab20868c4.png)


2. We create a tamplate named **signup.html**  Create this File in Your templates Folder.
Put below code inside.
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sign Up</title>
  <link href="../static/files/css/bootstrap.min.css" rel="stylesheet">
    <script src="../static/files/js/bootstrap.bundle.min.js"></script>
</head>
<body>
     <div class="container">
         {% include 'navbar.html' %}
         <section class="row">
             <div class="col-md-4">
                  <h3>Create Account</h3>
                  <span style="color:green;">{{success}}</span>
                  <span style="color:red;">{{error}}</span>
                  <form action="/signup" method="post">
                      <input type="text" name="username" placeholder="Your Username"
                      class="form-control"> <br>

                      <input type="email" name="email" placeholder="Your Email"
                      class="form-control"> <br>

                      <input type="tel" name="phone" placeholder="Your Phone"
                      class="form-control"> <br>

                      <input type="password" name="password1" placeholder="Your Password"
                      class="form-control"> <br>

                      <input type="password" name="password2" placeholder="Confirm Password"
                      class="form-control"> <br><br>

                      <input type="submit" value="Sign Up" class="btn btn-info">
                  </form>
                 <br>
                 <a href="/signin"> Already Have an Account?, Login </a>
             </div>
         </section>
     </div>
</body>
</html>
```

Above code has a table with the fields as per our users table. Observe the input names are same as the ones in the table(CASE SENSITIVE) i.e  username, password, email, phone.
NB: password2 is not in our table it will only be used to confirm if passwords are matching.

Check <form action="/signup" method="post">   this line it points to a route named /signup we will create this route in Python to help receive the data once the form is Posted.
<br/><br/>

3. Next we create a  **/signup**  route in our **app.py**
Put below code.
```
@app.route('/signup', methods=['POST', 'GET'])
def signup():
    # Check if form was posted by user
    if request.method == 'POST':
            # Receive what was posted by user including username, password1,password2 email, phone
            username = request.form['username']
            email = request.form['email']
            phone = request.form['phone']
            password1 = request.form['password1']
            password2 = request.form['password2']
	    
            # check if any of the password is less than eight x-ters and notify the user to put a password more that 8 -xters  
            if len(password1) < 8:
                return render_template('signup.html', error='Password must more than 8 xters')
		
            # Check if the 2 passwords are matching, if not notify the user to match them up.		
            elif password1 != password2:
                return render_template('signup.html', error='Password Do Not Match')
            else:
	        # Now we can save username, password, email, phone into our users table
		# Make a connection to database
                connection = pymysql.connect(host='localhost', user='root', password='',
                                             database='DemoClassDB')
		# Create an Insert SQL, Note the SQL has 4 placeholders, Real values to be provided later			     
                sql = ''' 
                     insert into users(username, password, phone, email) 
                     values(%s, %s, %s, %s)
                 '''
		# Create a cursor to be used in Executing our SQL 
                cursor = connection.cursor()
		# Execute SQL, providing the real values to replace our placeholders 
                cursor.execute(sql, (username, password1, phone, email))
		# Commit to Save to database
                connection.commit()
		# Return a message to user to confirm successful registration.
                return render_template('signup.html', success='Registered Successfully')

    else:
        # Form not posted, display the form to allow user Post something
        return render_template('signup.html')
```

Above code is a Python route that takes data form the form and pushes to your users table.

<br/><br/>
Now Run your App. <br/>
Right click inside **app.py** and the select  **Run Python file in Terminal**  <br/>
Now access  http://127.0.0.1:5000/signup From your browser. <br/>

You will get below Sign Up Form , Now you can Register a User, Enter the details and Click  **Sign Up**
![image](https://user-images.githubusercontent.com/66998462/223623834-f65a2f85-6ef8-4d7b-a91c-72a7c81c6fc9.png)
![image](https://user-images.githubusercontent.com/66998462/223624216-f255b32d-7f2d-45a9-9088-bfcdd5fe8413.png)
	
Confirm in your Database users table and see the registered USER.
![image](https://user-images.githubusercontent.com/66998462/223624274-1f3224d8-aba5-4896-aa43-5426a0c745a2.png)


## Step 12
In this step we send an SMS after successful registration. To send an SMS we will do with help of AfricasTalking  Gateway. For more on check https://africastalking.com/

First install required packages
Oopen Terminal in VS Code and Type this command
```
pip3 install africastalking
```


Create a File named sms.py and place this code
```
# sending an sms
import africastalking
africastalking.initialize(
    username="joe2022",
    api_key="aab3047eb9ccfb3973f928d4ebdead9e60beb936b4d2838f7725c9cc165f0c8a"
    #justpaste.it/1nua8
)
sms = africastalking.SMS
def send_sms(phone, message):
    recipients = [phone]
    sender = "AFRICASTKNG"
    try:
        response = sms.send(message, recipients)
        print(response)
    except Exception as error:
        print("Error is ", error)
	
```


In This code we use africas talking to define the access credentials(the username and api_key)Then we define a function that will accept phone and message paramaters and send an SMS to specified Mobile Number.


Now we need to Update our /signup route done in step 11 to Send SMS after Success registration
Here os the Updated Code For /signup route.
NB: The only added code is below connection.commit() , below is the 2 lines to add
```
import sms
send_sms(phone, "Thank you for Registering")
```

3. Next we create a  **/signup**  route in our **app.py**
Put below code.
```
@app.route('/signup', methods=['POST', 'GET'])
def signup():
    # Check if form was posted by user
    if request.method == 'POST':
            # Receive what was posted by user including username, password1,password2 email, phone
            username = request.form['username']
            email = request.form['email']
            phone = request.form['phone']
            password1 = request.form['password1']
            password2 = request.form['password2']
	    
            # check if any of the password is less than eight x-ters and notify the user to put a password more that 8 -xters  
            if len(password1) < 8:
                return render_template('signup.html', error='Password must more than 8 xters')
		
            # Check if the 2 passwords are matching, if not notify the user to match them up.		
            elif password1 != password2:
                return render_template('signup.html', error='Password Do Not Match')
            else:
	        # Now we can save username, password, email, phone into our users table
		# Make a connection to database
                connection = pymysql.connect(host='localhost', user='root', password='',
                                             database='DemoClassDB')
		# Create an Insert SQL, Note the SQL has 4 placeholders, Real values to be provided later			     
                sql = ''' 
                     insert into users(username, password, phone, email) 
                     values(%s, %s, %s, %s)
                 '''
		# Create a cursor to be used in Executing our SQL 
                cursor = connection.cursor()
		# Execute SQL, providing the real values to replace our placeholders 
                cursor.execute(sql, (username, password1, phone, email))
		# Commit to Save to database
                connection.commit()
		# ADD THIS BELOW LINES
		import sms
		send_sms(phone, "Thank you for Registering")
		# Return a message to user to confirm successful registration.
                return render_template('signup.html', success='Registered Successfully')

    else:
        # Form not posted, display the form to allow user Post something
        return render_template('signup.html')


```

Now Run Your and Signup , an SMS is sent to the phone number that was used in registering. 
NB: phone number must start with +2547XXXXXXXX

## Step 13
In this section we will do a Login, The sign Up was Done in Step 11.
Inside templates Folder Create a Page named  signin.html and write  below code.
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sign In</title>
    <link href="../static/files/css/bootstrap.min.css" rel="stylesheet">
      <script src="../static/files/js/bootstrap.bundle.min.js"></script>
</head>
<body>
     <div class="container">
         {% include 'navbar.html' %}
         <section class="row">
             <div class="col-md-4">
                  <h3>Login Account</h3>
                  <span style="color:green;">{{success}}</span>
                  <span style="color:red;">{{error}}</span>
                  <form action="/signin" method="post">
                      <input type="text" name="username" placeholder="Your Username"
                      class="form-control"> <br>

                      <input type="password" name="password" placeholder="Your Password"
                      class="form-control"> <br>

                      <input type="submit" value="Sign In" class="btn btn-info">
                  </form>
                 <br>
                 <a href="/signup"> Don't Have an Account?, Create One </a>
             </div>
         </section>
     </div>
</body>
</html>
```

Next Step Open app.py and write below route
```
@app.route('/signin', methods=['POST', 'GET'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        connection = pymysql.connect(host='localhost', user='root', password='',
                                     database='DemoClassDB')

        sql = '''
           select * from users where username = %s and password = %s
        '''
        cursor = connection.cursor()
        cursor.execute(sql, (username, password))

        if cursor.rowcount == 0:
            return render_template('signin.html', error='Invalid Credentials')  
        else:
            return redirect('/')  # redirect to Home Default route, After success Login
    else:
        return render_template('signin.html')
```

	
Lastly, Put Signin Link and SignUp Links to your navbar.html
TEST SIGN IN... UPON SUCCESSFUL LOGIN IT SHOULD REDICRECT TO HOME. 
Now Run your App. <br/>
Right click inside **app.py** and the select  **Run Python file in Terminal**  <br/>
Now access  http://127.0.0.1:5000/signin From your browser. <br/>



## Step 14
In this section we will add sessions to our Web Application.
A session is a way to store information (in variables) to be used across multiple pages.<br/>
Why is a web session used? (Web session use case examples) To avoid storing massive amounts of information in-browser, developers use session IDs to store information server-side while enabling user privacy.  <br/><br/>
Seesions can be used to allow developers limit user activities by looking their session status. In this Web Applicaion we will demonstrate how session can used to users Make Payment if they have a session, without a session they can Not Make any Payment.<br/><br/>

1. Open app.py and add below code, this Line must be added at the Top below app = Flask(__name__)

```
# set secret key to secure your session/make it unique
app.secret_key = "AW_r%@jN*HU4AW_r%@jN*HU4AW_r%@jN*HU4"
```
A secret key is used for protection against data tampering. It's very important that an attacker doesn't know the value of this secret key.
Next head to the /signin route, After a successful Login we add this Code. This is the only Line you add
```
session['key'] = username  # link the session key with username
```

Your Complete /signin route look like this 
```
@app.route('/signin', methods=['POST', 'GET'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        connection = pymysql.connect(host='localhost', user='root', password='',
                                     database='DemoClassDB')

        sql = '''
           select * from users where username = %s and password = %s
        '''
        cursor = connection.cursor()
        cursor.execute(sql, (username, password))

        if cursor.rowcount == 0:
            return render_template('signin.html', error='Invalid Credentials')
        else:
	    # ADD THIS
            session['key'] = username  # link the session key with username
            return redirect('/')  # redirect to product Default route
    else:
        return render_template('signin.html')
```

Now we have stored the username in a session once a successful Login happens, This is the session Key for the Logged in user, it holds the unique username. <br/><br/>
Once a session created it Exists throughout all Pages, We need a Route to help us clear/Kill this session. This is usually the logout where a user clears a session.<br/>
Write this route to Logout
```
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/signin')
```

To Test the session. Open navbar.html You will write this Code, You can write it inside navbar-nav class.
Here is the Code.
```
<!-- Here we check if session Exists -->
{% if session['key'] %}
         <!-- If it Exists, Show the username stored in the key, Show Logout Button, Link to Logout Route --> 
	 <p>Logged in: {{ session['key'] }}</p>
	 <a href="/logout">Logout</a>
{% else %}
        <!-- If it does Not Exists, means user has not Logged in , Give a Link to Login --> 
 	<a href="/signin">Not Signed in? Sign In Now</a>
{% endif %}

```

Now Run your App. <br/>
Right click inside **app.py** and the select  **Run Python file in Terminal**  <br/>
Now access  http://127.0.0.1:5000/signin From your browser. <br/>

Before Login, Observe on NavBar Top Right in below image, It Indicates No Logged in User.
![image](https://user-images.githubusercontent.com/66998462/224215628-7f4428a0-d433-4b32-9624-77ef38f0dae4.png)


After Login It Should Indecate the Logged in User, Here i Visit http://127.0.0.1:5000/signin  and Login as joan, This is what I get. It shows That Joan is Logged in and she can Logout.

![image](https://user-images.githubusercontent.com/66998462/224216601-79ef652d-718b-46f5-8a03-2f71ef4cba10.png)


## STep 15
In this section, Now that we have the session Working, You will Buy a product and make payment. NB: User must be Logged in to make any Payment through MPESA.

Go to single.html, Somewhere in this Page, Preferably before Similar Products,  write below Section.
```
	<section class="row">
	  <div class="col-md-6">
	      <!-- Check if user is Logged in-->	  
	      {% if session['key'] %}
	      <!-- Create a Form that has an action to mpesa route, We will create this route Next-->		  
	      <form action="/mpesa" method="post">
		      <!-- Bind Current product id in an Input-->	
		  <input type="hidden" name="id" value="{{product[0]}}"
		  class="form-control"><br>
		      
                  <!-- Create a Phone Number Input -->
		  <input type="number" name="phone" placeholder="Enter Phone  2547XXXXXX"
		   class="form-control"><br>
                   ind the current Product Amount in an Input-->   
		  <label for="">To Pay KES</label>
		  <input type="number" name="amount" value="{{ product[3]}}"
		   class="form-control" readonly><br>

		  <input type="submit" value="Pay Now"
			 class="btn btn-dark">
	      </form>
	      <!-- If not Logged in, user MUST Login below to see above Form-->	  
	      {% else %}
	      <h4>Please Sign in to make Payment!</h4>
	      <a href="/signin" class="btn btn-dark btn-sm">Sign in Account</a>
	      {% endif %}
	  </div>
	</section>
```
	
	
Next Go to app.py and create below route to trigger an MPESA STK Push on Your Phone
```
import requests
import datetime
import base64
from requests.auth import HTTPBasicAuth

@app.route('/mpesa', methods=['POST', 'GET'])
def mpesa_payment():
    if request.method == 'POST':
        phone = str(request.form['phone'])
        amount = str(request.form['amount'])
        # GENERATING THE ACCESS TOKEN
        # create an account on safaricom daraja
        consumer_key = "GTWADFxIpUfDoNikNGqq1C3023evM6UH"
        consumer_secret = "amFbAoUByPV2rM5A"

        api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"  # AUTH URL
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

        data = r.json()
        access_token = "Bearer" + ' ' + data['access_token']

        #  GETTING THE PASSWORD
        timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
        passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
        business_short_code = "174379"
        data = business_short_code + passkey + timestamp
        encoded = base64.b64encode(data.encode())
        password = encoded.decode('utf-8')

        # BODY OR PAYLOAD
        payload = {
            "BusinessShortCode": "174379",
            "Password": "{}".format(password),
            "Timestamp": "{}".format(timestamp),
            "TransactionType": "CustomerPayBillOnline",
            "Amount": "1",  # use 1 when testing
            "PartyA": phone,  # change to your number
            "PartyB": "174379",
            "PhoneNumber": phone,
            "CallBackURL": "https://modcom.co.ke/job/confirmation.php",
            "AccountReference": "account",
            "TransactionDesc": "account"
        }

        # POPULAING THE HTTP HEADER
        headers = {
            "Authorization": access_token,
            "Content-Type": "application/json"
        }

        url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"  # C2B URL

        response = requests.post(url, json=payload, headers=headers)
        print(response.text)
        return '<h3>Please Complete Payment in Your Phone and we will deliver in minutes</h3>' \
               '<a href="/" class="btn btn-dark btn-sm">Back to Products</a>'
```
	

ABove Code used MPESA Safaricom MPESA Integration to Make Payment, Check https://developer.safaricom.co.ke/  For more documentation.

Now Run your App. <br/>
Right click inside **app.py** and the select  **Run Python file in Terminal**  <br/>
Now access  http://127.0.0.1:5000/signin From your browser. <br/>

Once You sign in Click on Any Product - Buy Now Button.<br/><br/>
You will see a Form requesting For a phone Number Please Your Phone Number- Must Start with +254XXXXXXXXX.
Here we selected a Cheaper Product at 1 KES to Allow make a Smaller Payment Via MPESA. Click on Pay Now, Check Your Phone youll see below screen, Enter PIN and Make Your Payment.<br/><br/>
![image](https://user-images.githubusercontent.com/66998462/224219567-da379751-0c1b-4874-af03-beb5d3e53cfe.png)

This Guide did a Complete e commerce web application that includes Routing, Templates, Static Files, Jinja2, Database Connection using MySQL, Display of Products By Category, Display Single Product, Display Similar Products, Sign Up, Sign In, Sign Out, Manage User Sessions, Send SMS, Checkout, Lipa Na MPESA etc.


## Step 16  - Student Assesment
In Section you will advance the SokoGarden by adding Vendor Register, Create a Form to save a Vendor to the database, <br/>
Part 1: Creating a Table
In your Database Create below table

![image](https://user-images.githubusercontent.com/66998462/224652003-8060d600-1e5f-471c-962a-10b804b0511b.png)


<br/>
Part 2: In Your templates Folder Create a File Named **vendor.html** and Write HTML Code to produce below Form.

![image](https://user-images.githubusercontent.com/66998462/224652321-8d5a37c5-bceb-4cb9-a3f6-15b3ad7c98d5.png)


<br/>
Part 3: In app.py, Create a Route named /vendor to help submit above Form to vendors table created in Part 1 <br/>
Your Route should start like below. 

```
@app.route('/vendor', methods=['POST', 'GET'])
def vendor():
    if request.method == 'POST':
	# Continue From Here
```

For refference on Above Task , Check Step 11, Sign Up.
	
<br/><br/>
Once Now Run your App. <br/>
Right click inside **app.py** and the select  **Run Python file in Terminal**  <br/>
Now access  http://127.0.0.1:5000/vendor From your browser. <br/>

Enter Vendor Details In the Form and Submit.
Check Your vendor table, The Vendor Record Should appear in the Table. 


Done.
End


