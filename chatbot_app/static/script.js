const fileInput = document.getElementById("fileInput");
const pickBtn = document.getElementById("pickBtn");
const fileLabel = document.getElementById("fileLabel");
const uploadedFileEl = document.getElementById("uploadedFile");

const sendBtn = document.getElementById("sendBtn");
const attachBtn = document.getElementById("attachBtn");
const questionInput = document.getElementById("questionInput");
const messagesEl = document.getElementById("messages");

const continueBtn = document.getElementById("continueBtn");
const restartBtn = document.getElementById("restartBtn");

let uploaded = false;

pickBtn.onclick = () => fileInput.click();
attachBtn.onclick = () => fileInput.click();

fileInput.onchange = (e) => {
  const f = e.target.files[0];
  if (!f) return;

  uploaded = true;
  fileLabel.textContent = f.name;
  uploadedFileEl.textContent = f.name;

  addBot("Uploaded file: " + f.name);
};

function addUser(text) {
  const el = document.createElement("div");
  el.className = "msg user";
  el.textContent = text;
  messagesEl.appendChild(el);
  scrollBottom();
}

function addBot(text) {
  const el = document.createElement("div");
  el.className = "msg bot";
  el.textContent = text;
  messagesEl.appendChild(el);
  scrollBottom();
}

function scrollBottom() {
  messagesEl.scrollTop = messagesEl.scrollHeight;
}

sendBtn.onclick = send;

questionInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    send();
  }
});

function send() {
  const q = questionInput.value.trim();
  if (!q) return;

  if (!uploaded) {
    addBot("Please upload a file first.");
    return;
  }

  addUser(q);
  questionInput.value = "";

  setTimeout(() => {
    addBot("Generated answer: " + reverse(q));
  }, 700);
}

function reverse(t) {
  return t.split("").reverse().join("");
}

restartBtn.onclick = () => {
  uploaded = false;
  fileInput.value = "";
  fileLabel.textContent = "No file chosen";
  uploadedFileEl.textContent = "—";
  messagesEl.innerHTML = "";
  addBot("Restarted. Upload a new file.");
};

continueBtn.onclick = () => {
  if (!uploaded) addBot("Upload a file first.");
  else addBot("Continue mode activated.");
};

addBot("Vanakkam! Upload a file and start chatting.");
