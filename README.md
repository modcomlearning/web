####  E-COM  - SokoGarden
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
   
   3. Fetching Records
   # Default Home route
   ```
   @app.route('/')
def home():
    # Establish a dbase connection
    connection = pymysql.connect(host='localhost', user='root', password='',
                                 database='DemoClassDB')


    # SQL 1  - Smartphones
    sql1 = "SELECT * FROM products where product_category = 'Smartphones'"
    # Cursor - Used to run/execute above SQL
    cursor = connection.cursor()
    # Execute SQL
    cursor.execute(sql1)
    # Fetch Rows
    smartphones = cursor.fetchall()

    return render_template('home.html',
                           smartphones=smartphones)
    # above we return the smartphones in the home.html templates.
    # also make sure you upload products of Smartphones Category, use /upload route created in Step 16.
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

Below we update above **home.html**,  Update code is added on Line 347 Above. Below is the code snippet to be added.

   ```
    <br>
     <section class="slider p-4">
    <ul  class="cs-hidden autoWidth">
     <!-- We store each smartphone in item variable (We had many smartphones), The Loop below goes through all smartphones) -->
     <!-- For every smartphone item we index from 1 - 5, to access its details  i.e {{ item[5]}}  represent product image name, {{ item[1]}}  is product name . etc-->
     {% for item in smartphones %}
       <li>
         <div class="box">
             <div class="slide-img">
             <!-- Below we access the image name  {{ item[5]}}  and find it in images Folder, where we uploaded our images. Recall /uploads route-->
             <img src="../static/images/{{ item[5]}}"  width="50" height="50">
             <div class="overlay">
                 <a href="/single_item/{{ item[0]}}" class="buy-btn">Buy Now</a>
             </div>
             </div>
             <div class="detail-box">
                 {{item[1]}}<br>
                 <b class="text-warning">KES {{item[3]}}</b>
             </div>
             </div>
         </li>
        {% endfor %}
       </ul>
   </section>
  ```
  
  ### Explanation.
  Above we add a **slider** class to make the style for your slider, The slider is placed inside unordered List and a class '**autoWidth**' to make the slider Fit the 
  Page width
  Another class **overlay** , shows a buy Now Button when each product is hovered. the **Box** and **detail box** classes create a Box to place the image and the 
  details of the product.
  
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
	        <!-- Below we loop through each smartphone retrieved. We consider each smartphone as an item, we also use indexing to access specific item details like 
                cost , name etc -->
		{% for item in smartphones %}
		  <li>
		    <div class="box">
			<div class="slide-img">
			<!-- Below we place the image in the image tag -->
			<img src="../static/images/{{ item[5]}}"  width="50" height="50">
			<div class="overlay">
			    <!-- This is a Link to Buy Now, The route on href will be used Later in Next Steps -->
			    <a href="/single_item/{{ item[0]}}" class="buy-btn">Buy Now</a>
			</div>
			</div>
			<div class="detail-box">
			    <!-- Below we provide the product name and Cost. -->
			    {{item[1]}}<br>
			    <b class="text-warning">KES {{item[3]}}</b>
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
As we Run the code, we need to make sure we have products with Category 'Smartphones', Use the **/upload** route to upload products.
<br/>
Now Run your App. <br/>
Right click inside **app.py** and the select **Run Python file in Terminal** <br/>
Now access  http://127.0.0.1:5000/ From your browser. <br/>


After running, Below is the Output :crossed_fingers:
![image](https://user-images.githubusercontent.com/66998462/222487250-949b654f-ae05-4a09-a3d0-52da2ae3a239.png)

## Step 8b - Practice
In this step learn how to add more Products Slider , we will improve the home route to fetch more products from different
categories.
Go to your home route, Refer Step 7-(3), we wrote an SQL to fetch the smartphones, we are going to add another SQL to fetch 
another category Say 'detergents'.  Below is an improved home route.
```
@app.route('/')
def home():
    # Establish a dbase connection
    connection = pymysql.connect(host='localhost', user='root', password='',
                                 database='DemoClassDB')

    # SQL 1  - Smartphones
    sql1 = "SELECT * FROM products where product_category = 'Smartphone'"
    # Cursor - Used to run/execute above SQL
    cursor = connection.cursor()
    # Execute SQL
    cursor.execute(sql1)
    # Fetch Rows
    smartphones = cursor.fetchall()

    # SQL 2  - Detergents
    sql2 = "SELECT * FROM products where product_category = 'x'"

    # Execute SQL
    cursor.execute(sql2)
    # Fetch Rows
    detergents = cursor.fetchall()

    return render_template('home.html', detergents=detergents,
                           smartphones=smartphones)
