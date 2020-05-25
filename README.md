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
- Automatic email feature where it'll email the user all the recipes for the day at the beginning of each day on which there's a meal plan. User can of course specify the time the email goes out.

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

### Add/Edit Recipe
A form to add a new recipe:

*MVP*:

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

*Future*:

- Photo Upload
- Category
- Estimated cost
- Prep time
- Cook time
- Total time
- Required Equipment

### All Plans
Lists all the meal plans the user has made, with a + button to add a new one (takes them to Create Plan page)

### Create/Edit Plan
- Plan name
- Date Range (week will be the default)
Shows the user somewhat of a grid view, with columns being days, and rows being mealtime slots.
On mobile this will be a list, with collapsible sections for each day.
User can add multiple recipes to each slot.
When a recipe is added to a slot, the user has the option to specify how many servings they expect to eat for that meal.
When the recipe is able to make more servings, the user will be un-intrusively prompted (via a small alert in the recipe's box) to add that meal again later in the week as a leftover.
The user can just hit "No Thanks" if they don't want to block out that meal again in the week (it probably either doesn't reheat well, it's for a special occasion, or they just want to do something else with it)
At the bottom of the page, there's a "Create List" button that goes to the list section and automatically generates a shopping list based on the recipes.

*Future*:

Instead of leftovers, the user can reduce the amount that the recipe makes.
Users can customize mealtime slots
Templates for:
    - Slot configuration (other meals, intermittent fasting, planned snacking, etc.)
    - Meal Combinations (If you like to have bacon with your eggs regularly and don't want to keep adding both every time)
    - Days? (not sure how this would play with the different slots)

### View Plan
Same as create/edit, except without any form fields. Allows for easy navigation to recipes in the list.

### All Lists
Grid view showing the shopping lists the user has created, with a + button to add a new one (takes them to Create List page)

### Create/Edit List
- List name (default: "Shopping List for [date]")
- Create from plan button
- Add item to list
- Remove item from list
- Save List
- View List

*Future*:

- Sort list by store section
- User can easily change order of sections

### View List
- Allows for checking off of items
- Easy copy and paste functionality for phones
- Export list to pdf & email
- Print list