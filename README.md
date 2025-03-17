# Smart Notes

Smart notes is a note-taking tool that uses LLMs to parse through notes and this way making it easier to find information.

This will put all the notes into a vector space so that the model can quickly read them.

## How to run:

This application is built using django, and it's separated into two parts, the frontend and the backend. This means that you need to run two django applications at the same time in order for the system to work.

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