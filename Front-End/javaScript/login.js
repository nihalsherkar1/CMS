console.log("Login");

// Import SweetAlert2
// import Swal from "sweetalert2";
// const Swal = require("sweetalert2");

const showPassword = () => {
  var pass = document.getElementById("password");
  var eye1 = document.getElementById("eye1");
  var eye2 = document.getElementById("eye2");

  if (pass.type == "password") {
    pass.type = "text";
    eye1.style.display = "block";
    eye2.style.display = "none";
  } else {
    pass.type = "password";
    eye1.style.display = "none";
    eye2.style.display = "block";
  }
};

// const login = () => {
//   let email = document.getElementById("email").value;
//   let password = document.getElementById("password").value;
//   let checkme = document.getElementById("checkme");

//   if (checkme.checked) {
//     console.log(email + ", " + password);

//     return true;
//   } else {
//     alert("Please agree to the terms and conditions");

//     return false;
//   }
// };

const loginForm = async (event) => {
  event.preventDefault(); // Prevent the default form submission behavior
  const data = {
    email: document.getElementById("email").value,
    password: document.getElementById("password").value,
    checkme: document.getElementById("checkme").checked,
  };

  if (data.checkme) {
    console.log("we are in first if condition");

    if (data.password) {
      console.log("In Password");
      try {
        console.log("Ready to fecth");
        const response = await fetch(
          "http://localhost:8080/cms/usercontroller/login",
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
          }
        )
          .then((response) => {
            if (response.ok) {
              console.log("login successfull");
              window.location.href = "/Front-End/index.html";
            } else if (response.status == 401) {
              displayNotification("Invalid Username or Password!!");

              // alert("Invalid Username or Password");
            }
          })
          .catch((error) => console.log("Error", error));
      } catch (error) {
        console.error("Error during login", error);
      }
    }
  } else {
    displayNotification("You must accept the Terms & Conditions..!!");
    // alert("You must accept the Terms & Conditions");
  }

  function displayNotification(msg) {
    Swal.fire({
      icon: "error",
      title: msg,
    });
  }
  // const forgetPassword = async () => {
  //   const { value } = await Swal.fire({
  //     title: "Forget Password",
  //     input: "forgetPassword",
  //     inputLabel: "Your password",
  //     inputPlaceholder: "Enter your Password",
  //   });
  //   if (email) {
  //     Swal.fire(`Entered email: ${forgetPassword}`);
  //   }
  // };
};
