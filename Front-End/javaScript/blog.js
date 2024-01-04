console.log("In BLog.js File");
// var moment = require("moment");
const blogData = () => {
  // event.prevenetDefault();

  var title = document.getElementById("title").value;
  var author = document.getElementById("author").value;
  // var updatedTimestamp = document.getElementById("updatedTimestamp").value;
  var category = document.getElementById("category").value;
  var content = document.getElementById("content").value;
  var updatedTimestamp = new Date();
  var formatedDateTime = updatedTimestamp.toISOString();

  var formData = new FormData();
  formData.append("title", title);
  formData.append("author", author);
  formData.append("updatedTimestamp", updatedTimestamp);
  formData.append("category", category);
  formData.append("content", content);
  formData.append("updatedTimestamp", formatedDateTime);
  if (formData) {
    try {
      const response = fetch("http://localhost:8080/cms/blog/addblog", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      })
        .then((response) => {
          if (response.status == 415) {
            displayNotification("Something went wrong.....");
          } else if (response.ok) {
            displayNotification("Data Added Successfully...");
          }
        })
        .then((data) => console.log("SUccess", data))
        .catch((err) => console.log("Error", err));
    } catch (error) {
      displayNotification("Adding Blog added Failed...");
    }
  }

  // const data = {
  //   title: document.getElementById("title").value,
  //   author: document.getElementById("author").value,
  //   time: document.getElementById("time").value,
  //   category: document.getElementById("category").value,
  //   content: document.getElementById("content").value,
  // };

  // setTimeout(() => {
  //   window.location.reload();
  // // }, 2000);
  // console.log("Form Data: ", data);

  // Your logic to handle the form data (send to server, store in database, etc.) goes here
  // For now, let's just alert the user with the data
  // alert("Form submitted successfully!\n" + JSON.stringify(data));

  function displayNotification(msg) {
    Swal.fire({
      icon: "error",
      title: msg,
    });
  }
};
