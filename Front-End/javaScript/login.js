console.log("Login");

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
  // let email = document.getElementById("email").value;
  // let password = document.getElementById("password").value;
  // let checkme = document.getElementById("checkme");

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
        );

        console.log(typeof response.json);

        if (response.ok) {
          console.log("Login successfull");

          window.location.href = await "/index.html";
        } else {
          alert("Wrong password...Please Check");
        }
      } catch (error) {
        console.error("Error during login", error);
      }
    }
  } else {
    alert("You must accept the Terms & Conditions");
  }
};
