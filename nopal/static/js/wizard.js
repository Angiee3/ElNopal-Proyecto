const prevBtns = document.querySelectorAll(".btn-prev");
const nextBtns = document.querySelectorAll(".btn-next");
const progress = document.getElementById("progress");
const formSteps = document.querySelectorAll(".form-step");
const progressSteps = document.querySelectorAll(".progress-step");

let formStepsNum = 0;

nextBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    formStepsNum++;
    updateFormSteps();
    updateProgressbar();
  });
});

prevBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    formStepsNum--;
    updateFormSteps();
    updateProgressbar();
  });
});

function updateFormSteps() {
  formSteps.forEach((formStep) => {
    formStep.classList.contains("form-step-active") &&
      formStep.classList.remove("form-step-active");
  });

  formSteps[formStepsNum].classList.add("form-step-active");
}

function updateProgressbar() {
  progressSteps.forEach((progressStep, idx) => {
    if (idx < formStepsNum + 1) {
      progressStep.classList.add("progress-step-active");
    } else {
      progressStep.classList.remove("progress-step-active");
    }
  });

  const progressActive = document.querySelectorAll(".progress-step-active");

  progress.style.width =
    ((progressActive.length - 1) / (progressSteps.length - 1)) * 100 + "%";
}
// function buildStepsBreadcrumb (wizard, element, steps) {
//     const $steps = document.getElementById(element)
//     $steps.innerHTML = ''
//     for (let label in steps) {
//       if (steps.hasOwnProperty(label)) {
//         const $li = document.createElement('li')
//         const $a = document.createElement('a')
//         $li.classList.add('nav-item')
//         $a.classList.add('nav-link')
//         if (steps[label].active) {
//           $a.classList.add('active')
//         }
//         $a.setAttribute('href', '#')
//         $a.innerText = label
//         $a.addEventListener('click', e => {
//           e.preventDefault()
//           wizard.revealStep(label)
//         })
//         $li.appendChild($a)
//         $steps.appendChild($li)
//       }
//     }
//   }
  
//   function onStepChange(wizard, selector) {
//       const steps = wizard.getBreadcrumb()
//       buildStepsBreadcrumb(wizard, selector, steps)
//   }
  
//   const wizard = new window.Zangdar('#wizard', {
//     onStepChange: () => {
//       onStepChange(wizard, 'steps-native')
//     },
//     onSubmit(e) {
//       e.preventDefault()
//       console.log(e.target.elements)
//       return false
//     }
//   })
  
//   onStepChange(wizard, 'steps-native')