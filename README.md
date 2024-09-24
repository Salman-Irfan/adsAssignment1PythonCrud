<!DOCTYPE html>
<html>
<head>
  <title>Product Management Program</title>
</head>
<body>

  <h1>Product Management Application</h1>

  <p>This Python program allows you to manage a list of products by adding, updating, deleting, and viewing them. The application operates in a simple CLI where the user can choose various options from a menu.</p>

  <h2>Features</h2>
  <ul>
    <li>Display all products in a tabular format</li>
    <li>Add a new product with details like PID, name, description, rating, price, and image URL</li>
    <li>Delete a product by its PID</li>
    <li>Update product details such as name, description, rating, price, and image URL</li>
    <li>Exit the program</li>
  </ul>

  <h2>Technologies Used</h2>
  <ul>
    <li>Python 3.12.2</li>
  </ul>

  <h2>Installation</h2>
  <p>To run this application, follow the steps below:</p>
  <ol>
    <li>Ensure Python 3.12.2 is installed on your machine.</li>
    <li>Clone this repository using the following command:
      <pre><code>git clone https://github.com/Salman-Irfan/adsAssignment1PythonCrud.git</code></pre>
    </li>
    <li>Navigate to the project directory:
      <pre><code>cd adsAssignment1PythonCrud</code></pre>
    </li>
    <li>Run the Python script:
      <pre><code>python products_crud.py</code></pre>
    </li>
  </ol>

  <h2>How to Use</h2>
  <p>Upon running the program, you will be presented with a menu of options:</p>
  <ul>
    <li><strong>1. Show all products:</strong> Displays all the products currently available in a tabular format, showing their details (PID, name, description, rating, price, and image URL).</li>
    <li><strong>2. Add new product:</strong> Allows you to add a new product by entering its details, including PID, name, description, rating, price, and image URL.</li>
    <li><strong>3. Delete a product:</strong> Deletes a product by asking for the Product PID. You can also cancel the operation by typing "cancel".</li>
    <li><strong>4. Update a product:</strong> Allows you to update the details of a product by selecting a field to update (name, description, rating, price, or image URL) by providing its PID. You can cancel the update by typing "cancel".</li>
    <li><strong>5. Exit:</strong> Exits the program.</li>
  </ul>

  <h2>Sample Data for Testing</h2>
  <p>You can use the following sample products to test the application's functionality:</p>

  <table border="1">
    <tr>
      <th>Product ID</th>
      <th>Product Name</th>
      <th>Description</th>
      <th>Rating</th>
      <th>Price</th>
      <th>Image URL</th>
    </tr>
    <tr>
      <td>P001</td>
      <td>Refrigerator</td>
      <td>Refrigerator of Dawlance</td>
      <td>4.5</td>
      <td>55000</td>
      <td><a href="#">Image Link</a></td>
    </tr>
    <tr>
      <td>P002</td>
      <td>Washing Machine</td>
      <td>Washing Machine of PEL</td>
      <td>4.2</td>
      <td>32000</td>
      <td><a href="#">Image Link</a></td>
    </tr>
  </table>

  <h2>Contribution</h2>
  <p>Feel free to fork this repository, submit issues, or contribute new features via pull requests.</p>


</body>
</html>
