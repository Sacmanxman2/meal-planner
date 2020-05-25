# Notes for Meal Planning app

## Features:
- User login (with OAuth support)
- Recipe Management
    - Create your own recipes
    - Import recipe from link (using schema.org recipe type)
    - Recipe data must include servings
    - Users can add comments & notes to recipes
- Meal Planning
    - Users can specify mealtimes for each day (default will be "Breakfast", "Lunch", "Dinner", "Extra / Snack")
    - Users can add a meal to a specific day's time, and specify how many servings they expect to eat.
    - Program will automatically recognize if there are leftover servings and suggest planning it for a meal the next day if there are.
    - Drag and drop functionality to move meals around
- Shopping list
    - Will automatically generate the shopping list of necessary ingredients for the week
    - Can check items off the list
    - Can export list to pdf, email, printer, etc.

## Potential upcoming features:
- Freezer meals
- "My Kitchen" page on which users can specify what equipment they have as well as pantry staples & spices. The program will remind them to check every week or so to make sure they have them when they make the shopping list.

---

# Content
## Logged out (landing pages)
@TODO

## Logged in (webapp)
### Header Layout
*Logo - Left on desktop - first on hamburger*

*Main App Functionality - Center top on Desktop, second on hamburger*
- Recipes
    - All Recipes
    - Add Recipe
- Meal Planning
    - All Plans
    - Create Plan
- Shopping
    - All Lists
    - Create List

*Settings & User info - Right on Desktop - third on hamburger*
- Log In

### All Recipes
Lists all the recipes the user can make in a grid OR table, with a + button to add a new one (takes them to Add Recipe page)

### Add Recipe
A form to add a new recipe:
MVP:
- Title
- Description
- Ingredients list
    - Name
    - Unit
    - Quantity
- Directions (an array of steps)
- Serving size
- Number of servings
- External link (if applicable)
- Notes

Future:
- Category
- Estimated cost
- Prep time
- Cook time
- Total time
- Required Equipment