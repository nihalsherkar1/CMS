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

function submitForm() {
  var username = document.getElementById("name").value;
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;
  // repassword: document.getElementById("repassword").value,
  var imageInput = document.getElementById("image");

  var formData = new FormData();
  formData.append("name", username);
  formData.append("email", email);
  formData.append("password", password);
  formData.append("repassword", repassword);
  formData.append("image", imageInput.files[0]);

  //HTTP request
  fetch("http://localhost:8080/cms/usercontroller/add", {
    method: "POST",
    // headers: { "Content-Type": "multipart/form-data" },
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => console.log("Success", data))
    .catch((error) => console.log("Error", error));
}
