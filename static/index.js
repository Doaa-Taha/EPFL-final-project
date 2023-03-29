  //    // this script will run only in homepage(index.html)
// / select the required elements
const logoutBtn = document.getElementById("logout");
const message = document.getElementById("msg");

// define listener function
const logout = () => {
    localStorage.removeItem("username");
}

// check if the user has logged before and redirect him to the login page if not 
const handleSignedUser = () => {
    const username = localStorage.getItem("username");
    if (username == null){
        location.assign("http://127.0.0.1:5000/login");
    }else{
        message.innerHTML = `Welcome <b>${username}</b>`
    }
}
// add event listener
logoutBtn.addEventListener("click", logout);

// run the program
handleSignedUser()