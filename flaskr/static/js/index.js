// Displays the selected image in html
function displaySelectedImage(input, target) {
  let file = input.files[0];
  let reader = new FileReader();

  reader.readAsDataURL(file);
  reader.onload = function () {
    let img = document.getElementById(target);
    img.src = reader.result;

    displayBtn(); //Now the Upload button can show
    localStorage.setItem("imageData", reader.result); // Store image on local storage
  };
}

// Displays the upload button when an image is selected
function displayBtn() {
  let btn = document.getElementById("upload-button");
  btn.style.display = "block";
}
