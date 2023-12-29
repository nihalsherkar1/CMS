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

const login = () => {
  let email = document.getElementById("email").value;
  let password = document.getElementById("password").value;
  let checkme = document.getElementById("checkme");

  if (checkme.checked) {
    console.log(email + ", " + password);

    return true;
  } else {
    alert("Please agree to the terms and conditions");

    return false;
  }
};
