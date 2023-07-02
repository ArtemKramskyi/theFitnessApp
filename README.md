#

![markdown logo](https://escrituras-eremitas.com/wp-content/uploads/2023/05/fitnessLogoNoBg.png)

---

> _The Fitness App_ is a project by __Artem Kramskyi__. Using the Django framework this is an application that allow users to create exercising programs.
>
> Once the user has created an account they are able to access a catalog of exercises that they can select and add to their programs. These exercises contain instructions on how to perform the exercises in a safe and proper form.

---

## Technologies

- HTML
- CSS
- JavaScript
- Python
- Django
- Tailwind CSS

---

## Client-side files

- [Templates/base](./base/templates/base/)
  - Layout.html: Loads on regular pages and contains the header of the site.
  - Index.html: This is the landpage of the project and if the user is not logged it loads as a introduction page prompting the user to Register or to Login to their account. If the user is logged in then it loads as a dashboard that allow users to see their workout programs. exercises, etc.
  - Login.html: Allow users to log in sending their credentials to the server-side.
  - Register.html: Allow users to register sending their credentials to the server-side.
  - myPrograms.html: Using Django Templates 'for' loop, it load all the programs for current user.
  - programPage.html: Program page relies on a dynamic url and it load the page for the partilar workout program showing all relevant information of the exercises such as sets and repetitions.
- [Static/base](./base/static/base/): This contains the css of the project as well as the JavaScript files.
  - JavaScript: The JavaScript files have two main purposes:
    1. Allow elements such as modals to be manipulated on the DOM;
    2. In certain cases they allow for the submission of forms.
  - CSS: The CSS is a mixture of vanilla CSS and Tailwind CSS. This allow for a more dynamic design and to prevent other from being overloaded.

---

## Server-side files

- [models.py](./base/models.py): Contains four Models
  - User Model: Handles the database for user accounts
  - ExercisesCatalog Model: Handles the database for the exercises and includes information such as number of sets and repetitions for that particular exercise. This dabase can only be manipulated by the admins using the admin's client.
  - Program Model: Store the name of the programs
  - Plan Model: The plan model is link between the exercises and the programs. This allow for the creation of the workout plans. These two factors are defined by Foreign keys.
- [forms.py](./base/forms.py): Contains two Classes. The form for the exercises and the form for the programs. In the project the Categories are implemente using the exercises form, and the programs are defined using the program form.
- [urls.py](./base/urls.py): Contains all relevant urls for this project. The Project Pages being the only dynamic url required for this project.
- [views.py](./base/views.py): This is the heart of the back-end and here we find the main features of the application. The views has 12 functions for different operations.
  - def index: Takes current user, exercises from catalog and the user's program and load them into the index.html.
  - def login_view, logout_view & register: Handle the user account management for registration, log in and out.
  - search_exercise: Takes query by the user and uses django's icontain to fetch the relevant information required by the user. The search is performed on partial matches and is case insensitive.
  - add_program: Adds the named program to the database, this information comes through the ProgramForm
  - add_exercise: Links the exercise to a program using the Plan database, this relational database generate unique relations of exercises and programs that are late filtered to be able to load all exercises in any particular program.
  - programs_view: Filters the program required and load its page
  - edit_program & delete_program: Updates database and delete instances from the database using the program's id to find the correct instance.
  - delete_exercise: Simply remove an exercise from a particular program. This is achieved by deleting the relational instance in the Plan database.

---

## External resources

- Images: The images used for this project come from different sources and are free to use.
- Icons: The Icons used are from "Awersome Icons" and are free to use.
