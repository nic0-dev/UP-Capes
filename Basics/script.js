//Get the button:
top_button = document.getElementById("scroll-top");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    top_button.style.display = "inline-block";
  } else {
    top_button.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function toTop() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

function validateForm() {
  var username = document.getElementById("Username").value;
  var password = document.getElementById("Password").value;
  if (username == "sun" && password == "moon") {
    document.getElementById("account-form").style.display = 'none';
    document.getElementById("error-message").style.display = 'none';
    document.getElementById("sign-in-success").style.display = 'block';
  }
  else {
    document.getElementById("error-message").style.display = 'block';
  }
}