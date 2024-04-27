let subscriberData;
let payment_amount;


// ================ Open and Close Mobile Menu 
document.querySelector(".mobile-menu__close").addEventListener("click", () => {
  document.querySelector(".mobile-menu").classList.toggle("toggle");
  document.querySelector(".overlay").classList.toggle("show");
});

document.querySelectorAll(".header__menu-toggle").forEach((item) => {
  item.addEventListener("click", () => {
    document.querySelector(".mobile-menu").classList.toggle("toggle");
    document.querySelector(".overlay").classList.toggle("show");
  });
});

// ================ Open and Close Mobile Submenu 
document.querySelector(".mobile__expand-icon").addEventListener("click", () => {
  document.querySelector(".mobile__submenu").classList.toggle("open");
});

// ================ Get The Current Year 
const currentYear = new Date().getFullYear();
document.getElementById("current-year").innerHTML = currentYear;

// ================ Activate Progress bar ================
const steps = document.querySelectorAll(".steps-names > span");
const progressBar = document.querySelector(".progress-bar");
const nextBtn = document.getElementById("next-btn");

const oneSpan = steps[0];
let spanStyle = window.getComputedStyle(oneSpan);
const widthStep = parseInt(spanStyle.width);

progressBar.style.width = `${widthStep / 2}px`;

// ================= Hide Input Label 
const inputFields = document.querySelectorAll(".step__input");

inputFields.forEach((item) => {
  item.addEventListener("input", () => {
    if (item.value.trim() !== "") {
      item.parentElement.classList.remove("error");
      item.parentElement.querySelector(".step__label--one").style.visibility =
        "hidden";
    } else {
      item.parentElement.querySelector(".step__label--one").style.visibility =
        "visible";
    }
  });
});

// ================= Open & Close Step Menu =================
const selectContainers = document.querySelectorAll(
  ".step__input-container--select"
);
const options = document.querySelectorAll(".step__menu-option");

for (let i = 0; i < selectContainers.length; i++) {
  const selectContainer = selectContainers[i];
  selectContainer.addEventListener("click", () => {
    selectContainer.querySelector(".step__menu").classList.toggle("show");
    selectContainer.querySelector(".step__icon").classList.toggle("rotate");
  });
}

for (let i = 0; i < options.length; i++) {
  const option = options[i];
  const optionsList = option.parentElement;

  option.addEventListener("click", (e) => {
    e.stopPropagation();
    if (optionsList.classList.contains("show")) {
      option.parentElement.classList.remove("show");
      optionsList.parentElement
        .querySelector(".step__icon")
        .classList.remove("rotate");

      optionsList.parentElement.querySelector(".step__hidden-input").value =
        option.dataset.value;
      optionsList.parentElement.querySelector(".step__label--one").innerHTML =
        option.dataset.value;
      optionsList.parentElement.querySelector(".step__label--one").style.color =
        "var(--primary-color)";
      optionsList.parentElement.classList.remove("error");
    }
  });
}

const paymentFields = document.querySelectorAll(".payment__input-field");

paymentFields.forEach((item) => {
  item.addEventListener("input", () => {
    if (!isEmpty(item.value)) {
      item.parentElement.classList.remove("error");
    }
  });
});
// ================= Validate Form =================
const submit_btn = document.getElementById("submit-btn");
submit_btn.addEventListener("click", async (e) => {
  e.preventDefault();
  const rulesCheckBox = document.querySelector("#rules");

  let isValid = true;

  paymentFields.forEach((item) => {
    if (isEmpty(item.value)) {
      item.parentElement.classList.add("error");
      isValid = false;
    }
  });

  if (!rulesCheckBox.checked) {
    rulesCheckBox.classList.add("error");
    isValid = false;
  }

  if (isValid) {
    updateProgressBar();
    goToNextStep(7);
    const form = document.querySelector("#payment_form");
    const formData = new FormData(form);
    const data = Object.fromEntries(formData);
    const amount = document.querySelector("#payment_amount > span")


    data["amount"] = payment_amount;
    data["subscriber"] = subscriberData.id;
    data["method"] = "VISA";
    

    // Change the endpoint to the payment submission endpoint
    try{
    const response = await fetch("http://127.0.0.1:8000/subscription/payments/", {  // Replace with your actual endpoint
      method: "POST",
      body: JSON.stringify(data),
      headers: { "Content-Type": "application/json" },  // Set content type header
    })
    const responseData = await response.json()
    console.log("Success");
    }catch(error){
      console.error("Error:", error);
    }

  }
});


