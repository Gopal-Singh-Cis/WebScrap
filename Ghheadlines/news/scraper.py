import requests
from bs4 import BeautifulSoup

# Function to scrape content from a website
def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Example: Scraping article titles
    for div in soup.find_all('div', class_='home-post-list-title'):
    # Find the <a> tag inside the <div>
        a_tag = div.find('a')
        if a_tag:
            # Extract the URL from the href attribute of the <a> tag
            article_url = a_tag['href']
            # Extract the title from the text content of the <a> tag
            article_title = a_tag.text.strip()
            # Print the URL and title
            print("Article URL:", article_url)
            # print("Article Title:", article_title)
            
            # Optionally, follow the URL and fetch additional details  position-relative share-this-item-show img-holder 
            response = requests.get(article_url)
            if response.status_code == 200:
                # Parse the linked page content
                linked_page_soup = BeautifulSoup(response.content, 'html.parser')

                div_tag = linked_page_soup.find('div', class_='article-meta').find('div')
                article_date = div_tag.text.strip()

                img_tag = linked_page_soup.find('div', class_='img-holder').find('a').find('img')
                article_image = img_tag['data-src']

                for div in linked_page_soup.find_all('div', class_='article-text'): 
                    p_tags = div.find_all('p')
                    p_text_list = [ p_tag.text.strip() for p_tag in p_tags]
                    article_content = ''.join(p_text_list)
        print("Article Title:", article_title)
        print("article_date:", article_date)
        print("article_image:", article_image)
        print("article_content:", article_content)

# Example usage
scrape_website('https://www.myjoyonline.com/')