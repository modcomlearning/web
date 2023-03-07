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


## Step 10, This is an Optional Step But It can be done to provide More similar Product to the product displayed in Image above
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
   
Your **single.html **should be updated to Look as below.
   
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

   
   

End of Part 1


