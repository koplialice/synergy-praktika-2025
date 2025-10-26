Travel Diary Website
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Travel Diary</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Travel Diary</h1>
        <nav>
            <a href="#register">Register</a>
            <a href="#addTravel">Add Travel</a>
            <a href="#viewTravels">View Travels</a>
        </nav>
    </header>

    <main>
        <!-- Registration Section -->
        <section id="register">
            <h2>Register or Login</h2>
            <form id="userForm">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required>

                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>

                <button type="submit">Submit</button>
            </form>
        </section>

        <!-- Add Travel Section -->
        <section id="addTravel">
            <h2>Add Your Travel</h2>
            <form id="travelForm">
                <label for="destination">Destination:</label>
                <input type="text" id="destination" name="destination" required>

                <label for="location">Location (Coordinates):</label>
                <input type="text" id="location" name="location" placeholder="Latitude, Longitude" required>

                <label for="image">Upload Image:</label>
                <input type="file" id="image" name="image" accept="image/*">

                <label for="cost">Cost ($):</label>
                <input type="number" id="cost" name="cost">

                <label for="rating">Rate the Trip:</label>
                <select id="rating" name="rating">
                    <option value="excellent">Excellent</option>
                    <option value="good">Good</option>
                    <option value="average">Average</option>
                    <option value="poor">Poor</option>
                </select>

                <button type="submit">Add Travel</button>
            </form>
        </section>

        <!-- View Travels Section -->
        <section id="viewTravels">
            <h2>View Travels</h2>
            <div id="travelsList">
                <!-- Travels dynamically loaded here -->
            </div>
        </section>
    </main>

    <footer>
        <p>&copy; 2024 Travel Diary. All rights reserved.</p>
    </footer>

    <script src="scripts.js"></script>
</body>
</html>

