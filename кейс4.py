<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Online Bookstore</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Welcome to MyBookStore</h1>
        <nav>
            <a href="#user">User Interface</a>
            <a href="#admin">Admin Interface</a>
        </nav>
    </header>

    <main>
        <!-- User Interface -->
        <section id="user">
            <h2>User Interface</h2>
            <div id="library">
                <h3>Library</h3>
                <div id="bookList">
                    <!-- Dynamically loaded books -->
                </div>
            </div>
            <div id="filters">
                <h3>Sort by:</h3>
                <label for="category">Category:</label>
                <select id="category">
                    <option value="">All</option>
                    <!-- Dynamic categories -->
                </select>

                <label for="author">Author:</label>
                <select id="author">
                    <option value="">All</option>
                    <!-- Dynamic authors -->
                </select>

                <label for="year">Year:</label>
                <select id="year">
                    <option value="">All</option>
                    <!-- Dynamic years -->
                </select>
                <button id="applyFilters">Apply Filters</button>
            </div>
            <div id="rentalOptions">
                <h3>Rent or Buy</h3>
                <label for="rentalDuration">Choose duration:</label>
                <select id="rentalDuration">
                    <option value="2">2 weeks</option>
                    <option value="4">1 month</option>
                    <option value="12">3 months</option>
                </select>
                <button id="rentOrBuy">Confirm</button>
            </div>
        </section>

        <!-- Admin Interface -->
        <section id="admin">
            <h2>Admin Interface</h2>
            <form id="manageBooks">
                <h3>Manage Books</h3>
                <label for="bookTitle">Title:</label>
                <input type="text" id="bookTitle" name="title" required>

                <label for="bookAuthor">Author:</label>
                <input type="text" id="bookAuthor" name="author" required>

                <label for="bookCategory">Category:</label>
                <input type="text" id="bookCategory" name="category" required>

                <label for="bookYear">Year:</label>
                <input type="number" id="bookYear" name="year" required>

                <label for="bookPrice">Price:</label>
                <input type="number" id="bookPrice" name="price" required>

                <label for="bookStatus">Status:</label>
                <select id="bookStatus" name="status">
                    <option value="available">Available</option>
                    <option value="rented">Rented</option>
                </select>

                <button type="submit">Add/Update Book</button>
            </form>

            <div id="reminders">
                <h3>Rental Reminders</h3>
                <button id="sendReminders">Send Reminders</button>
            </div>
        </section>
    </main>

    <footer>
        <p>&copy; 2025 MyBookStore. All Rights Reserved.</p>
    </footer>

    <script src="scripts.js"></script>
</body>
</html>

