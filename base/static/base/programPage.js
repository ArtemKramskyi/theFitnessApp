 // Elements
 const modal = document.querySelector('.modal');
 const showModalButton = document.querySelector('.show-modal');
 const closeModalButton = document.querySelector('.close-modal');
 const editProgramButton = document.querySelector('.add-modal');
 const deleteProgramButton = document.querySelector('.deleteProgramButton');
 const removeExerciseButtons = document.querySelectorAll('.remove-exercise');
 
    // Event handlers
 const showModal = () => {
    modal.classList.remove('hidden');
 }
 
 const hideModal = () => {
    modal.classList.add('hidden');
 }
 
 const submitProgramForm = () => {
    document.forms['editProgramForm'].requestSubmit()
 }
 
 const submitRemoveExerciseForm = (event) => {
    const currentFormName = event.target.parentElement.id;
    document.forms[currentFormName].requestSubmit();
 }

 const submitDeleteProgramForm = () => {
    document.forms['deleteProgramForm'].requestSubmit()
 }
 
    // Event listeners
 showModalButton.addEventListener("click", showModal)
 closeModalButton.addEventListener("click", hideModal);
 editProgramButton.addEventListener("click", submitProgramForm);
 deleteProgramButton.addEventListener("click", submitDeleteProgramForm)
 for (let i = 0; i < removeExerciseButtons.length; i++) {
    removeExerciseButtons[i].addEventListener("click", submitRemoveExerciseForm);
 }