const radioOptions = document.querySelectorAll(".step__label--radio");
radioOptions.forEach((item) => {
  item.addEventListener("click", () => {
    item.parentElement.parentElement.querySelector(".error-msg").style.display =
      "none";
    item.parentElement.querySelector(".hidden-input").value =
      item.dataset.value;
  });
});

const checkboxOptions = document.querySelectorAll(".step__label--checkbox");

checkboxOptions.forEach((item) => {
  item.addEventListener("click", () => {
    item.parentElement.parentElement.querySelector(".error-msg").style.display =
      "none";
  });
});

// ================= Utility Functions =================
function getStepFields(num) {
  const step = document.getElementById(`step${num}`);
  let fields;
  if (num === 3 || num === 4 || num === 5) {
    fields = step.querySelectorAll(".step__checkbox");
  } else {
    fields = step.querySelectorAll(
      ".step__input, .step__hidden-input, .step__radio, .step__checkbox, .payment__input-field"
    );
  }

  return fields;
}

function updateProgressBar() {
  progressBar.style.width = `${
    parseInt(progressBar.style.width) + widthStep + 3
  }px`;
}

function showErrorMsg(name) {
  const errorMsg = document.getElementById(`${name}__error-msg`);
  errorMsg.textContent = errorMsg.dataset.msg;
  errorMsg.style.display = "block";
}

function updateFormData(stepNumber, data) {
  const fields = getStepFields(stepNumber);
  let collectedData = [];
  let currentName;
  fields.forEach((item) => {
    currentName = item.name
    if (item.checked === true) {
      collectedData.push(item.value);
    }
  });
  if (collectedData.length === 0) {
    showErrorMsg(currentName);
    isValid = false;
  } else {
    data[currentName] = collectedData;
  }
}


function isEmpty(value) {
  return value.trim() === "";
}

function addErrorClass(id) {
  const containerWithError = document.querySelector(
    `.step__input-container input#${id}`
  ).parentElement;
  containerWithError.classList.add("error");
}

function validateEmail(email) {
  const re =
    /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return re.test(String(email).toLowerCase());
}

function goToNextStep(currentStep) {
  const currentStepElement = document.getElementById(`step${currentStep}`);
  const nextStepElement = document.getElementById(`step${currentStep + 1}`);

  currentStepElement.style.display = "none";
  nextStepElement.style.display = "flex";
}

// ================= Validate Step =================
function validateStep(stepNumber) {
  const step = document.getElementById(`step${stepNumber}`);
  const fields = getStepFields(stepNumber);

  let isValid = true;

  for (let item of fields) {
    switch (item.name) {
      case "first_name":
      case "last_name":
      case "age":
      case "gender":
      case "nationality":
      case "whatsapp":
      case "email":
      case "difficulties":
        if (isEmpty(item.value)) {
          addErrorClass(item.name);
          isValid = false;
        }
        break;

      case "email":
        if (!validateEmail(item.value)) {
          addErrorClass(item.name);
          isValid = false;
        }
        break;

      case "level":
      case "class":
      case "curriculum":
      case "students":
      case "time_period":
      case "time":
      case "session":
      case "hours":
      case "subscription":
        const hiddenInput = step.querySelector(`#${item.name}__hidden-input`);

        if (isEmpty(hiddenInput.value)) {
          showErrorMsg(item.name);
          isValid = false;
        }
        break;

      case "goals":
      case "days":
      case "subjects":
        const checkedFields = Array.from(fields).filter(item => item.checked);
        if (checkedFields.length === 0) {
          showErrorMsg(item.name);
          isValid = false;
        }
    }


  }


  if (isValid) {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });

    updateProgressBar();

    goToNextStep(stepNumber);
  }
}




