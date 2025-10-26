<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Social Media Platform</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Welcome to SocialHub</h1>
        <nav>
            <a href="#login">Login</a>
            <a href="#register">Register</a>
            <a href="#posts">Posts</a>
        </nav>
    </header>
    
    <main>
        <!-- User Registration/Login -->
        <section id="login">
            <h2>Login</h2>
            <form id="loginForm">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required>
                
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>
                
                <button type="submit">Login</button>
            </form>
        </section>

        <section id="register">
            <h2>Register</h2>
            <form id="registerForm">
                <label for="newUsername">Username:</label>
                <input type="text" id="newUsername" name="username" required>

                <label for="newPassword">Password:</label>
                <input type="password" id="newPassword" name="password" required>

                <button type="submit">Register</button>
            </form>
        </section>

        <!-- Create a Post -->
        <section id="createPost">
            <h2>Create Post</h2>
            <form id="postForm">
                <label for="postContent">Content:</label>
                <textarea id="postContent" name="content" required></textarea>

                <label for="tags">Tags (comma-separated):</label>
                <input type="text" id="tags" name="tags">

                <button type="submit">Post</button>
            </form>
        </section>

        <!-- Public Posts -->
        <section id="posts">
            <h2>Public Posts</h2>
            <div id="postList">
                <!-- Dynamically loaded posts -->
            </div>
        </section>

        <!-- Subscriptions -->
        <section id="subscriptions">
            <h2>Subscriptions</h2>
            <form id="subscriptionForm">
                <label for="subscribeTo">Subscribe to user:</label>
                <input type="text" id="subscribeTo" name="username" required>
                <button type="submit">Subscribe</button>
            </form>
            <h3>Your Subscriptions</h3>
            <ul id="subscriptionList">
                <!-- Dynamically loaded subscriptions -->
            </ul>
        </section>

        <!-- Comments -->
        <section id="comments">
            <h2>Comments</h2>
            <form id="commentForm">
                <label for="commentContent">Comment:</label>
                <textarea id="commentContent" name="comment" required></textarea>
                <button type="submit">Add Comment</button>
            </form>
            <div id="commentList">
                <!-- Dynamically loaded comments -->
            </div>
        </section>

    </main>

    <footer>
        <p>&copy; 2025 SocialHub. All Rights Reserved.</p>
    </footer>

    <script src="scripts.js"></script>
</body>
</html>
