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
    eye3.style.display = "none";
    eye4.style.display = "block";
  } else {
    pass.type = "password";
    eye3.style.display = "block";
    eye4.style.display = "none";
  }
};

// function submitForm() {
//   var username = document.getElementById("name").value;
//   var email = document.getElementById("email").value;
//   var password = document.getElementById("password").value;
//   // repassword: document.getElementById("repassword").value,
//   var imageInput = document.getElementById("image");

//   var formData = new FormData();
//   formData.append("name", username);
//   formData.append("email", email);
//   formData.append("password", password);
//   formData.append("repassword", repassword);
//   formData.append("image", imageInput.files[0]);

//   if (formData) {
//     try {
//       const response = fetch(
//         "http://localhost:8080/cms/usercontroller/register",
//         {
//           method: "POST",
//           // headers: { "Content-Type": "multipart/form-data" },
//           body: formData,
//         }
//       )
//         .then((response) => {
//           if (response.status == 400) {
//             displayNotification("All fields are required....");
//             // alert("All fields are required....");
//             return Promise.reject("All fields are required....");
//           } else if (response.ok) {
//             console.log("Registration Successfull");

//             setTimeout(() => {
//               window.location.reload();
//             }, 2000);
//           } else {
//             // Handle other HTTP status codes or unexpected situations
//             return Promise.reject("Unexpected response from server");
//           }
//         })
//         .then((data) => console.log("Success", data))
//         .catch((error) => console.log("Error", error));
//     } catch (error) {
//       displayNotification("Registration failed. Please try again.");
//       // alert("Registration failed. Please try again.");
//     }

//     function displayNotification(msg) {
//       Swal.fire({
//         icon: "error",
//         title: msg,
//       });
//     }

//     //HTTP request
//   }
// }

// Tejas JS COde

const showToast = (type, msg) => {
  var toast = document.getElementById("toast");
  toast.classList.add("show");
  toast.style.display = "block";

  if (type === "success") {
    toast.style.backgroundColor = "#07bc0c";
  } else if (type === "error") {
    toast.style.backgroundColor = "#e74c3c";
  } else if (type === "warning") {
    toast.style.backgroundColor = "#f1c40f";
  }
  toast.innerHTML = `${msg}`;

  setTimeout(() => {
    toast.style.display = "none";
    toast.classList.remove("show");
  }, 3000);
};

const reqFieldsValidation = () => {
  var name = document.getElementById("name").value;
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;
  var repassword = document.getElementById("repassword").value;

  if (name === " || email=== " || password === " || repassword ===") {
    showToast("error", "Please fill all the required fields");
  } else {
    return true;
  }
};