// ================= Populate Education Level Data from backend =================
const educationLevelsContainer = document.querySelector('#education_levels'); // Assuming this is the container element
const hiddenInput = document.getElementById('level__hidden-input'); // Hidden input for storing selected level

function generateEducationLevelOptions(educationLevels) {

  // Clear existing options
  educationLevelsContainer.innerHTML = '';

  // Loop through education levels and create radio button options
  educationLevels.forEach(level => {
    const label = document.createElement('label');
    label.classList.add('step__label-box', 'step__label', 'step__label--radio');
    label.setAttribute('data-value', level.level);

    const correctIcon = document.createElement('img');
    correctIcon.src = './assets/images/correct-icon.svg';
    correctIcon.alt = 'correct icon';
    correctIcon.classList.add('correct-icon');
    label.appendChild(correctIcon);

    const labelText = document.createTextNode(level.level);
    label.appendChild(labelText);

    const radioInput = document.createElement('input');
    radioInput.type = 'radio';
    radioInput.id = `level${level.id}`;
    radioInput.name = 'education_level';
    radioInput.value = level.id;
    radioInput.classList.add('step__radio');
    label.appendChild(radioInput);

    educationLevelsContainer.appendChild(label);
  });

  // Add event listener to update hidden input on radio button change
  const radioButtons = document.querySelectorAll('.step__radio');
  radioButtons.forEach(radioButton => {
    radioButton.addEventListener('change', () => {
      if (radioButton.checked) {
        hiddenInput.value = radioButton.value;
      }
    });
  });
}

// ================== Populate Class Level Data from backend =================

// Assuming this is the container element for class options
const classLevelsContainer = document.querySelector('#class_years');
const hiddenClassInput = document.getElementById('class__hidden-input');

// Function to generate class level options (similar to education levels)
function generateClassLevelOptions(classLevels) {



  classLevelsContainer.innerHTML = '';  // Clear existing options

  classLevels.forEach(classLevel => {
    const label = document.createElement('label');
    label.classList.add('step__label-box', 'step__label', 'step__label--radio');
    label.setAttribute('data-value', classLevel.year); 

    const correctIcon = document.createElement('img');
    correctIcon.src = './assets/images/correct-icon.svg';
    correctIcon.alt = 'correct icon';
    correctIcon.classList.add('correct-icon');
    label.appendChild(correctIcon);

    const labelText = document.createTextNode(classLevel.year); 
    label.appendChild(labelText);

    const radioInput = document.createElement('input');
    radioInput.type = 'radio';
    radioInput.id = `class${classLevel.id}`; // Assuming 'id' property
    radioInput.name = 'class_year';
    radioInput.value = classLevel.id; 
    radioInput.classList.add('step__radio');
    label.appendChild(radioInput);

    classLevelsContainer.appendChild(label);
  });

  // Add event listener to update hidden input on radio button change (similar to education levels)
  const radioButtons = document.querySelectorAll('.step__radio');
  radioButtons.forEach(radioButton => {
    radioButton.addEventListener('change', () => {
      if (radioButton.checked) {
        hiddenClassInput.value = radioButton.value;
      }
    });
  });
}

// ================ Populate Curriculum Data from backend ================
// Assuming this is the container element for curriculum options
const curriculumLevelsContainer = document.querySelector('#curriculum');
const hiddenCurriculumInput = document.getElementById('curriculum__hidden-input');

