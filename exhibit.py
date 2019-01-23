import glob
from random import shuffle


def get_images():
    images = glob.glob("gallery/*.png")
    shuffle(images)
    return images


def format_html(images):
    with open("reveal.js/index.html", 'r') as template:
        lines = iter(template.readlines())

    stylesheet = "<link rel=\"stylesheet\" href=\"css/theme/night.css\">\n"
    title = "<section><h1>Blobs And Flags</h1></section>\n"
    img = "<section><img src=\"../{}\" width=\"1200\" height=\"500\"></section>\n"

    content = []
    for line in lines:
        if "<link rel=\"stylesheet\" href=\"css/theme/black.css\">" in line:
            content.append(" "*4 + stylesheet)
        elif "<section>Slide 1</section>" in line:
            content.append(" "*8 + title)
            for image in images:
                content.append(" "*8 + img.format(image))
            next(lines) # skip <section>Slide 2</section>
        else:
            content.append(line)

    return content


def write_html(content):
    with open("reveal.js/index.html", 'w') as html:
        for line in content:
            html.write(line)


if __name__ == '__main__':
    
    images = get_images()

    content = format_html(images)

    write_html(content)
