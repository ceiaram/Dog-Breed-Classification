function displaySelectedImage(input, target) {
  let file = input.files[0];
  let reader = new FileReader();

  reader.readAsDataURL(file);
  reader.onload = function () {
    let img = document.getElementById(target);
    img.src = reader.result;
  };
  //   var imageDiv = document.getElementById("image");
  //   imageDiv.style.display = "block"
}
