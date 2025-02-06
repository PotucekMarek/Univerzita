<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Aurora</title>
    </head>
    <body>
        <?php
            $integerVar = 10;
            $stringVar = "Hello, PHP!";
            $floatVar = 3.14;
            $booleanVar = true;

            echo "Integer: $integerVar<br>";
            echo "String: $stringVar<br>";
            echo "Float: $floatVar<br>";
            echo "Boolean: " . ($booleanVar ? 'true' : 'false') . "<br>";
        ?>

        <?php
            $number = 7;

            if ($number > 0) {
                echo "$number is positive.<br>";
            } elseif ($number < 0) {
                echo "$number is negative.<br>";
            } else {
                echo "$number is zero.<br>";
            }
        ?>
        <?php
            for ($i = 0; $i < 3; $i++) {
                echo "Line $i<br>";
            }
        ?>
        <?php
            $number = 7;

            if ($number > 0) {
                echo "$number is positive.<br>";
            } elseif ($number < 0) {
                echo "$number is negative.<br>";
            } else {
                echo "$number is zero.<br>";
            }
        ?>
        <div><br>Iteration:</div>
        <?php
            for ($i = 0; $i < 5; $i++) {
                echo "Iteration: $i<br>";
            }
        ?>

        <?php
            $name = "Marek";
            function greeting($name) {
                return "Hello, $name!<br>";
            }

            echo greeting("$name");
        ?>

        <?php
            $person = array("name" => "Marek", "age" => 23, "city" => "Brno");

            echo "Name: " . $person["name"] . "\n";
            echo "Age: " . $person["age"] . "\n";
            echo "City: " . $person["city"] . "\n";
        ?>

        <form action="process.php" method="post">
            Name: <input type="text" name="name">
            Age: <input type="number" name="age">
            <input type="submit">
        </form>

    </body>
</html>