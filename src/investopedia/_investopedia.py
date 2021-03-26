import re
import requests
import bs4
import subprocess


def _download_page(url):
    print('Downloading:', url, end='')
    resp = requests.get(url)
    resp.encoding = 'ISO-8859-1'
    print('', resp.status_code)
    soup = bs4.BeautifulSoup(resp.content, 'html.parser')
    head = soup.find('h1', 'article-heading')
    cont = soup.find('div', 'article-body')

    # remove videos
    [x.extract() for x in cont.find_all('div', 'inline-video')]

    # remove math
    [x.extract() for x in cont.find_all('span', 'katex-html')]

    return head, cont


def download_pages(urls):
    if isinstance(urls, list):
        pass
    elif isinstance(urls, str):
        urls = [urls]
    else:
        raise Exception('urls is not a list of strings')

    res = []
    for url in urls:
        head, cont = _download_page(url)
        head.attrs.pop('id')
        [x.attrs.pop('id') for x in cont.find_all('h2')]
        [x.attrs.pop('id') for x in cont.find_all('h3')]
        new_soup = bs4.BeautifulSoup()
        new_soup.append(head)
        new_soup.append(cont)
        res.append(new_soup)

    return res


def save_html(pages, file):
    with open(file, 'w') as outcon:
        for page in pages:
            outcon.write(str(page))
    return file


def convert_pdf(file, outfile=None):
    if outfile is None:
        outfile = re.sub('\\.html$', '.pdf', file)

    # -f html+tex_math_dollars+tex_math_single_backslash -t latex
    pandoc_command = f'pandoc -V fontsize=12pt -V geometry:"top=1.5cm, bottom=1.5cm, left=1.5cm, right=1.5cm" --pdf-engine=xelatex --toc -o {outfile} {file}'

    print(pandoc_command)
    subprocess.run(pandoc_command, shell=True)
