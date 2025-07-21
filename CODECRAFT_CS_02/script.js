const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const imageInput = document.getElementById("imageInput");

let originalImage = null;

imageInput.addEventListener("change", () => {
  const file = imageInput.files[0];
  if (!file) return;

  const img = new Image();
  const reader = new FileReader();

  reader.onload = function (e) {
    img.onload = function () {
      canvas.width = img.width;
      canvas.height = img.height;
      ctx.drawImage(img, 0, 0);
      originalImage = ctx.getImageData(0, 0, canvas.width, canvas.height);
    };
    img.src = e.target.result;
  };
  reader.readAsDataURL(file);
});

function getPasswordHash(password) {
  let hash = 0;
  for (let i = 0; i < password.length; i++) {
    hash = (hash + password.charCodeAt(i) * (i + 1)) % 256;
  }
  return hash;
}

function manipulateImage(encrypt = true) {
  const password = document.getElementById("password").value;
  if (!password) {
    alert("Please enter a password.");
    return;
  }

  if (!originalImage) {
    alert("Please upload an image first.");
    return;
  }

  const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
  const data = imageData.data;
  const key = getPasswordHash(password);

  for (let i = 0; i < data.length; i += 4) {
    // Encrypt/Decrypt each RGB channel
    data[i] = encrypt ? (data[i] + key) % 256 : (data[i] - key + 256) % 256;     // Red
    data[i + 1] = encrypt ? (data[i + 1] + key) % 256 : (data[i + 1] - key + 256) % 256; // Green
    data[i + 2] = encrypt ? (data[i + 2] + key) % 256 : (data[i + 2] - key + 256) % 256; // Blue
    // Alpha remains unchanged
  }

  ctx.putImageData(imageData, 0, 0);
}

function encryptImage() {
  manipulateImage(true);
}

function decryptImage() {
  manipulateImage(false);
}
