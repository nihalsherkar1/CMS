console.log("In BLog.js File");

const blogData = (e) => {
  //   var title = document.getElementById("title").value;
  //   var author = document.getElementById("author").value;
  //   var time = document.getElementById("time").value;
  //   var category = document.getElementById("category").value;
  //   var content = document.getElementById("content").value;

  e.preventDefault();

  const data = {
    title: document.getElementById("title").value,
    author: document.getElementById("author").value,
    time: document.getElementById("time").value,
    category: document.getElementById("category").value,
    content: document.getElementById("content").value,
  };

  setTimeout(() => {
    window.location.reload();
  }, 1000);
  console.log("Form Data: ", data);

  if (
    data.title.trim() === "" ||
    data.author.trim() === "" ||
    data.category.trim() === "" ||
    data.content.trim() === ""
  ) {
    console.error("Please fill in all fields.");
    return;
  }

  // Your logic to handle the form data (send to server, store in database, etc.) goes here
  // For now, let's just alert the user with the data
  alert("Form submitted successfully!\n" + JSON.stringify(data));
};