// Function to generate curriculum options (similar to education levels)
function generateCurriculumOptions(curriculumData) {
  curriculumLevelsContainer.innerHTML = '';  // Clear existing options

  curriculumData.forEach(curriculum => {
    const label = document.createElement('label');
    label.classList.add('step__label-box', 'step__label', 'step__label--radio');
    label.setAttribute('data-value', curriculum.cirriculum); 

    const correctIcon = document.createElement('img');
    correctIcon.src = './assets/images/correct-icon.svg';
    correctIcon.alt = 'correct icon';
    correctIcon.classList.add('correct-icon');
    label.appendChild(correctIcon);

    const labelText = document.createTextNode(curriculum.cirriculum); 
    label.appendChild(labelText);

    const radioInput = document.createElement('input');
    radioInput.type = 'radio';
    radioInput.id = `curriculum${curriculum.id}`; // Assuming 'id' property
    radioInput.name = 'cirriculum';
    radioInput.value = curriculum.id; 
    radioInput.classList.add('step__radio');
    label.appendChild(radioInput);

    curriculumLevelsContainer.appendChild(label);
  });

  // Add event listener to update hidden input on radio button change (similar to education levels)
  const radioButtons = document.querySelectorAll('.step__radio');
  radioButtons.forEach(radioButton => {
    radioButton.addEventListener('change', () => {
      if (radioButton.checked) {
        hiddenCurriculumInput.value = radioButton.value;
      }
    });
  });
}

// ================= Populate Subjects data from backend =============
const subjectsContainer = document.querySelector('#subjects');

// Function to generate subject options
function generateSubjectOptions(subjects) {
  subjectsContainer.innerHTML = '';  // Clear existing options

  subjects.forEach(subject => {
    const label = document.createElement('label');
    label.classList.add('step__label-box', 'step__label', 'step__label--checkbox');
    label.setAttribute('data-value', subject.subject);

    const correctIcon = document.createElement('img');
    correctIcon.src = './assets/images/correct-icon.svg';
    correctIcon.alt = 'correct icon';
    correctIcon.classList.add('correct-icon');
    label.appendChild(correctIcon);

    const subjectImg = document.createElement('img');
    subjectImg.src = subject.image; // Assuming 'image' property in the object
    subjectImg.alt = `${subject.subject} subject`;
    subjectImg.classList.add('subject-img');
    label.appendChild(subjectImg);

    const labelText = document.createTextNode(subject.subject);
    label.appendChild(labelText);

    const checkBoxInput = document.createElement('input');
    checkBoxInput.type = 'checkbox';
    checkBoxInput.id = `subject${subject.id}`; // Assuming 'id' property
    checkBoxInput.name = 'subjects';
    checkBoxInput.value = subject.id;
    checkBoxInput.classList.add('step__checkbox');
    label.appendChild(checkBoxInput);

    subjectsContainer.appendChild(label);
  });
}

// ================= Populate Student Count data from backend ==================
const studentCountContainer = document.querySelector('#student_count');

// Function to generate student count options
function generateStudentCountOptions(studentCounts) {
  studentCountContainer.innerHTML = '';  // Clear existing options

  studentCounts.forEach(count => {
    const label = document.createElement('label');
    label.classList.add('step__label-box', 'step__label', 'step__label--radio');
    label.setAttribute('data-value', count.student_count);

    const correctIcon = document.createElement('img');
    correctIcon.src = './assets/images/correct-icon.svg';
    correctIcon.alt = 'correct icon';
    correctIcon.classList.add('correct-icon');
    label.appendChild(correctIcon);

    const labelText = document.createTextNode(count.student_count);
    label.appendChild(labelText);

    const radioInput = document.createElement('input');
    radioInput.type = 'radio';
    radioInput.id = `number${count.id}`;  // Assuming 'id' property
    radioInput.name = 'student_count';
    radioInput.value = count.id;
    radioInput.classList.add('step__radio');
    label.appendChild(radioInput);

    studentCountContainer.appendChild(label);
  });
}


// =============== Populate Academic Goals data from backend =================
const goalsContainer = document.querySelector('#academic_goals');

// Function to generate academic goal options
function generateAcademicGoalOptions(academicGoals) {
  goalsContainer.innerHTML = '';  // Clear existing options

  academicGoals.forEach(goal => {
    const label = document.createElement('label');
    label.classList.add('step__label-box', 'step__label', 'step__label--checkbox');
    label.setAttribute('data-value', goal.goal);

    const correctIcon = document.createElement('img');
    correctIcon.src = './assets/images/correct-icon.svg';
    correctIcon.alt = 'correct icon';
    correctIcon.classList.add('correct-icon');
    label.appendChild(correctIcon);

    const labelText = document.createTextNode(goal.goal);
    label.appendChild(labelText);

    const checkBoxInput = document.createElement('input');
    checkBoxInput.type = 'checkbox';
    checkBoxInput.id = `goal${goal.id}`;  // Assuming 'id' property
    checkBoxInput.name = 'academic_goals';
    checkBoxInput.value = goal.id;
    checkBoxInput.classList.add('step__checkbox');
    label.appendChild(checkBoxInput);

    goalsContainer.appendChild(label);
  });
}

