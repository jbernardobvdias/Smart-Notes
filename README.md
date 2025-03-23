# Smart Notes

Smart notes is a note-taking tool that uses LLMs to parse through notes and this way making it easier to find information.

This will put all the notes into a vector space so that the model can quickly read them.

## How to run:

In order to run this tool there are a few steps you need to do:

1. Install dependencies:

```sh
$ python -m pip install --upgrade pip
$ pip install -r requirements.txt
```

2. Run the django front project:

```sh
$ python manage.py runserver
```

## To-do:

Frontend:
- [ ] Implement page to select the notes or the LLM;
- [ ] Implement page to use LLM;
- [ ] Implement page to take, select, and delete notes;
- [ ] (opt.) Make frontend look nice;

Backend:
- [ ] Implement API;
- [ ] Implement DB;
- [ ] Implement LLM;
- [ ] Implement connection between LLM and DB;