import argparse
import investopedia as iv


def main():
    parser = argparse.ArgumentParser(description='Investopedia page downloader:')
    parser.add_argument('-v', '--version', action='version', version=iv.__version__)
    parser.add_argument('-p', '--no-pdf', help='Do not attempt to create PDF file', action='store_true')
    parser.add_argument('-o', '--output-file', type=str, help='output file')
    parser.add_argument('-m', '--input-file' , type=str, help='input file')
    parser.add_argument('urls', help='urls you want to download.', nargs="+")
    args = parser.parse_args()

    # parse args
    urls = args.urls
    pdf = not args.no_pdf

    if args.output_file:
        output_file = args.output_file
    else:
        output_file = 'generated_investopedia_book.html'

    # pipeline
    pages = iv.download_pages(urls)
    filename = iv.save_html(pages, output_file)
    if pdf:
        iv.convert_pdf(filename)


if __name__ == "__main__":
    main()