// ================= Fetch Suitable Days from backend =================
const daysContainer = document.querySelector('#suitable_days');

// Function to generate suitable day options
function generateSuitableDayOptions(suitableDays) {
  daysContainer.innerHTML = '';  // Clear existing options

  suitableDays.forEach(day => {
    const label = document.createElement('label');
    label.classList.add('step__label-box', 'step__label', 'step__label--checkbox');
    label.setAttribute('data-value', day.day); // Assuming 'day' property

    const correctIcon = document.createElement('img');
    correctIcon.src = './assets/images/correct-icon.svg';
    correctIcon.alt = 'correct icon';
    correctIcon.classList.add('correct-icon');
    label.appendChild(correctIcon);

    const labelText = document.createTextNode(day.day);  // Assuming 'day' property
    label.appendChild(labelText);

    const checkBoxInput = document.createElement('input');
    checkBoxInput.type = 'checkbox';
    checkBoxInput.id = `day${day.id}`;  // Assuming 'id' property
    checkBoxInput.name = 'suitable_days';
    checkBoxInput.value = day.id;  
    checkBoxInput.classList.add('step__checkbox');
    label.appendChild(checkBoxInput);

    daysContainer.appendChild(label);
  });
}


// ================= Populate Suitable day periods data from backend =================
// Assuming this is the container element for time period options
const timePeriodContainer = document.querySelector('#suitable_day_periods');

function generateTimePeriodOptions(timePeriods) {
  timePeriodContainer.innerHTML = '';  // Clear existing options

  timePeriods.forEach(period => {
    const label = document.createElement('label');
    label.classList.add('step__label-box', 'step__label', 'step__label--radio');
    label.setAttribute('data-value', period.period); // Assuming 'period' property

    const correctIcon = document.createElement('img');
    correctIcon.src = './assets/images/correct-icon.svg';
    correctIcon.alt = 'correct icon';
    correctIcon.classList.add('correct-icon');
    label.appendChild(correctIcon);

    const labelText = document.createTextNode(period.period); // Assuming 'period' property
    label.appendChild(labelText);

    const radioInput = document.createElement('input');
    radioInput.type = 'radio';
    radioInput.id = `period${period.id}`;  // Assuming 'id' property
    radioInput.name = 'suitable_day_periods';
    radioInput.value = period.id;  
    radioInput.classList.add('step__radio');
    label.appendChild(radioInput);

    timePeriodContainer.appendChild(label);
  });
}

// ================= Populate suitable day times data from backend =================
const timeContainer = document.querySelector('#suitable_day_times');

// Function to generate suitable time options
function generateSuitableTimeOptions(suitableTimes) {
  timeContainer.innerHTML = '';  // Clear existing options

  suitableTimes.forEach(time => {
    const label = document.createElement('label');
    label.classList.add('step__label-box', 'step__label', 'step__label--radio');
    label.setAttribute('data-value', time.time); // Assuming 'time' property

    const correctIcon = document.createElement('img');
    correctIcon.src = './assets/images/correct-icon.svg';
    correctIcon.alt = 'correct icon';
    correctIcon.classList.add('correct-icon');
    label.appendChild(correctIcon);

    const labelText = document.createTextNode(time.time.slice(0, 5)); // Assuming 'time' property, extract only hours and minutes

    label.appendChild(labelText);

    const radioInput = document.createElement('input');
    radioInput.type = 'radio';
    radioInput.id = `time${time.id}`;  // Assuming 'id' property
    radioInput.name = 'suitable_day_times';
    radioInput.value = time.id;  
    radioInput.classList.add('step__radio');
    label.appendChild(radioInput);

    timeContainer.appendChild(label);
  });
}

