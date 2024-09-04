**USAGE-EXAMPLE**
- Quick use

```
import easyhost.EasyHost as eh
host1 = eh.EasyHost(port=1234) # turn on http://localhost:1234/
host1.set(route='/wasdwasdwasd', file='example.png') #also able .html .mp4 etc..
input("Press Enter to exit...")
```


- Full use
```
import easyhost.EasyHost as eh
host1 = eh.EasyHost(port=1234)
host1.set(route='/wasdwasdwasd', file='example.html')
host1.set_shared_dict(dict_path='worldlove/dog', arg=555)
dog_love = host1.get_shared_dict('worldlove/dog')
input("Press Enter to exit...")
```

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
**INSTALLATION**
```
pip install https://github.com/kikunayar/easyhost.git
```
