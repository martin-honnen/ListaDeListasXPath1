#from lxml import etree as ET
from lxml import html as html

html_string = '''
<html>
    <head>
        <title>Nombres</title>
    </head>
    <body>
        
        <div class="contenedor_total">
            <div class="nombres">
                <a href="#">Pedro</a>
                <a href="#">José</a>
                <a href="#">Maria</a>
            </div>

            <div class="nombres">
                <a href="#">Arturo</a>
                <a href="#">Martha</a>
                <a href="#">Luis</a>
            </div>

            <div class="nombres">
                <a href="#">Carlos</a>
                <a href="#">Sergio</a>
            </div>

            <div class="nombres">
                <a href="#">Sandra</a>
                <a href="#">Enrique</a>
                <a href="#">Arturo</a>
            </div>
        </div>

    </body>
</html>
'''

root = html.fromstring(html_string)

result = [div.xpath('a[@href]/text()') for div in root.xpath('//div[@class = "nombres"]')]

print(result)
