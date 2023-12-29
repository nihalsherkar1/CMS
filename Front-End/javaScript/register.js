console.log("Register");

const showPassword = () => {
  var pass = document.getElementById("password");
  var eye1 = document.getElementById("eye1");
  var eye2 = document.getElementById("eye2");

  if (pass.type === "password") {
    pass.type = "text";
    eye1.style.display = "block";
    eye2.style.display = "none";
  } else {
    pass.type = "password";
    eye1.style.display = "none";
    eye2.style.display = "block";
  }
};
const showRePassword = () => {
  var pass = document.getElementById("re-password");
  var eye3 = document.getElementById("eye3");
  var eye4 = document.getElementById("eye4");

  if (pass.type === "password") {
    pass.type = "text";
    eye3.style.display = "block";
    eye4.style.display = "none";
  } else {
    pass.type = "password";
    eye3.style.display = "none";
    eye4.style.display = "block";
  }
};
