
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-app.js";

import { getFirestore,collection,addDoc,getDocs } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";

async function loadRooms() {

  const querySnapshot = await getDocs(
    collection(db, "rooms")
  );

  querySnapshot.forEach((doc) => {

    console.log(doc.id, doc.data());

  });
}

 const firebaseConfig = {
    apiKey: "AIzaSyDwgMuyUjo9WHVjPJhZzFAz_jUWlCA9ehU",
    authDomain: "wiki-9405e.firebaseapp.com",
    databaseURL: "https://wiki-9405e-default-rtdb.firebaseio.com",
    projectId: "wiki-9405e",
    storageBucket: "wiki-9405e.firebasestorage.app",
    messagingSenderId: "78843707374",
    appId: "1:78843707374:web:4a3bb78647b1f38cce18ff",
    measurementId: "G-88MQPB4F5H"
  };

// Inicializa
const app = initializeApp(firebaseConfig);

// Banco
const db = getFirestore(app);

let currentUser = null;
let currentRoom = null;

const users = JSON.parse(localStorage.getItem("users")) || [];
const rooms = JSON.parse(localStorage.getItem("rooms")) || [];

// ======================
// TELAS
// ======================

const authScreen = document.getElementById("auth-screen");
const dashboardScreen = document.getElementById("dashboard-screen");
const roomScreen = document.getElementById("room-screen");

function showScreen(screen) {
  authScreen.classList.remove("active");
  dashboardScreen.classList.remove("active");
  roomScreen.classList.remove("active");

  screen.classList.add("active");
}

// ======================
// LOGIN
// ======================

document.getElementById("login-btn").addEventListener("click", () => {

  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  if (!email || !password) {
    alert("Preencha todos os campos");
    return;
  }

  const existingUser = users.find(user => user.email === email);

  if (!existingUser) {
    users.push({ email, password });
    localStorage.setItem("users", JSON.stringify(users));
  }

  currentUser = email;

  renderRooms();

  showScreen(dashboardScreen);
});

// ======================
// LOGOUT
// ======================

document.getElementById("logout-btn").addEventListener("click", () => {
  currentUser = null;
  showScreen(authScreen);
});

// ======================
// CRIAR SALA
// ======================

document.getElementById("create-room-btn").addEventListener("click", () => {

  const roomName = document.getElementById("room-name").value;

  if (!roomName) {
    alert("Digite o nome da sala");
    return;
  }

  const room = {
    id: Date.now(),
    name: roomName,
    participants: [],
    expenses: []
  };

  rooms.push(room);

  localStorage.setItem("rooms", JSON.stringify(rooms));

  document.getElementById("room-name").value = "";

  renderRooms();
});

// ======================
// LISTAR SALAS
// ======================

function renderRooms() {

  const roomsList = document.getElementById("rooms-list");

  roomsList.innerHTML = "";

  rooms.forEach(room => {

    const div = document.createElement("div");

    div.classList.add("room-card");

    div.innerHTML = `
      <h3>${room.name}</h3>
      <p>${room.participants.length} participantes</p>
    `;

    div.addEventListener("click", () => {
      openRoom(room.id);
    });

    roomsList.appendChild(div);
  });
}

// ======================
// ABRIR SALA
// ======================

function openRoom(roomId) {

  currentRoom = rooms.find(room => room.id === roomId);

  document.getElementById("room-title").innerText = currentRoom.name;

  renderParticipants();
  renderExpenses();
  calculateBalances();

  showScreen(roomScreen);
}

// ======================
// VOLTAR
// ======================

document.getElementById("back-btn").addEventListener("click", () => {
  renderRooms();
  showScreen(dashboardScreen);
});

// ======================
// PARTICIPANTES
// ======================

document.getElementById("add-participant-btn").addEventListener("click", () => {

  const participantName = document.getElementById("participant-name").value;

  if (!participantName) {
    alert("Digite um nome");
    return;
  }

  currentRoom.participants.push(participantName);

  localStorage.setItem("rooms", JSON.stringify(rooms));

  document.getElementById("participant-name").value = "";

  renderParticipants();
});

function renderParticipants() {

  const list = document.getElementById("participants-list");

  const select = document.getElementById("expense-paid-by");

  list.innerHTML = "";
  select.innerHTML = "";

  currentRoom.participants.forEach(participant => {

    const li = document.createElement("li");

    li.innerText = participant;

    list.appendChild(li);

    const option = document.createElement("option");

    option.value = participant;
    option.innerText = participant;

    select.appendChild(option);
  });
}

// ======================
// DESPESAS
// ======================

document.getElementById("add-expense-btn").addEventListener("click", () => {

  const description = document.getElementById("expense-description").value;

  const value = parseFloat(
    document.getElementById("expense-value").value
  );

  const paidBy = document.getElementById("expense-paid-by").value;

  if (!description || !value || !paidBy) {
    alert("Preencha todos os campos");
    return;
  }

  currentRoom.expenses.push({
    description,
    value,
    paidBy
  });

  localStorage.setItem("rooms", JSON.stringify(rooms));

  document.getElementById("expense-description").value = "";
  document.getElementById("expense-value").value = "";

  renderExpenses();
  calculateBalances();
});

function renderExpenses() {

  const list = document.getElementById("expenses-list");

  list.innerHTML = "";

  currentRoom.expenses.forEach(expense => {

    const li = document.createElement("li");

    li.innerHTML = `
      <strong>${expense.description}</strong><br>
      R$ ${expense.value.toFixed(2)} - Pago por ${expense.paidBy}
    `;

    list.appendChild(li);
  });
}

// ======================
// CÁLCULO
// ======================

function calculateBalances() {

  const summary = document.getElementById("summary");

  summary.innerHTML = "";

  if (currentRoom.participants.length === 0) {
    return;
  }

  const total = currentRoom.expenses.reduce(
    (sum, expense) => sum + expense.value,
    0
  );

  const perPerson = total / currentRoom.participants.length;

  const balances = {};

  currentRoom.participants.forEach(person => {
    balances[person] = -perPerson;
  });

  currentRoom.expenses.forEach(expense => {
    balances[expense.paidBy] += expense.value;
  });

  const debtors = [];
  const creditors = [];

  for (const person in balances) {

    if (balances[person] < 0) {
      debtors.push({
        name: person,
        amount: Math.abs(balances[person])
      });
    } else {
      creditors.push({
        name: person,
        amount: balances[person]
      });
    }
  }

  debtors.forEach(debtor => {

    creditors.forEach(creditor => {

      if (debtor.amount > 0 && creditor.amount > 0) {

        const payment = Math.min(
          debtor.amount,
          creditor.amount
        );

        const p = document.createElement("p");

        p.innerText = `
          ${debtor.name} deve pagar
          R$ ${payment.toFixed(2)}
          para ${creditor.name}
        `;

        summary.appendChild(p);

        debtor.amount -= payment;
        creditor.amount -= payment;
      }
    });
  });
}