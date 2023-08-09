import requests
from bs4 import BeautifulSoup

def scrape_reviews(base_url, num_pages):
    print(f"Scraping reviews from {base_url}...")
    
    reviews = []
    sentiments = []
    helpfuls = []  # Adding a list to store the 'helpful' information

    for page_num in range(1, num_pages + 1):
        url = f"{base_url}?page={page_num}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        review_elements = soup.find_all('div', class_='jdgm-rev__body') # assuming each review is in a 'div' tag with class 'review'

        for review_element in review_elements:
            # Extracting the review text
            review_text_element = review_element.find('span')  # assuming the review text is in a 'p' tag
            review_text = review_text_element.text if review_text_element else ''
            reviews.append(review_text)

            # Extracting the review rating
            div_element = review_element.find('div', class_='jdgm-row-rating')
            if div_element:  # if the div element is found
                rating_element = div_element.find('span', class_='jdgm-rev__rating')
                if rating_element:  # if the rating element is found
                    rating = int(rating_element['data-score'])  # access the 'data-score' attribute
                else:
                    rating = 3  # use a neutral rating as default if it's not found
            else:
                rating = 3  # use a neutral rating as default if div is not found

            sentiment = 'positive' if rating > 3 else 'negative' if rating < 3 else 'neutral'  # converting rating to sentiment
            sentiments.append(sentiment)

            # Extracting the review helpful count
            helpful_element = review_element.find('span', {'data-hook': 'helpful-vote-statement'})  # assuming the helpful count is in a 'span' with data-hook 'helpful-vote-statement'
            if helpful_element is not None:
                helpful = helpful_element.text
            else:
                helpful = '0 people found this helpful'
            helpfuls.append(helpful)  # adding the helpful count to the list

            # Print the review text, rating, sentiment, and helpful count for debugging
            print(f"Review: {review_text}\nRating: {rating}\nSentiment: {sentiment}\nHelpful: {helpful}\n")

    print(f"Scraped {len(reviews)} reviews.\n")
    return reviews, sentiments, helpfuls  # return the list of 'helpful' counts along with the other lists