```
In addtion, we now return the detergents and smartphones all together to the template, Now Lets go to **home.html** and bind detergents.

Below is how we bind detergents in home.html , its basicaly similar to smartphones, we add a new section and add the specific classes the loop every item in the detergents variable returned.
```
    <h2>Detergents</h2>
        <section class="slider p-4">
	    <ul  class="cs-hidden autoWidth">
        {% for item in detergents %}
          <li>
            <div class="box">
                <div class="slide-img">
                <img src="../static/images/{{ item[5]}}"  width="50" height="50">
                <div class="overlay">
                    <a href="/single_item/{{ item[0]}}" class="buy-btn">Buy Now</a>
                </div>
                </div>
                <div class="detail-box">
                    {{item[1]}}<br>
                    <b class="text-warning">KES {{item[3]}}</b>
                </div>
                </div>
            </li>
           {% endfor %}
          </ul>
        </section>
```
 
When you now run your web appliction, you will see to sections with sliders.  NB: Images used here are dummy they don't represent the real category and names. (looking forward to see yours with exact categories and names as per your database).
![image](https://github.com/modcomlearning/web/assets/66998462/18ae1066-6481-4e57-bdb6-5899d028cdda)

## Students Assignment.
DO SQL3 in your home route, Your SQL should select based on a given category in your database. i.e could be clothes for example, (That is in your where clause).
Return the variable fetched to **home.html**, bind the data using a for loop in **home.html**
DO SQL4 and SQL5 - Practice. Always remember to add products and their categories in the database.

Finally, In home.html, add a footer, check below Link.
[https://justpaste.it/dfnjn]

```
<section class="row bg-warning p-5">
        <div class="col-md-4">
            <h3 class="text-white">About Us</h3>
            <p class="text-white">Lorem ipsum dolor, sit amet consectetur adipisicing elit. Voluptatibus, quasi.</p>
            <p class="text-white">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Earum quibusdam cumque ullam 
            aliquid ratione assumenda tempore ducimus recusandae cupiditate? Cupiditate saepe ratione vitae neque soluta 
            repudiandae veniam quam accusantium impedit!</p>
        </div>

         <div class="col-md-4">
            <h3 class="text-white">Contact Us</h3>
            <form action="">
                  <input type="email" placeholder="Enter Email" class="form-control"> <br>
                  <textarea name="" id="" cols="5" rows="5" class="form-control" placeholder="Leave a Comment"></textarea>
                  <br>
                  <button class="btn btn-danger">Send Message</button>
            </form>
        </div>

         <div class="col-md-4">
            <h3 class="text-white">Stay Connected</h3>
             <br>
            <a href="">
                <img src="images/fb.png" alt=""> 
            </a> 
             <a href="">
                <img src="images/in.png" alt=""> 
            </a> 

             <a href="">
                <img src="images/x.png" alt=""> 
            </a> 
            <br>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Laboriosam neque tenetur quam unde officiis nesciunt 
            repellat dicta laudantium assumenda aspernatur hic consequatur labore, ducimus enim libero harum facere nihil 
            expedita!</p>
        </div>
    </section>
    <footer class="bg-dark text-center p-2">
            <b class="text-white">Developed by X.  &copy; 2024. All Rights Reserved</b>. 
    </footer>
```

Now, Your Home Page with a footer will look like below.
![image](https://github.com/modcomlearning/web/assets/66998462/b91e9985-0690-47cf-94e2-f35c81f1ae55)
You're Now Done with creating Dynamic Products Sliders with Navbar, Carousel and a Footer. :muscle:

## Step 9
In this step we will create a Page which displays when a product is clicked from Home Page.  From **Home.html**, each product had an Overlay and a **BUY** Button, It looked something like below code, Please refer your home.html. Please check Step 8.
```
<div class="overlay">
    <!-- This is a Link to Buy Now, The route on href will be used Later in Next Steps -->
    <a href="/single_item/{{ item[0]}}" class="buy-btn">Buy Now</a>
