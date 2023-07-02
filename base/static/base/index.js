    // Elements
const modal = document.querySelector('.modal');
const showModalButton = document.querySelector('.show-modal');
const closeModalButton = document.querySelector('.close-modal');
const addProgramButton = document.querySelector('.add-modal');
const addExerciseButtons = document.querySelectorAll('.add-exercise')

    // Event handlers
const showModal = () => {
    modal.classList.remove('hidden');
}

const hideModal = () => {
    modal.classList.add('hidden');
}

const submitProgramForm = () => {
    document.forms['addProgramForm'].requestSubmit()
}

const submitExerciseForm = (event) => {
    const currentFormName = event.target.parentElement.id;
    document.forms[currentFormName].submit();
}

    // Event listeners
showModalButton.addEventListener("click", showModal)
closeModalButton.addEventListener("click", hideModal);
addProgramButton.addEventListener("click", submitProgramForm);
for (let i = 0; i < addExerciseButtons.length; i++) {
    addExerciseButtons[i].addEventListener("click", submitExerciseForm);
}