// ================= Populate Weekly class counts from backend ==================
const sessionContainer = document.querySelector('#weekly_class_counts');
const classCountHiddenInput = document.querySelector('#session__hidden-input') 

// Function to generate suitable session (weekly class count) options
function generateSuitableSessionOptions(sessionCounts) {
  sessionContainer.innerHTML = '';  // Clear existing options

  sessionCounts.forEach(count => {
    const label = document.createElement('label');
    label.classList.add('step__label-box', 'step__label', 'step__label--radio');
    label.setAttribute('data-value', count.weekly_count); // Assuming 'weekly_count' property

    const correctIcon = document.createElement('img');
    correctIcon.src = './assets/images/correct-icon.svg';
    correctIcon.alt = 'correct icon';
    correctIcon.classList.add('correct-icon');
    label.appendChild(correctIcon);

    const labelText = document.createTextNode(count.weekly_count); // Assuming 'weekly_count' property
    label.appendChild(labelText);

    const radioInput = document.createElement('input');
    radioInput.type = 'radio';
    radioInput.id = `session${count.id}`;  // Assuming 'id' property
    radioInput.name = 'weekly_class_count';
    radioInput.value = count.id;  
    radioInput.classList.add('step__radio');
    label.appendChild(radioInput);
    sessionContainer.appendChild(label);

    radioInput.addEventListener('change', () => {
      if (radioInput.checked) {
        classCountHiddenInput.value = radioInput.value;
      }
    })

  });

}

// ================= Populate class times data from backend =================
const hoursContainer = document.querySelector('#class_times');
const hoursHiddenInput = document.querySelector('#hours__hidden-input')

// Function to generate suitable class time options
function generateSuitableClassTimeOptions(classTimes) {
  hoursContainer.innerHTML = '';  // Clear existing options

  classTimes.forEach(time => {
    const label = document.createElement('label');
    label.classList.add('step__label-box', 'step__label', 'step__label--radio');
    label.setAttribute('data-value', time.class_time); // Assuming 'class_time' property

    const correctIcon = document.createElement('img');
    correctIcon.src = './assets/images/correct-icon.svg';
    correctIcon.alt = 'correct icon';
    correctIcon.classList.add('correct-icon');
    label.appendChild(correctIcon);

    const labelText = document.createTextNode(time.class_time); // Assuming 'class_time' property
    label.appendChild(labelText);

    const radioInput = document.createElement('input');
    radioInput.type = 'radio';
    radioInput.id = `hour${time.id}`;  // Assuming 'id' property
    radioInput.name = 'class_time';
    radioInput.value = time.id;  
    radioInput.classList.add('step__radio');
    label.appendChild(radioInput);
    hoursContainer.appendChild(label);


    // Append both radio button and hidden input to the label (optional)
    radioInput.addEventListener('change', () => {
      if (radioInput.checked) {
        hoursHiddenInput.value = radioInput.value;
      }
    })

    
  });

  const radioButtons = document.querySelectorAll('.step__radio');
  radioButtons.forEach(radioButton => {
    radioButton.addEventListener('change', () => {
      if (radioButton.checked) {
        hoursHiddenInput.value = radioButton.value;
      }
    });
  });
}

// ================= Populate Subscription Plans data from backend =================
const subscriptionContainer = document.querySelector('#subscription_plans');
const subscriptionHiddenInput = document.querySelector('#subscription__hidden-input');