</div>
```
We need to provide a route in href = "", <a href="/single/{{ item[0]}}" class="buy-btn">Buy Now</a>, passing along the product ID. Here we use 
{{ item[0]}} since i used it in **Step 8**.  This means when you click on Buy Now it Navigates to **/single_item** route.


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
	       <!-- product variable holds the Current Product, This comes from /single_item route in app.py  -->
               <!-- product variable is indexed from 0  - 5  to access specific product details
               product[1] is product name, product[5] represent product image etc..  -->
                      <img src="../static/images/{{product[5]}}" alt="" width="300" height="300"
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
![image](https://github.com/modcomlearning/web/assets/66998462/57a299ca-e370-4c93-a4b4-0f6bdf0c0876)

When You Click on One Product - i.e Nokia   - Buy Now, You see a single Item Display.
![image](https://github.com/modcomlearning/web/assets/66998462/17f28861-7536-4f83-9cb4-00b422e7b2fd)


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
Below is Sign up Page/Route
![image](https://github.com/modcomlearning/web/assets/66998462/8700088e-7a18-4464-aeb8-c69871993977)

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


## Step 15
In this section, Now that we have the session Working, You will Buy a product and make payment. NB: User must be Logged in to make any Payment through MPESA.

Go to **single_item.html**, Somewhere in this Page, Preferably after the section with product details,  write below Section.
```
	<section class="row">
	  <div class="col-md-6">
	      <!-- Check if user is Logged in-->	  
	      {% if session['key'] %}
	      <!-- Create a Form that has an action to mpesa route, We will create this route Next-->		  
	      <form action="/mpesa" method="post">

                  <!-- Create a Phone Number Input - User will Enter the Phone number to send STK Push to;  -->
		  <input type="number" name="phone" placeholder="Enter Phone  2547XXXXXX"
		   class="form-control"><br>
                   ind the current Product Amount in an Input-->   
		  <label for="">To Pay KES</label>
                  <!-- Here, we bind current product_cost in the Cost Input, meaning users will not type the amount,
                   its automatically put/binded, its readonly you 
                  can't change it-->
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
<br>
Above we action our form to /mpesa route to be created in Next steps<br>
NB: You need to install requests if not already installed. use below command to install <br>

```
  pip3 install requests
```

Requests allows you to send HTTP requests extremely easy. Will be used in sending payment request to MPESA. <br>
<br>
Create a File named **mpesa.py**, and place below code inside.

```
import requests
import datetime
import base64
from requests.auth import HTTPBasicAuth

def stk_push(phone, amount):
    # GENERATING THE ACCESS TOKEN
    # create an account on safaricom daraja, here you are provided with below Credentials (Consumer Key and Secret Key)
    # For testing Purposes we use MODCOM Credentials
    consumer_key = "GTWADFxIpUfDoNikNGqq1C3023evM6UH"
    consumer_secret = "amFbAoUByPV2rM5A"

    # Pass Consumer and Secret Key to Mpesa URL
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials" # AUTH URL
    data = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret)).json()

    # We get access token from data above - To be used Later
    access_token = data['access_token']

    # GETTING THE PASSWORD
    timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
    business_short_code = "174379"
    # Combine the above 3 variables into single variable called "dats"
    data = business_short_code + passkey + timestamp
    # We encode data into base64(ASCII)
    encoded = base64.b64encode(data.encode())
    # Decode with utf-8
    # This might be useful if you need to pass this string as a parameter in an API request
    # Its a requirement by Safaricom to be in UTF-8(web)
    password = encoded.decode('utf-8')
    print(password)

    # BODY OR PAYLOAD
    payload = {
    "BusinessShortCode": "174379",
    "Password": "{}".format(password),
    "Timestamp": "{}".format(timestamp),
    "TransactionType": "CustomerPayBillOnline",
    "Amount": amount, # use 1 when testing
    "PartyA": phone, # change to your number
    "PartyB": "174379",
    "PhoneNumber": phone,
    "CallBackURL": "https://modcom.co.ke/job/confirmation.php",
    "AccountReference": "account",
    "TransactionDesc": "account"
    }

    # POPULATING THE HTTP HEADER
    # Headers carry the access token and content type
    # JSON is the format of data
    headers = {
    "Authorization": "Bearer " + access_token,
    "Content-Type": "application/json"
    }

    # SPECIFY SAFARICOM URL
    url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest" # C2B URL

    # Finally, using requests, we post payload and headers to above url
    # Below code will automatically send a SIM TOOLKIT(stk) push to your phone

    response = requests.post(url, json=payload, headers=headers)
    print(response.text)
```


