Initially this would have been the first project I wanted to use Unit tests to do my testing for me.
Unfortunatly my coding abilities for production are better than my coding abilities for testing.

I had to fall back on my old-school technique of manuall testing everything. 

---  
# Content
- [Functionality testing](#Functionality-Testing)
    - [Login / Registration](#Login/Registration)
    - [Adding product to the bag](#Adding-product-to-the-bag)
    - [Modifying the bag](#Modifying-the-bag)
    - [Adding product to wishlist](#Adding-product-to-wishlist)
    - [Modifying Wishlist](#Modifying-Wishlist)
    - [Commenting on products](#Commenting-on-products)
    - [Deleting comments](#Deleting-comments)
    - [Checkout](#Checkout)
    - [Profile](#Profile)
    - [Product Admin](#Product-Admin)
    - [Browsing products](#Browsing-products)
    - [Search functionality](#Search-functionality)
    - [Logout](#Logout)

- [Hidden features testing](#Hidden-features-testing)
    - [Stripe](#Stripe)
    - [Webhooks](#Webhooks)
--- 
# Functionality Testing 
---
## Login/Registration
### Registration
- A new user opens the site
- Clicking on "My Account" > Register - takes the user to the registration form
- Filling out the form and submitting it sends a email to the user
- Clicking on the link in the email takes the user to the sign in page where they sign in
- Sign in is successful with the registered details

#### Forcing URLS
- Forcing URLs does not work since a unique key is attached to the link sent to the user
- Forcing Other URLs will only generate the registration page, the login page and the home page

### Login
- A user who has registered and is logged out opens the site
- Clicking on "My Account" > Sign in - takes user to a sign in page
- Filling out the form successfully sends user to the home page and they are signed in
- Unsuccessful submissions result in errors being displayed
    - Users are able to change their password if needed

## Adding product to the bag
- A new site user or a registered user is using the site
- A user uses the main navigation or search functionality to find a product
- Opening a product details page and clicking on add to bag adds a product to the cookie created
    - The user is able to select the amount of that item (quantity)
    - The user is unable to add more than what is in stock
- Clicking on the bag icon then takes the user to the page where they can view their bag and make modifications


### Forcing URLs
- Forcing a URL like `bag/add/2` creates a TypeError without submitting a form
- To prevent such things from happening: This code has been implemented in bag/views.py to handle `GET` requests to URLs which users are not supposed to visit
```
    else:
        messages.error(request, "No such URL exists")
        return render(request, 'home/index.html')
```
## Modifying the bag
- A user (new/old) has items in their bag and is at the page where they view their bag
- Items are displayed in a table
- Modifications occur under the *Qty* table heading
- Changing the quantity and clicking on "Update" will update the quantity (can't go higher than 99 and lower than 0 - via the buttons)
    - If a user wants to add more stock (quantity) than what the store has in stock a error message will appear
- Clicking on "Delete" will remove a item from the bag
- Setting the quantity to 0 or lower (manually) and clicking update will remove that item from the bag
- If all items have been removed then text saying "Your bag is empty" will appear

### Forcing URLs
- After the modifications in [Adding product to the bag](#Adding-product-to-the-bag) users are unable to force URLs

## Adding product to wishlist
- To access this feature a user must be logged in. Forcing URLS (not logged in) will result in a Sign in page appearing
- A signed in user can add a product to their wishlist by clicking "Add to wishlist" - a success message will appear saying that the item has been added to their wishlist
- The Add to Wishlist button is available on the products page or the product's details page. 

### Forcing URLs
- A user is unable to add produts through forcing URLs and will be redirected to the home page with a error message

## Modifying Wishlist
- To access this feature a user must be logged in. Forcing URLS (not logged in) will result in a Sign in page appearing.
- 
## Commenting on products
## Deleting comments
## Checkout
### Checkout Conflict
- If two users order the last item at the exact same time nothing will happen
- The user Who checks out first (successfully) will modify the stock 
- When the second wants to checkout their stock is checked
- If the remaining stock is less than 0 then a error will apear telling them which item has run out of stock
- The second user will not be able to checkout until they modify their bag
- After the modifications the second user is able to checkout
## Profile
## Product Admin
## Browsing products
## Search functionality
## Logout
# Hidden features testing
## Stripe
## Webhooks