# Extract product details from a single product element and append to all_data
# (This cell is now part of the main loop, but you can break it out for clarity if needed)
# Example usage inside the loop:
#   extract_product_data(product)

def extract_product_data(product):
    title_elem = product.find('span', {'class': 'a-size-medium a-color-base a-text-normal'})
    if not title_elem:
        h2_elem = product.find('h2')
        if h2_elem:
            title_elem = h2_elem.find('span')
    title = title_elem.text.strip() if title_elem else None
    price_whole = product.find('span', {'class': 'a-price-whole'})
    price_fraction = product.find('span', {'class': 'a-price-fraction'})
    rating_elem = product.find('span', {'class': 'a-icon-alt'})
    link_elem = product.find('a', {'class': 'a-link-normal s-no-outline'})
    price = None
    if price_whole and price_fraction:
        price = price_whole.text.strip() + price_fraction.text.strip()
    elif price_whole:
        price = price_whole.text.strip()
    rating = rating_elem.text.strip() if rating_elem else None
    link = 'https://www.amazon.in' + link_elem['href'] if link_elem else None
    all_data.append({'Title': title, 'Price': price, 'Rating': rating, 'Link': link})