Next Go to **app.py** and create below route to trigger an MPESA STK Push on Your Phone
```
# Below we only need to use a POST, as posted in our Single item
@app.route('/mpesa', methods = ['POST'])
def mpesa():
    # Receive the amount and phone from single item
    phone = request.form['phone']
    amount = request.form['amount']
    # import mpesa.py module
    import mpesa
    # Call the SIM Toolkit(stk) push function present in mpesa.py
    mpesa.stk_push(phone, amount)
    # SHow user below message.
    return '<h3>Please Complete Payment in Your Phone and we will deliver in minutes</h3>' \
    '<a href="/" class="btn btn-dark btn-sm">Back to Products</a>'
```
	

Above Code used MPESA Safaricom MPESA Integration to Make Payment, Check https://developer.safaricom.co.ke/  For more documentation.

Now Run your App. <br/>
Right click inside **app.py** and the select  **Run Python file in Terminal**  <br/>
Now access  http://127.0.0.1:5000/signin From your browser. <br/>

Once You sign in Click on Any Product(Costing 1 or 2 Shillings For Testing purposes) - Buy Now Button.<br/><br/> The SIngle Item will show a Form to input Phone Number. <br>
<br> 
![image](https://github.com/modcomlearning/web/assets/66998462/3aa1b004-2851-4c7f-a66f-694872c9108e)

You will see a Form requesting For a phone Number Please Your Phone Number - :point_up_2: - Must Start with +254XXXXXXXXX.
Here we selected a Cheaper Product at 1 KES to Allow make a Smaller Payment Via MPESA. Click on Pay Now, Check Your Phone youll see below screen, Enter PIN and Make Your Payment.<br/><br/>
Hope you received an STK on your Phone  <br>
:thumbsup:  :muscle:  <br>
![image](https://user-images.githubusercontent.com/66998462/224219567-da379751-0c1b-4874-af03-beb5d3e53cfe.png)


## Step 16.
This step, we will create a product upload route. <br/> Consider a web application where we can upload products and sell them online, This route will aim to allow selling/uploading product to this Application.<br/>
Please confirm that you have an **images** Folder inside your static Folder, this folder will be used to store uploaded product images. <br/>
Please Note in the database we will only store the image name and image File will be saved in **images** Folder!. 
NB: Saving images in a folder and image name in the database makes the database load faster avoiding unnecessary lag/slowness.
<br/>
In templates create a file named upload.html and write below code. The Code includes a Form that will help us write product details in our Dbaseas per our product table.<br/>

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upload</title>
    <link rel="stylesheet" href="../static/files/css/bootstrap.css">
</head>
<body>
    <div class="container -fluid">
         {% include 'navbar.html' %}
        <br>
        <section class="row">
            <div class="col-md-6 ms-5">
                <div class="card shadow p-2">
                    <h5 class="m-2">{{message}}</h5>
                    <form action="/upload" method="post" enctype="multipart/form-data">
                        <!-- Ectype - Allow Upload of a non text data like images, audio -->
                     
                        <label> Product Name </label>
                        <input type="text" name="product_name" class="form-control" required>
            
                        <label> Product Description </label>
                        <textarea name="product_desc" cols="30" rows="3" class="form-control" required></textarea>
            
                        <label> Product Cost </label>
                        <input type="number" name="product_cost" id="cost" class="form-control" required>
            
                        <label> Product Category </label>
                        <select name="product_category" class="form-control">
                            <option value="Electronics">Electronics</option>
                            <option value="Clothes">Clothes</option>
                            <option value="Electronics">Electronics</option>
                            <option value="Utensils">Utensils</option>
                            <option value="Smartphones">Smartphones</option>
                            <option value="Other">Other</option>
                        </select><br>
            
            
                        <label> Product Image </label>
                        <input type="file" name="product_image_name" class="form-control" required><br>
            

                        <input type="submit" value="Add/Upload Product" class="btn btn-success" required><br>
                    </form>
                </div>
            </div>
        </section>
    </div>
</body>
</html>
```
![image](https://github.com/modcomlearning/web/assets/66998462/24c4bb82-072c-47ce-b36a-f84fd7101647)

## Explanation
```
 <form action="/upload" method="post" enctype="multipart/form-data">
```
Above code means that on **Submit** the form,  will navigate to **/upload** route using method **POST** <br/>
enctype="multipart/form-data"  is an attribute that means our form will have a File to upload, in this case the image. <br/><br/>
First in the form, we include a navbar.html, a section and a card.
The Form has Five inputs. product_name, product_desc, product_cost, product_category, product_image_name.<br/>
It also includes, a textarea to upload long description and a Select option for the Category Drop Down, Other inputs and a Submit Button.<br/>
<br/>

After Creating the **upload.html** Form, we now create the route that is used to Upload the image to images Folder and the other details including image_name to the database. In you app.py, write below **route** code , its the **/upload **route. 
```
# pymysql is python package to help/aid in database connection. 
import pymysql

@app.route('/upload', methods=['POST', 'GET'])
def upload_product():
    # Below if works when the Form in upload.html is Submitted/Sent
    if request.method == 'POST':
        # Below receives all variables sent/submitted from the Form
        product_name = request.form['product_name'] 
        product_desc = request.form['product_desc']
        product_cost = request.form['product_cost']
        product_category = request.form['product_category']
        product_image_name = request.files['product_image_name']
        product_image_name.save('static/images/' + product_image_name.filename) # Saves the image File in images folder, in static Folder.

        # Connect to DB
        connection = pymysql.connect(
            host='localhost', user='root', password='', database='DemoClassDB')
        # Create a Cursor
        cursor = connection.cursor()
        
        # Prepare you data, Notice the 'product_image_name.filename' below, Gets only the image name not the File
        data = (product_name, product_desc, product_cost,
                product_category, product_image_name.filename)
        # Do SQL, Be keen on columns spelling, should be same as in database
        # %s in the SQL means placeholder to be replace by the data above.
        sql = "insert into products (product_name, product_desc, product_cost, product_category, product_image_name) values (%s, %s, %s, %s, %s)"
        try:
            # Excecute SQL, parsing your data
            cursor.execute(sql, data)
            connection.commit() # Commit to write changes to database and render a success message to upload template
            return render_template('upload.html', message='Product Added Successfully')
        except:
            # In case of an Error/Exception rollback to undo chnages and return a fail message to upload template
            connection.rollback()
            return render_template('upload.html', message='Failed, Try Again Later')

    else:
        # Below renders the template when a user accesses the /upload route, it shows the upload.html so that the user can input product details and POST/submit
        return render_template('upload.html', message='Please Add Product Details')
```
## Explanation
Above code is used to receive details from the Uploads Form and save them to the database (product table).<br/>
Run Your App and Navigate to upload route.<br/>
[http://127.0.0.1:5000/upload] , You can add a Link to **/upload** in your Navba, For quick access to the route.<br/>
Below is the Output, Fill the product details and upload the Image and Submit, Confirm that the image file goes to **static/images** Folder, and other details including image name are saved in **products** table in your DBase. <br/> Below is a Test of Uploading a Nokia Phone, After Filling the Form Clcik submit and Success Message is shown at the Top of the Form.
![image](https://github.com/modcomlearning/web/assets/66998462/28d270e1-5a38-4510-8e8c-f466c500588a)
<br/>
We do Confirm the Nokia Product is saved in the Database, all details including image name nokia1.jpg are seen in below screenshot.
![image](https://github.com/modcomlearning/web/assets/66998462/08e7f506-f3c3-40e3-abf2-93249eee5dfe)

And the image File is present in **static/images** Folder.
![image](https://github.com/modcomlearning/web/assets/66998462/8980eb25-16cd-4c39-b9d8-c8aa4e8ef6d9)
Done!. :thumbsup: 
Please add/upload several products in different categories using **/upload** route


<b>DONE</b> <br>
This Guide did a Complete e commerce web application known as Soko Garden that includes Routing, Templates, Static Files, Images, Jinja2, Database Connection using MySQL, Display of Products By Category, Display Single Product, Sign Up, Sign In, Sign Out, Manage User Sessions, Send SMS, Checkout, Payment Integration - Lipa Na MPESA etc. You can use this project in coming up with your Final project Later in this Program. <br>
<br>
Hope you liked SokoGarden Project, You can Now Buy me a Coffee :coffee:<br/>
Follow us on twitter @ModcomKenya

<!--
## Step 17  - Student Assesment
In this Section you will advance the SokoGarden by adding Vendor Register, Create a Form to save a Vendor to the database, <br/>
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
-->


