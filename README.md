**USAGE-EXAMPLE**


- mypyname.py
```
import easyhost.EasyHost as eh

# Create an instance of the EasyHost class, which sets up an HTTP server
# on the localhost at port 1234
host1 = eh.EasyHost(port=1234)

# Define a route '/wasdwasdwasd' and associate it with the 'example.html' file
# This allows the server to serve the HTML or .png . mp4 etc.. file when the route is accessed
host1.set(route='/wasdwasdwasd', file='example.html') 

# for Set a value in the shared dictionary, which can be accessed from both
# the Python code and the HTML code
# host1.set_shared_dict(dict_path='worldlove/dog', arg=555)

# Retrieve the value from the shared dictionary
# dog_love = host1.get_shared_dict('worldlove/dog')

# Keep the program running until the user presses Enter
input("Press Enter to exit...")
```


- example.html if you need the communication
```
<!DOCTYPE html>
<html>
<head>
    <title>Shared Dict Example</title>
</head>
<body>

    <script>
        // Update the value in the shared dictionary
        async function updateValue() {
            await setSharedDict('worldlove/dog', true);
            const value = await getSharedDict('worldlove/dog');
            document.getElementById('result').textContent = `Dog love: ${value}`;
        }
    </script>
</body>
</html>
```
