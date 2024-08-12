<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $pin = $_POST["pin"];
    $token = $_POST["token"]; // Get the token from the form

    // Validate the PIN code
    $validPin = "1234";  // Example valid PIN code, replace with your own logic
    if ($pin === $validPin) {
        echo "PIN code is correct. Token: " . htmlspecialchars($token);
        // You can redirect to a specific page or display the content based on the token0
        $error = "Invalid PIN code. Please try again.";
    }
} else {
    if (isset($_GET["token"])) {
        $token = $_GET["token"];
    } else {
        $error = "No token provided.";
        $token = "";
    }
}
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enter PIN Code</title>
</head>

<body>
    <h1>Enter PIN Code</h1>
    <?php if (isset($error)): ?>
        <p style="color: red;"><?php echo $error; ?></p>
    <?php endif; ?>
    <form method="post" action="">
        <label for="pin">PIN Code:</label>
        <input type="password" id="pin" name="pin" required>
        <input type="hidden" name="token" value="<?php echo htmlspecialchars($token); ?>">
        <button type="submit">Submit</button>
    </form>
</body>

</html>