// Function to generate suitable subscription plan options
function generateSubscriptionPlansOptions(plans) {

  subscriptionContainer.innerHTML = '';  // Clear existing options

  plans.forEach(plan => {
    const label = document.createElement('label');
    label.classList.add('step__label-box', 'step__label', 'step__label--radio', 'subscription_label');

    // Assuming 'period' translates to months
    const months = plan.period;
    const semesters = plan.semesters;
    const cost = plan.cost;

    let discount = 0;
    if (months === 6) {
      discount = 10;
    } else if (months === 12) {
      discount = 15;
    } else if (months === 15) {
      discount = 20; 
    }

    label.setAttribute('data-value', `${months}months`); // Value for radio button

    const correctIcon = document.createElement('img');
    correctIcon.src = './assets/images/correct-icon.svg';
    correctIcon.alt = 'correct icon';
    correctIcon.classList.add('correct-icon');
    label.appendChild(correctIcon);

    const discountSpan = document.createElement('span');
    discountSpan.classList.add('subscription_discount');
    discountSpan.textContent = discount > 0 ? `خصم ${discount}%` : '';
    label.appendChild(discountSpan);

    const semesterSpan = document.createElement('span');
    semesterSpan.textContent = semesters === 1 ? 'فصل دراسي' : `${semesters} فصول دراسية`;
    label.appendChild(semesterSpan);

    const durationSpan = document.createElement('span');
    durationSpan.classList.add('subscription_duration');
    durationSpan.textContent = `${months} ${months === 1 ? 'شهر' : 'شهرًا'}`;
    label.appendChild(durationSpan);

    const priceSpan = document.createElement('span');
    priceSpan.classList.add('subscription_price');
    priceSpan.textContent = `${cost} درهم`;
    label.appendChild(priceSpan);

    const radioInput = document.createElement('input');
    radioInput.type = 'radio';
    radioInput.id = `plan${plan.id}`; // Assuming 'id' property
    radioInput.name = 'subscription_plan';
    radioInput.value = `${plan.id}`;  // Value for radio button
    radioInput.classList.add('step__radio');
    label.appendChild(radioInput);
    subscriptionContainer.appendChild(label);


    // Append both radio button and hidden input to the label
    radioInput.addEventListener('change', () => {
      if (radioInput.checked) {
        subscriptionHiddenInput.value = radioInput.value;
        const costDiv = document.querySelector("#payment_amount > span");
        costDiv.innerHTML = `الإجمالي: ${plan.cost} درهم`;
        payment_amount = plan.cost;
      }
    })
 
  });

}

// ================= Fetch data from backend =================

(async () => {
  const formOptions = await fetchFormOptions()
  const subscriptionPlans = await fetchSubscriptionPlansOptions()

  if (formOptions) {
    generateEducationLevelOptions(formOptions.education_levels); // Access education_levels directly
    generateClassLevelOptions(formOptions.class_years); 
    generateCurriculumOptions(formOptions.cirriculums);
    generateSubjectOptions(formOptions.subjects);
    generateStudentCountOptions(formOptions.student_counts);
    generateAcademicGoalOptions(formOptions.academic_goals);
    generateSuitableDayOptions(formOptions.suitable_days);
    generateTimePeriodOptions(formOptions.suitable_day_periods);
    generateSuitableTimeOptions(formOptions.suitable_day_times);
    generateSuitableSessionOptions(formOptions.weekly_class_counts);
    generateSuitableClassTimeOptions(formOptions.class_times);
  }
  if (subscriptionPlans) {
    generateSubscriptionPlansOptions(subscriptionPlans);
  }
}) ();

async function fetchFormOptions() {
  try {
    const response = await fetch("http://127.0.0.1:8000/education/subscription-form/");
    const data = await response.json();

    return data;

  } catch (error) {
    console.error("Error:", error);
    return null;  
  }
}

async function fetchSubscriptionPlansOptions() {
  try {
    const response = await fetch("http://127.0.0.1:8000/subscription/plans/");
    const data = await response.json();

    return data;

  } catch (error) {
    console.error("Error:", error);
    return null;  
  }
}

// ===================== Send user data before payment ======================
async function sendUserData() {

  const rulesCheckBox = document.querySelector("#rules");

  let isValid = true;

  if (isValid) {
    updateProgressBar();
    
    const form = document.querySelector("#contact_form");
    const formData = new FormData(form);
    const data = Object.fromEntries(formData);
    updateFormData(3, data);
    updateFormData(4, data);
    updateFormData(5, data);

    try{
    const response = await fetch("http://127.0.0.1:8000/user/subscribers/", {  
      method: "POST",
      body: JSON.stringify(data),
      headers: { "Content-Type": "application/json" },  
    })
    const responseData = await response.json()
    console.log("Success");
    subscriberData = responseData
    }catch(error){
      console.error("Error:", error);
    }

  }

}