//  // // /// this script will run only in login page(login.html)
const loginBtn = document.getElementById("in");
const inputField = document.getElementById("username");

// define listener function
const getAndSave = () =>{
    const nameValue = inputField.value;
    localStorage.setItem("username", nameValue);   
}


// add event listeners
loginBtn.addEventListener("click", getAndSave);

