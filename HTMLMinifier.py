class MinifyHTML(object):
    def __init__(self, htmlFilename, escapeCharacters):
        minifiedHTML = self.minify(open(htmlFilename, 'r').readlines())
        if (escapeCharacters):
            print(escape(minifiedHTML))
        else:
            print(minifiedHTML)

    def minify(htmlLines):
        result = ""
        for line in htmlLines:
            result += line.strip()
        return result

    def escape(html):
        minifiedHTML.replace("'", "\\'")
        minifiedHTML.replace('"', '\\"')

while(True):
    MinifyHTML(input("Filename > "), bool(input("Escape Characters? [True/False] > ")))
